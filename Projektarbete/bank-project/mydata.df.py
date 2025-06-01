import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database/database.db')

df1 = pd.read_csv('sebank_customers_with_accounts.csv')
df2 = pd.read_csv('transactions.csv')

df1.to_sql('customers', con=engine, if_exists='replace', index=False)
df2.to_sql('transactions', con=engine, if_exists='replace', index=False)

print("Data har importerats")

print("Första filen:")
print(df1.head())

print("\nAndra filen:")
print(df2.head())

# 1. Kontrollera om det finns några saknade värden (NaN)
print("Saknade värden i fil1:")
print(df1.isnull().sum())

print("\nSaknade värden i fil2:")
print(df2.isnull().sum())

# 2. Kontrollera datatyper
print("\nDatatyper i fil1:")
print(df1.dtypes)

print("\nDatatyper i fil2:")
print(df2.dtypes)

# 3. Grundläggande statistik (för numeriska kolumner)
print("\nStatistik fil1:")
print(df1.describe())

print("\nStatistik fil2:")
print(df2.describe())

# 4. Kontrollera om det finns dubbletter
print("\nAntal dubbletter i fil1:", df1.duplicated().sum())
print("Antal dubbletter i fil2:", df2.duplicated().sum())

# 5. Validera unika nycklar (exempel: om du har en kolumn 'ID' som ska vara unik)
if 'ID' in df1.columns:
    print("\nAntal unika ID i fil1:", df1['ID'].nunique())
    print("Totalt antal rader i fil1:", len(df1))

if 'ID' in df2.columns:
    print("\nAntal unika ID i fil2:", df2['ID'].nunique())
    print("Totalt antal rader i fil2:", len(df2))