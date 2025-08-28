from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///C:/Users/stenm/Desktop/Data Manager/Datakvalitet/Projektarbete/bank-project/db/database.db"
# DATABASE_URL = "sqlite:///database.db"

engine = create_engine("sqlite:///C:/Users/stenm/Desktop/Data Manager/Datakvalitet/Projektarbete/bank-project/db/database.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
