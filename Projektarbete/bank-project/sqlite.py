import sqlite3

db_path = "Projektarbete/bank-project/database/database.db"

conn = sqlite3.connect("database/database.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table = cursor.fetchall()

print("Tabeller i databasen:\n")
for table_name in table:
    table = table_name[0]
    print(f"Tabell: {table}")
    
    cursor.execute(f"PRAGMA table_info({table});")
    columns = cursor.fetchall()
    for col in columns:
        print(f"   -{col[1]} ({col[2]})")
        
    print()
    
conn.close