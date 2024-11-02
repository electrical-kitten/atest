from selenium.webdriver.common.by import By
from conftest import get_json
import json


# with open('./pages/user_info.json') as file:
#     user_info = json.load(file)

user_info = get_json()


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # def open(self):
    #     self.driver.get('https://multishik.cynteka.ru')

# Один большой единый метод, собравший методы open и click_login вместе.
# Что бы сократить количество кода ибо в начало каждого теста требует логина
    def login_to_fk(self):
        self.driver.get('https://multishik.cynteka.ru')
        login_input = self.driver.find_element(
            By.XPATH, '/html/body/app-root/app-template-module/app-login/div/div[1]/form/div[1]/control/app-control-input-phone/app-control-input/input')
        pass_input = self.driver.find_element(
            By.XPATH, '/html/body/app-root/app-template-module/app-login/div/div[1]/form/div[2]/control/app-control-input-password/app-control-input/input')
        login_button = self.driver.find_element(
            By.XPATH, '/html/body/app-root/app-template-module/app-login/div/div[1]/form/button')

        login_input.send_keys(user_info['user_login'])
        pass_input.send_keys(user_info['user_password'])
        login_button.click()

    # def click_login_btn(self):
    #     login_button = self.driver.find_element(
    #         By.XPATH, '/html/body/app-root/app-template-module/app-login/div/div[1]/   form/button')
    #     login_button.click()
