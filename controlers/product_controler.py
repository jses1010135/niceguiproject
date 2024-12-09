from model.product_model import Product
from init_db import get_async_session_context
from sqlalchemy.future import select
from typing import List

class ProductControler:

    @staticmethod
    async def add_product(pNo:str, pName: str, unitPrice: int,
                          stock: str, spac: str, detail: str) -> None:
        
        async with get_async_session_context() as session:        
            product = Product(
                pNo = pNo, pName = pName, unitPrice = unitPrice,
                stock = stock, spac = spac, detail = detail
            )
            session.add(product)
            await session.commit()
            
    @staticmethod
    async def update_product(id: int,
                             pNo: str = None, 
                             pName: str = None,
                             unitPrice: int = None,
                             stock: int = None,
                             spec: str = None,
                             detail: str= None) -> None:
        
        async with get_async_session_context() as session:
            product = await session.get(Product, id)
            if pNo is not None:
                product.pNo = pNo
            if pName is not None:
                product.pName = pName
            if unitPrice is not None:
                product.unitPrice = unitPrice                                                  
            if stock is not None:
                product.stock = stock
            if spec is not None:
                product.spac = spec
            if detail is not None:
                product.detail = detail                                                                  
                                         
            await session.commit()
            
            
    @staticmethod
    async def delete_product(id: int) -> None:
        
        async with get_async_session_context() as session:
            product = await session.get(Product, id)
            await session.delete(product)                                                                                           
            await session.commit()                  


    @staticmethod
    async def select_all() -> List[Product]:
        async with get_async_session_context() as session:
            result = await session.execute(select(Product))
            products = result.scalars().all()
            return products

    @staticmethod
    async def select_product(id: int = None, pNo: str = None, pName: str = None) -> Product:
        async with get_async_session_context() as session:
            result = await session.execute(
                select(Product).where(
                    (Product.id == id) |
                    (Product.pNo == pNo) |
                    (Product.pName == pName))
            )
            product = result.scalars().first()
            return product        