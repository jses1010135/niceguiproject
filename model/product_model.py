from sqlalchemy import Column, String, Integer #資料庫欄位型態 #model基本操作：新增、刪除、修改、查詢
from init_db import Base

class product(Base):
    _tablename_ = 'product'

    id= Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_number = Column(String, unique=True, index=True)
    product_name = Column(String, unique=True, index=True)
    unitPrice = Column(Integer)
    stock = Column(Integer)
    spec = Column(String)
    detail = Column(String)