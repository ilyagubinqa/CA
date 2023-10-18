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
    chrome_browser.implicitly_wait(13)
    return chrome_browser

def test_invalidemail(browser):
    # Открытие браузера и переход на страницу регистрации
    browser.get('https://app.staging1.clickadilla.com/login')

    # Ожидание появления полей и ввод данных для авторизации
    wait = WebDriverWait(browser, 55)
    login_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-email-field")))
    login_input.send_keys('ilyagubin1234567@gmail.comm')
    login_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-password-field")))
    login_input.send_keys('ilyagubin1234567@gmail.com')

    # Отправка данных для авторизации и вход в личный кабинет
    send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
    send_button.click()

    # Вывод сообщения об ошибке
    time.sleep(5)
    error_element = browser.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[1]/div/form/div[1]/div[2]/div/div[2]/div/div/div')
    error_message = error_element.text

    expected_error_message = "These credentials do not match our records."

    if error_message.strip() == expected_error_message.strip():
        print("Test passed successfully")
    else:
        print("Test failed")
    time.sleep(10)