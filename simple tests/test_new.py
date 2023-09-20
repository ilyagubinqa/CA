from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.options import Options
import time
import pytest
from selenium.webdriver import Chrome



# Опции для запуска в режиме headless
options = Options()
options.add_argument('--headless')

@pytest.fixture()
def browser():
    url = "https://app.staging1.clickadilla.com/login"
    driver = webdriver.Chrome()
    driver.get(url)
def test_button1_exist(browser):
    browser.get('https://app.staging1.clickadilla.com/login')
    assert browser.find_element(By.CLASS_NAME, "v-btn__content").is_displayed()