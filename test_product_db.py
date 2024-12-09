import asyncio
from init_db import create_db_and_tables
from controlers.product_controler import ProductControler

async def init():
    await create_db_and_tables()

async def add_product():
    await ProductControler.add_product(
        pNo = 'p001',
        pName = 'Test Product 1',
        unitPrice = 500,
        stock = 1000, 
        spac ='This is product 1',
        detail = 'Product 1 detail'
    )  

    await ProductControler.add_product(
        pNo = 'p002',
        pName = 'Test Product 2',
        unitPrice = 700,
        stock = 1000, 
        spac ='This is product 2',
        detail = 'Product 2 detail'
    )  

async def update_product():
    await ProductControler.update_product(id=1, unitPrice = 800)     

async def delete_product():
    await ProductControler.delete_product(id=1)   

async def select_all():
    products = await ProductControler.select_all()
    for p in products:
        print('{} | {} | {} | {} | {} | {} | {}'.format(p.id, p.pNo, p.pName, p.unitPrice, p.stock, p.spac, p.detail)) 
    
async def select_product():
    p = await ProductControler.select_product(id=1)
    print('{} | {} | {} | {} | {} | {} | {}'.format(p.id, p.pNo, p.pName, p.unitPrice, p.stock, p.spac, p.detail))    


def main():
    asyncio.run(init())
    asyncio.run(add_product())
    #asyncio.run(update_product())
    #asyncio.run(delete_product())
    asyncio.run(select_all())
    print()
    asyncio.run(select_product())
 
if __name__ == "__main__":
     main()