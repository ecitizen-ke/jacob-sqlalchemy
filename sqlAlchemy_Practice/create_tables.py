from database import engine, Base
from models import User, Post

# Create the table in the database
Base.metadata.create_all(engine)
