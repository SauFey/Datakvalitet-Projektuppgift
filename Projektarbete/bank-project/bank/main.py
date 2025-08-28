from database import SessionLocal, engine
from bank import models

# Skapa tabeller om man kör direkt (utan Alembic)
models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

bank = models.Bank(name="TestBank")
customer = models.Customer(name="Anna Andersson", email="anna@example.com", bank=bank)
account = models.Account(account_number="1234567890", balance=1000.0, customer=customer, bank=bank)
transaction = models.Transaction(amount=250.0, account=account)

db.add(bank)
db.commit()
db.refresh(bank)

print("Bank och kund skapad!")
db.close()