from sqlalchemy import Column, String, Integer
from init_db import Base

class UserAccount(Base):
    __tablename__ = 'user_account'    

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    account = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    address = Column(String)