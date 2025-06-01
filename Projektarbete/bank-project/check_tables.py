import sqlite3
import os

# Sökvägen till rätt databas
db_path = os.path.join("database", "database.db")

# Anslut till databasen
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Hämta alla tabeller
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tabeller i databasen:")
for table in tables:
    print("-", table[0])

conn.close()