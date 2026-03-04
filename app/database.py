"""from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import Settings

DATABASE_URL = Settings.DATABASE_URL

# Special arg for SQLite to allow usage in multithreaded FastAPI
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, echo=False, future=True, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()

# FastAPI dependency to get a DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()"""