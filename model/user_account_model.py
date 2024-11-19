from sqlalchemy import Column, String, Integer #資料庫欄位型態 #model基本操作：新增、刪除、修改、查詢
from init_db import Base

class UserAccount(Base):
    __tablename__ = 'user_account'    

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)#primary_key=True:主鍵 #index=True:索引 #autoincrement=True:自動增加
    account = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    address = Column(String)