from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import get_json
import time

user_info = get_json()


class PersonsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=5)

    def check_title(self, title):
        page_title = self.driver.find_element(By.CSS_SELECTOR, 'h2')
        assert page_title.text == title

    def filter_phone(self):
        phone_button = self.driver.find_element(
            By.XPATH, '/html/body/app-root/app-template-module/app-personinfo-registry/div/div[2]/fck-registry-ui/fck-registry-v2/fck-registry-wrapper/div[1]/fck-registry-filter/div/div[2]/div/fck-field-button-overlay[3]/fck-field-render/fck-text-field-button/span/button')
        phone_button.click()
        time.sleep(2)

        # phone_input = self.driver.find_element(
        #     By. CSS_SELECTOR, '#mat-mdc-dialog-3 > div > div > fck-modal-bottom > div > div.modal_body > fck-field-wrapper > label > div > mask-field > input[type=tel]')
        # phone_input.click()
        # phone_input.send_keys(user_info["user_login"])

        # try:
        #     modal_phone = WebDriverWait(10).until(EC.visibility_of_element_located(
        #         By.XPATH, '//*[@id="mat-mdc-dialog-3"]/div/div/fck-modal-bottom/div/div[2]/fck-field-wrapper/label/div/mask-field/input'))
        #     modal_phone.click()
        #     modal_phone.send_keys(user_info["user_login"])
        #     apply_btn = self.driver.find_element(
        #         By.XPATH, '//*[@id="mat-mdc-dialog-3"]/div/div/fck-modal-bottom/div/div[3]/div/button[2]')
        #     apply_btn.click()
        # except:
        #     print("Модальное окно не найдено")

        time.sleep(5)
