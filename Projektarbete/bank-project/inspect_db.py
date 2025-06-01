from sqlalchemy import create_engine, inspect

engine = create_engine("sqlite:///database/database.db")

inspector = inspect(engine)

tables = inspector.get_table_names()

print("Tabeller i databasen:")
for table in tables:
    print(f"- {table}")