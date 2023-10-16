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
    chrome_browser.implicitly_wait(12)
    return chrome_browser

def test_login(browser):
    # Открытие браузера и переход на страницу регистрации
    browser.get('https://app.staging1.clickadilla.com/login')

# Ожидание появления полей и ввод данных для авторизации
    wait = WebDriverWait(browser, 55)
    login_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-email-field")))
    login_input.send_keys('test_selenium04@gmail.com')
    login_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-password-field")))
    login_input.send_keys('test_selenium04@gmail.com')

    # Отправка данных для авторизации и вход в личный кабинет
    send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
    send_button.click()
    wait = WebDriverWait(browser, 40)

    # Отображение поля для ввода ключа
    google_code = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-78--0"]')))
    google_code.click()

    time.sleep(40)

    # Проверяем, что произошел вход в личный кабинет
    expected_url = 'https://staging-app.clickadilla.com/dashboard'
    print(expected_url)
    current_url = browser.current_url
    
    if current_url == expected_url:
        print("Вход в личный кабинет произошел")
    else:
        print("Вход в личный кабинет не произошел")

    time.sleep(30)