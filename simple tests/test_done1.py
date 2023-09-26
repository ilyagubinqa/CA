from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import pytest

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(12)
    return chrome_browser

def test_button1_exist(browser):
    browser.get('https://app.staging1.clickadilla.com/login')
    assert browser.find_element(By.CLASS_NAME, "v-btn__content").is_displayed()
