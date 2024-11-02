from selenium.webdriver.common.by import By
from conftest import get_json
import time

user_info = get_json()


class PersonsPage:

    def __init__(self, driver):
        self.driver = driver

    def check_title(self, title):
        page_title = self.driver.find_element(By.CSS_SELECTOR, 'h2')
        assert page_title.text == title

    def filter_phone(self):
        phone_button = self.driver.find_element(
            By.XPATH, '/html/body/app-root/app-template-module/app-personinfo-registry/div/div[2]/fck-registry-ui/fck-registry-v2/fck-registry-wrapper/div[1]/fck-registry-filter/div/div[2]/div/fck-field-button-overlay[3]/fck-field-render/fck-text-field-button/span/button')
        phone_button.click()
        # phone_input = self.driver.find_element()
        # phone_input.send_keys(user_info['user_login'])
        time.sleep(5)
