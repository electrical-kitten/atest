from selenium.webdriver.common.by import By


class BurgerMenu:

    def __init__(self, driver):
        self.driver = driver

    def open_menu(self):
        menu_btn = self.driver.find_element(
            By.XPATH, '/html/body/app-root/app-template-module/header/div/div/button')
        menu_btn.click()

    def click_persons_registry(self):
        self.open_menu()
        persons_reg_icon = self.driver.find_element(
            By.XPATH, '/html/body/app-root/app-template-module/side-navigation/div[1]/div/div[1]/a/div[2]/div')
        persons_reg_icon.click()
