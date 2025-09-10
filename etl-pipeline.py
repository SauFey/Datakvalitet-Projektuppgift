import pandas as pd
import re
import os
from datetime import datetime
from sqlalchemy import create_engine

# 1. Mappstruktur
raw_path = "./data/raw"
clean_path = "./data/clean"
bad_path = "./data/bad"
db_path = "./bank.db"

# os.makedirs(clean_path, exist_ok=True)
# os.makedirs(bad_path, exist_ok=True)

# 2. Läs in rådata
customers_file = f"{raw_path}/sebank_customers_with_accounts.csv"
transactions_file = f"{raw_path}/transactions.csv"

customers_accounts = pd.read_csv(customers_file)
transactions = pd.read_csv(transactions_file)

print(f"Kunder/Konton: {len(customers_accounts)}, Transaktioner: {len(transactions)}")

# --- 3. Valideringsfunktioner ---
def check_date(date_str):
    """Kolla om datum är giltigt, stöder både YYYY-MM-DD och YYYY-MM-DD HH:MM:SS"""
    for fmt in ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d"]:
        try:
            datetime.strptime(date_str, fmt)
            return True
        except:
            continue
    return False

iban_pattern = re.compile(r'^[A-Z]{2}\d{2}[A-Z0-9]{1,30}$')

# --- 4. Validering ---
## 4.1 Saknade värden
bad_customers_null = customers_accounts[customers_accounts.isnull().any(axis=1)]
bad_transactions_null = transactions[transactions.isnull().any(axis=1)]

## 4.2 Datumformat
bad_transactions_date = transactions[~transactions["timestamp"].astype(str).apply(check_date)]

## 4.3 IBAN
bad_accounts_iban = customers_accounts[
    ~customers_accounts["BankAccount"].astype(str).apply(lambda x: bool(iban_pattern.match(x)))
]

## 4.4 Negativa belopp
bad_transactions_negative = transactions[transactions["amount"] < 0]

## 4.5 Misstänkta transaktioner
bad_transactions_suspicious = transactions[transactions["amount"] > 100000]

# --- 5. Spara trasig data till Bad data ---
bad_customers_null.to_csv(f"{bad_path}/bad_customers_null.csv", index=False)
bad_transactions_null.to_csv(f"{bad_path}/bad_transactions_null.csv", index=False)
bad_transactions_date.to_csv(f"{bad_path}/bad_transactions_date.csv", index=False)
bad_accounts_iban.to_csv(f"{bad_path}/bad_accounts_iban.csv", index=False)
bad_transactions_negative.to_csv(f"{bad_path}/bad_transactions_negative.csv", index=False)
bad_transactions_suspicious.to_csv(f"{bad_path}/bad_transactions_suspicious.csv", index=False)

# --- 6. Skapa rena dataset ---
clean_customers_accounts = customers_accounts.drop(bad_customers_null.index).drop(bad_accounts_iban.index)
clean_transactions = transactions.drop(bad_transactions_null.index, errors="ignore").drop(bad_transactions_date.index, errors="ignore")


### 7. Ta bort dubbletter och lägg de i Bad data ###
dupes_customers = clean_customers_accounts[clean_customers_accounts.duplicated(subset=["BankAccount"], keep=False)]
dupes_transactions = clean_transactions[clean_transactions.duplicated(subset=["transaction_id"], keep=False)]

## Lägg dubbletter i Bad data
dupes_customers.to_csv(f"{bad_path}/bad_customers_duplicates.csv", index=False)
dupes_transactions.to_csv(f"{bad_path}/bad_transactions_duplicates.csv", index=False)

clean_customers_accounts = clean_customers_accounts.drop_duplicates(subset=["BankAccount"])
clean_transactions = clean_transactions.drop_duplicates(subset=["transaction_id"])

# --- 7. Spara rena filer ---
clean_customers_accounts.to_csv(f"{clean_path}/customers_accounts_clean.csv", index=False)
clean_transactions.to_csv(f"{clean_path}/transactions_clean.csv", index=False)

print("✅ Validering klar! Rensade CSV-filer sparade!")

# --- 8. Ladda upp till SQLite ---
engine = create_engine(f"sqlite:///{db_path}")

clean_customers_accounts.to_sql("customers_accounts_clean", engine, if_exists="replace", index=False)
clean_transactions.to_sql("transactions_clean", engine, if_exists="replace", index=False)

print(f"✅ Databasen {db_path} uppdaterad med rena tabeller.")

print("Antal transactions totalt:", len(transactions))
print("Null transactions:", len(bad_transactions_null))
print("Felaktigt datum:", len(bad_transactions_date))
print("Negativa belopp:", len(bad_transactions_negative))
print("Misstänkta belopp:", len(bad_transactions_suspicious))
print("Dubbletter customers:", len(dupes_customers))
print("Dubbletter transactions:", len(dupes_transactions))
print("Kvar efter rensning:", len(clean_transactions))
