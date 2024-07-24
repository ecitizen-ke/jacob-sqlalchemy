import os 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

#step 1: create engine
engine = create_engine(DATABASE_URL, echo=True)

#step 2: create our declarative base
Base = declarative_base()

#step 3: create your session
Session = sessionmaker(bind=engine)

session=Session()