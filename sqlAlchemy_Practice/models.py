# code for models.py
 
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
 
class User(Base):
    __tablename__ = 'users'
 
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100), unique=True)
    posts = relationship("Post", back_populates="author")

 #User class represents the users table 
class Post(Base):
    __tablename__ = 'posts'
 
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="posts")
 
    def __repr__(self):
        return f"<Post(title='{self.title}', content='{self.content}')>"
    
    