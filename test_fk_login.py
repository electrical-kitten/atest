from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import json

with open('user_info.json') as file:
    user_info = json.load(file)
    
@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    yield driver

def test_login_fk(driver):
    driver.get('https://multishik.cynteka.ru/#/login')
    time.sleep(3)

    login_input = driver.find_element(By.XPATH, '/html/body/app-root/app-template-module/app-login/div/div[1]/form/div[1]/control/app-control-input-phone/app-control-input/input')

    pass_input = driver.find_element(By.XPATH, '/html/body/app-root/app-template-module/app-login/div/div[1]/form/div[2]/control/app-control-input-password/app-control-input/input')

    login_button = driver.find_element(By.XPATH, '/html/body/app-root/app-template-module/app-login/div/div[1]/form/button')

    login_input.click()
    login_input.send_keys(user_info['user_login'])

    pass_input.click()
    pass_input.send_keys(user_info['user_password'])

    login_button.click()

    time.sleep(5)
    title = driver.find_element(By.CSS_SELECTOR, 'h2')
    
    assert title.text == 'Реестр ТМЦ'
    


