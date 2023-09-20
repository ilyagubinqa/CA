from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.options import Options
import time
import pytest

# Опции для запуска в режиме headless
options = Options()
options.add_argument('--headless')

@pytest.fixture()
def browser():
    driver_service = Service(executable_path="C:\\Program Files\\Webdriver\\chromedriver-win64\\chromedriver.exe")
    chrome_browser = webdriver.Chrome(service=driver_service)
    chrome_browser.implicitly_wait(10)
    return chrome_browser

def test_button1_exist(browser):
    browser.get('https://app.staging1.clickadilla.com/login')
    assert browser.find_element(By.CLASS_NAME, "v-btn__content").is_displayed()