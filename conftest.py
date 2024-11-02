from selenium import webdriver
import pytest
import json


def get_json():
    file = open('user_info.json')
    user_info = json.load(file)
    return user_info


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
