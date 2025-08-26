from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./bank.db"

# Skapa en engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}) # Krävs för SQLite

# Skapa en session factory
SessionLocal = sessionmaker(autocommit=False, autoFlush=False, bind=engine)

# # Skapa tabeller (om du kör direkt utan Alembic, men Alembic använder inte detta)
# def init_db():
#     Base.metadata.create_all(bind=engine)
    
Base = declarative_base()