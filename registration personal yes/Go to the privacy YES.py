from selenium import webdriver
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
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(25)
    return chrome_browser

def test_registration(browser):
    # Открытие браузера и переход на страницу регистрации
    browser.get('https://app.staging1.clickadilla.com/register')


    # Ожидание появления полей ввода
    wait = WebDriverWait(browser, 15)
    terms = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[3]/div[1]/span[1]/a')))
    terms.click()

    # Добавляем задержку перед проверкой URL
    time.sleep(15)

    expected_url = 'https://staging-app.clickadilla.com/privacy-policy'
    current_url = browser.current_url

    if current_url == expected_url:
        print("Переход на страницу Privcacy policy произошел")
    else:
        print("Переход на страницу Privacy policy не произошел")

    time.sleep(10)