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

def test_login(browser):
    # Открытие браузера и переход на страницу регистрации
    browser.get('https://app.staging1.clickadilla.com/login')

    # Ожидание появления полей и ввод данных для авторизации
    wait = WebDriverWait(browser, 55)
    login_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-email-field")))
    login_input.send_keys('ilyagubin1234567@gmail.com')
    password_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-password-field")))
    password_input.send_keys('ilyagubin1234567@gmail.com')
    send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
    send_button.click()

    # Отправка данных для авторизации и вход в личный кабинет
    send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
    send_button.click()

    time.sleep(15)

    # Отображение поля для ввода кода с почты

    time.sleep(25)
    confirmation_code = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-541"]')))
    confirmation_code.click()
    wait = WebDriverWait(browser, 20)

    # Вход в личный кабинет
    send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
    send_button.click()

    time.sleep(15)

    # Проверяем, что произошел вход в личный кабинет
    expected_url = 'https://app.staging1.clickadilla.com/dashboard'
    print(expected_url)
    current_url = browser.current_url

    if current_url == expected_url:
        print("Вход в личный кабинет произошел")
    else:
        print("Вход в личный кабинет не произошел")

    time.sleep(30)