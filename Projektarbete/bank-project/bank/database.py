from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bank.models import Base

# Skapa en engine
engine = create_engine("sqlite:///bank.db", echo=True)

# Skapa en session factory
SessionLocal = sessionmaker(bind=engine)

# Skapa tabeller (om du kör direkt utan Alembic, men Alembic använder inte detta)
def init_db():
    Base.metadata.create_all(bind=engine)