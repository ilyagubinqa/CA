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
    name_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-name-field")))
    email_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-email-field")))
    password_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-password-field")))
    confirm_password_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-password-confirm-field")))
    phone_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-phone-field")))
    nickname_code_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-nickname-0-field")))

    # Заполнение полей формы регистрации
    name_input.send_keys('test_selenium')
    email_input.send_keys('test_selenium01@gmail.com')
    password_input.send_keys('test_selenium')
    confirm_password_input.send_keys('test_selenium')
    phone_input.send_keys('test_selenium')
    nickname_code_input.send_keys('test_selenium')

    # Капча
    time.sleep(25)

    # Отправка данных по кнопке Sign up
    send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
    send_button.click()

    # Добавляем задержкку перед проверкой URL
    time.sleep(10)

    expected_url = 'https://app.staging1.clickadilla.com/registration-succeeded'
    current_url = browser.current_url

    if current_url == expected_url:
        print("Пользователь успешно зарегистрирован")
    else:
        print("Пользователь не зарегистрирован")

    time.sleep(60)