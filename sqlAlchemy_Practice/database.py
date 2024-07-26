import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# step 1: create engine
# create_engine establishes a connection to the database
engine = create_engine(DATABASE_URL, echo=True)

# step 2: create our declarative base
# declarative_base function is used to create a base class for defining ORM models
Base = declarative_base()

# step 3: create your session
# Session is created to interact with the database. It manages transactions and keeps track of changes to objects.


Session = sessionmaker(bind=engine)

session = Session()
