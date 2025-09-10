import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sys
import os
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from bank.models import Base, Account
from bank.transactions import transfer_funds

@pytest.fixture(scope="function")
def db_session():
    """Skapar en temporär testdatabas i minnet."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Skapa två testkonton
    account1 = Account(account_number="111", balance=1000.0)
    account2 = Account(account_number="222", balance=500.0)
    session.add_all([account1, account2])
    session.commit()

    yield session

    session.close()
    engine.dispose()


def test_transfer_success(db_session):
    """Testar en lyckad överföring."""
    sender = db_session.query(Account).filter_by(account_number="111").one()
    receiver = db_session.query(Account).filter_by(account_number="222").one()

    transfer_funds(db_session, sender.id, receiver.id, 200.0)

    assert sender.balance == 800.0
    assert receiver.balance == 700.0


def test_transfer_insufficient_funds(db_session):
    """Testar att rollback fungerar om avsändaren inte har täckning."""
    sender = db_session.query(Account).filter_by(account_number="111").one()
    receiver = db_session.query(Account).filter_by(account_number="222").one()

    with pytest.raises(ValueError):
        transfer_funds(db_session, sender.id, receiver.id, 2000.0)

    # Kontrollera att saldon inte ändrats
    assert sender.balance == 1000.0
    assert receiver.balance == 500.0
