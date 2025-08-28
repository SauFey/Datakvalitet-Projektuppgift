from sqlalchemy import engine, inspect
import sqlite3
import os

## Denna fil checkar bara av och visar vilka tabeller som finns i den angivna databasen

# Sökvägen till rätt databas
db_path = "db/database.db"

# Anslut till databasen
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Hämta alla tabeller
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Dessa tabeller finns i databasen:")
for table_name in tables:
    table = table_name[0]
    print(f"Tabell: {table}")
    
    cursor.execute(f"PRAGMA table_info({table});")
    columns = cursor.fetchall()
    for col in columns:
        print(f"   -{col[1]} ({col[2]})")
        
    print()

conn.close