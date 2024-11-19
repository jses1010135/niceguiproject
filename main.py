from nicegui import ui, app
from user_account_view import UserAccountView
from init_db import engine, create_db_and_tables

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
    ua = UserAccountView()
    await ua.display()

init_app()
ui.run()
