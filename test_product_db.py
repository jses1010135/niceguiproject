import asyncio
from init_db import create_db_and_tables
from controlers.product_controler import Product_Controler

async def init():
    await create_db_and_tables()

async def add_product():
    await Product_Controler.add_product(
        pNo = 'p002',
        pName = 'testProduct2',
        unitPrice = 500,
        stock = 1000, 
        spac ='this is product 2',
        detail = 'product2 detail'
    )  

def main():
    asyncio.run(init())
    asyncio.run(add_product())
 
if __name__ == "__main__":
     main()