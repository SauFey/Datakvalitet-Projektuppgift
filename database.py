from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bank.models import Base

DATABASE_URL = "sqlite:///./bank.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

# Skapar tabeller om de inte finns (första gången du kör)
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("✅ Databasen och tabellerna är skapade!")