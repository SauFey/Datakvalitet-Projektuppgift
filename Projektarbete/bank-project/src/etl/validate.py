import re
import pandas as pd

def validate_row(row):
    """
    Validerar en enskild rad från kunddata.
    Returnerar (True, None) om raden är giltig, annars (False, felorsak).
    """
    errors = []

    # Kontrollera kundnamn
    if not isinstance(row.get("Customer"), str) or not row["Customer"].strip():
        errors.append("Kundnamn saknas eller är ogiltigt.")

    # Kontrollera adress
    if not isinstance(row.get("Address"), str) or not row["Address"].strip():
        errors.append("Adress saknas eller är ogiltig.")

    # Kontrollera telefonnummer
    phone = str(row.get("Phone", ""))
    if not re.match(r"^(\\+46|0)[\\d\\s\\-()]{6,}$", phone):
        errors.append("Ogiltigt telefonnummer.")

    # Kontrollera personnummer
    pnr = str(row.get("Personnummer", ""))
    if not re.match(r"^\\d{6,8}-\\d{4}$", pnr):
        errors.append("Ogiltigt personnummerformat.")

    if errors:
        return False, "; ".join(errors)
    return True, None


def validate_data(df):
    """
    Validerar hela DataFrame med kunddata.
    Returnerar en tuple: (valida, ogiltiga, felorsaker)
    """
    valida = []
    ogiltiga = []
    felorsaker = []

    for _, row in df.iterrows():
        is_valid, reason = validate_row(row)
        if is_valid:
            valida.append(row.to_dict())
        else:
            ogiltiga.append(row.to_dict())
            felorsaker.append(reason)

    return valida, ogiltiga, felorsaker

# if __name__ == "__main__":
#     df = pd.read_csv("bank-project", "data", "sebank_customers_with_accounts.csv")
#     valida, ogiltiga, felorsaker = validate_data(df)

#     print(f"Antal giltiga: {len(valida)}")
#     print(f"Antal ogiltiga: {len(ogiltiga)}")
#     print("Exempel på felorsaker:")
#     for reason in felorsaker[:5]:
#         print(" -", reason)
