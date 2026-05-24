from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from backend.app.core.config import DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_DATABASE, DATABASE_DRIVER

DATABASE_URL = URL.create(
    drivername=DATABASE_DRIVER,
    username=DATABASE_USER,
    password=DATABASE_PASSWORD,
    host=DATABASE_HOST,
    database=DATABASE_DATABASE,
)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)