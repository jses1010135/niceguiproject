from nicegui import ui, app
from init_db import engine, create_db_and_tables
from controlers.product_controler import product_controler
def init_app():
    async def handle_startup():
        try:
            await create_db_and_tables()
        except:
            pass    

    async def handle_shutdown():
        await engine.dispose()

    app.on_startup(handle_startup)
    app.on_shutdown(handle_shutdown)


@ui.page('/')
async def home_page():
    await product_controler.add_product(
        id = 1,
        product_number = '001',
        product_name = 'apple',
        unitPrice = 100,
        stock = 10,
        spec = 'taiwan',
        detail = 'good'
    )

init_app()
ui.run()