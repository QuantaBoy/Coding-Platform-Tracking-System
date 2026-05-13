# create engine creates Connection between python adn postgreSQL
from sqlalchemy import create_engine

# Sessionmaker creates database sessions 
# Sessions are temporary conversations with database 
from sqlalchemy.orm import sessionmaker 

# Import Decelrative Base 
# Used for Creating tables using Python Classes 

from sqlalchemy.ext.decelrative import declarative_base

# Import Dotenv Loader 
# Loads all the variables from .env file 
from dotenv import load_dotenv

# Import os Module 
# used for accessing environment variables 
import os 

#load .env file 
#without this : Database_URL cannot access variables
load_dotenv()

# Read Database_URL from .env 
Database_URL = os.getenv("Database_URL")

# Creating Database Engine
# Engine is the Main Bridge 
# FastAPI <--> I am Connecting the Database 

engine = create_engine(
    Database_URL,

    # Checks whether DB Connection is Alive 
    # Important for Cloud Databases
    pool_pre_ping=True
    )
# Create Session Factory 
# Session are used for :
# insert data 
# fetch data
# update data
# delete data

Sessionlocal = sessionmaker(
    # Preventing Autocommit Commits
    # we manually controlling commits
    autocommit = False,

    # Prevent Automatic Flushing 
    # Gives Better Control over Queries 
    autoflush = False,

    # Connecting the Sessions to Engine 
    bind = engine
)
# Base Class For all Database Models
Base = declarative_base()