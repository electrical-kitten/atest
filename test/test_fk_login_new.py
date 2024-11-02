import time
from pages.login_page import LoginPage
from pages.inventories_page import InventoryPage


def test_login_fk(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.login_to_fk()
    time.sleep(2)
    inventory_page.check_title('Реестр ТМЦ')
