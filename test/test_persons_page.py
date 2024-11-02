from pages.login_page import LoginPage
from pages.burger_menu import BurgerMenu
from pages.persons_page import PersonsPage
import time


def test_person_page(driver):
    login_page = LoginPage(driver)
    burger_menu = BurgerMenu(driver)
    persons_page = PersonsPage(driver)
    login_page.open()
    login_page.login_to_fk()
    login_page.click_login_btn()
    # time.sleep(3)
    burger_menu.open_menu()
    time.sleep(2)
    burger_menu.click_persons_registry()
    time.sleep(2)
    persons_page.check_title('Пользователи')
