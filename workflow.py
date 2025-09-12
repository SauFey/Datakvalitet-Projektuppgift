from prefect import flow, task
import subprocess
import os
import shutil

### ETL ###
@task
def run_etl():
    print("Kör ETL-pipeline..")
    subprocess.run(["python", "etl-pipeline.py"], check=True)

### Alembic migration ###
@task
def run_migrations():
    print("Kör Alembic migration..")
    subprocess.run(["python", "-m", "alembic", "upgrade", "head"], check=True)

### Tester ###
@task
def run_tests():
    print("Kör tester..")
    subprocess.run(["python", "-m", "pytest", "-v"], check=True)

### 4. Exportera ren data (valfritt) ###
@task
def export_data():
    print("Exporterar data..")
    os.makedirs("data/export", exist_ok=True)  # Skapa mappen om den inte finns
    src = "data/clean/transactions_clean.csv"
    dst = "data/export/transactions_clean.csv"
    shutil.copy(src,dst)

### Workflow ###
@flow
def bank_workflow():
    run_etl()
    run_migrations()
    run_tests()
    export_data()

if __name__ == "__main__":
    bank_workflow()
