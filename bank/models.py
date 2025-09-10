from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

# Basen-modellen
Base = declarative_base()

# Tabell för kunder
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=True)
    iban = Column(String, unique=True, nullable=True)

    # Relation till Account
    accounts = relationship("Account", back_populates="customer")

    def __repr__(self):
        return f"<Customer(name={self.name}, email={self.email})>"


# Tabell för konto
class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True, nullable=False)
    balance = Column(Float, nullable=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))

    # Relation till customer och transactions
    customer = relationship("Customer", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")

    def __repr__(self):
        return f"<Account(number={self.account_number}, balance={self.balance})>"


# Tabell för transaktioner
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=True)
    amount = Column(Float, nullable=False)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    sender_account = Column(String, nullable=True)      # <-- Lägg till
    receiver_account = Column(String, nullable=True)    # <-- Lägg till
    notes = Column(String, nullable=True)               # <-- Lägg till
    transaction_type = Column(String, nullable=True)    # <-- Lägg till

    # Relation till account
    account = relationship("Account", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction(date={self.date}, amount={self.amount})>"
