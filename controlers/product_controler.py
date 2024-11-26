from model.product_model import product #workflows 資料運算
from init_db import get_async_session_context
from sqlalchemy.future import select
from typing import List

class product_controler:

    @staticmethod
    async def add_product(id:int,product_number:str,product_name:str,unitPrice:int,stock:int,spec:str,detail:str) -> None:
        async with get_async_session_context() as session:
            product = product(
                id = id,
                product_number = product_number,
                product_name = product_name,
                unitPrice = unitPrice,
                stock = stock,
                spec = spec,
                detail = detail
            )
            session.add(product)
            await session.commit()
            return product
    