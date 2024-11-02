import time
from pages.login_page import LoginPage
from pages.inventories_page import InventoryPage


def test_login_fk(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_to_fk()
    login_page.click_login_btn()
    inventory_page = InventoryPage(driver)
    time.sleep(3)
    inventory_page.check_title('Реестр ТМЦ')
