from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String,nullable = False)
    email = Column(String, nullable = False,unique = True)
    password = Column(String, nullable = False)

class CompleteProfile(Base):
    __tablename__ = 'complete_profiles'
    id = Column(Integer,primary_key = True, index = True)
    user_id = Column(Integer,ForeignKey('users.id'))
    leetcode_username = Column(String, nullable = False)
    codeforces_username = Column(String,nullable=False)
    hackerrank_username = Column(String, nullable = False)
    github_username = Column(String,nullable =False)
    