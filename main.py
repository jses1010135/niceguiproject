from nicegui import ui
from user_account import UserAccount

@ui.page('/')
def home_page():
    ua = UserAccount()
    ua.display()

ui.run()
