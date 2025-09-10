from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from bank.models import Account, Transaction
from datetime import datetime


def transfer_funds(session: Session, sender_id: int, receiver_id: int, amount: float, notes: str = ""):
    """Utför en överföring mellan två konton med rollback vid fel."""
    try:
        # 1. Hämta konton
        sender = session.query(Account).filter_by(id=sender_id).one()
        receiver = session.query(Account).filter_by(id=receiver_id).one()

        # 2. Kontrollera att avsändaren har täckning
        if sender.balance < amount:
            raise ValueError("Avsändaren har inte tillräckligt med saldo!")

        # 3. Uppdatera saldon
        sender.balance -= amount
        receiver.balance += amount

        # 4. Logga transaktionen
        tx = Transaction(
            date=datetime.now(),
            amount=amount,
            sender_account=sender.account_number,
            receiver_account=receiver.account_number,
            transaction_type="transfer",
            notes=notes
        )
        session.add(tx)

        # 5. Spara
        session.commit()
        print(f"✅ Överfört {amount} från {sender.account_number} till {receiver.account_number}")

    except Exception as e:
        # Rulla tillbaka om något går fel
        session.rollback()
        print(f"❌ Transaktionen misslyckades: {e}")
        raise
