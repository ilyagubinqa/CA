import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time

# Инициализация драйвера и переход на страницу логина
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pytest

@pytest.fixture()
def browser():
    options = Options()

    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(26)
    return chrome_browser

def test_web_push(browser):
    # Открытие браузера и переход на страницу регистрации
    browser.maximize_window()
    browser.get('https://staging-app.clickadilla.com/login')

    # Ожидание появления полей и ввод данных для авторизации
    wait = WebDriverWait(browser, 55)
    login_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-email-field")))
    login_input.send_keys('ilyagubin1234567@gmail.com')
    password_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-password-field")))
    password_input.send_keys('ilyagubin1234567@gmail.com')

    # Отправка данных для авторизации и вход в личный кабинет
    send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
    send_button.click()

    # Выбор локали
    wait = WebDriverWait(browser, 15)
    language = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, ("//*[contains(text(),'English')]"))))
    language.click()
    ru = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, ("//*[contains(text(),' Russian ')]"))))
    ru.click()

    # Проверка локали
    time.sleep(3)
    status_element = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, ("//*[contains(text(),'Кампании')]"))))
    status = status_element.text
    if status == "Кампании":
        print("Русская локаль сайта")
    else:
        print("Failed")
    time.sleep(15)
