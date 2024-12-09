from sqlalchemy import Column, String, Integer
from init_db import Base


class Product(Base):
    __tablename__ = 'product'    

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pNo = Column(String, unique=True, index=True)
    pName = Column(String, unique=True, index=True)
    unitPrice = Column(Integer)
    stock = Column(Integer)
    spac = Column(String)
    detail = Column(String)