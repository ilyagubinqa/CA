from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pytest

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    driver_service = Service(executable_path="C:\\Program Files\\Webdriver\\chromedriver-win64\\chromedriver.exe")
    chrome_browser = webdriver.Chrome(service=driver_service, options=options)
    chrome_browser.implicitly_wait(12)
    return chrome_browser

def test_button1_exist(browser):
    browser.get('https://app.staging1.clickadilla.com/login')
    assert browser.find_element(By.CLASS_NAME, "v-btn__content").is_displayed()
