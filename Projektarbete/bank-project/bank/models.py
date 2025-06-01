from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    adress = Column(String)
    phone = Column(String)
    personnummer = Column(String)
    bank_account = Column(String, unique=True)
    

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(String, primary_key=True)  # UUID
    timestamp = Column(DateTime)
    amount = Column(Float)
    currency = Column(String)
    sender_account = Column(String)
    receiver_account = Column(String)
    sender_country = Column(String)
    sender_municipality = Column(String)
    receiver_country = Column(String)
    receiver_municipality = Column(String)
    transaction_type = Column(String)
    notes = Column(String)