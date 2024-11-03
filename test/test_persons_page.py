from pages.login_page import LoginPage
from pages.burger_menu import BurgerMenu
from pages.persons_page import PersonsPage
import time


def test_person_page(driver):
    login_page = LoginPage(driver)
    burger_menu = BurgerMenu(driver)
    persons_page = PersonsPage(driver)
    login_page.login_to_fk()
    burger_menu.open_menu()
    time.sleep(2)
    burger_menu.click_persons_registry()
    time.sleep(2)
    # persons_page.wait()
    persons_page.filter_phone()
    persons_page.check_title('Пользователи')
