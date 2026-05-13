from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os 

load_dotenv()
Database_URL = os.getenv("Database_URL")

engine = create_engine(
    Database_URL,
    pool_pre_ping = True
)
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine 
)
base = declarative_base()