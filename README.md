# Bank Project - ETL och Analys

Detta projekt innehåller ett ETL-flöde för att automatisera data-flöden:
- **Extract**: CSV-filer med kunder och transaktioner.
- **Transform**: Validering av data (IBAN, datum, belopp).
- **Load**: Rensad data laddas till SQLite-databas (`bank.db`).

## Struktur
- `etl_pipeline.py` - Skript för att köra ETL-flödet.
- `validation.ipynb` - Notebook med analys och grafer.
- `data/raw/` - Originalfiler.
- `data/clean/` - Rensade filer.
- `data/bad/` - Trasiga poster.

## Krav
Installera beroenden:
