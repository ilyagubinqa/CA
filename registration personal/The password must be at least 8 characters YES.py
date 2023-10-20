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
    chrome_browser.implicitly_wait(24)
    return chrome_browser

def test_registration(browser):
    # Открытие браузера и переход на страницу регистрации
    browser.get('https://app.staging1.clickadilla.com/register')

    # Ожидание появления полей ввода
    wait = WebDriverWait(driver, 15)
    name_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-name-field")))
    email_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-email-field")))
    password_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-password-field")))
    confirm_password_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-password-confirm-field")))
    nickname_code_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-nickname-0-field")))

    # Заполнение полей формы регистрации
    name_input.send_keys('test_selenium')
    email_input.send_keys('ilyagubin123456467@gmail.com')
    password_input.send_keys('clicka')
    confirm_password_input.send_keys('clicka')
    nickname_code_input.send_keys('skypeclickadilla')

    # Отправка данных по кнопке Sign up
    send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
    send_button.click()

    # Поиск ошибки
    details_element = browser.find_element(By.CLASS_NAME, "v-messages__message")

    # Текст элемента
    details_text = details_element.text

    # Проверка на то, что ошибка содержит текст
    error_message = "The password must be at least 8 characters."

    if error_message in details_text:
        print("Test passed successfully")
    else:
        print("Test failed")
    time.sleep(35)