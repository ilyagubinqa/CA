from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pytest
import pyautogui

@pytest.fixture()
def browser():
    options = Options()

    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(25)
    return chrome_browser

def test_registration(browser):
    # Открытие браузера и переход на страницу авторизации
    browser.get('https://app.staging1.clickadilla.com/password/reset?email=ilyagubin1234567%40gmail.com&token=7d392d1a6f72766b8ffd13d2615c1a801107a13758526567228b6f83c1ae0269')

    # Ожидание появления полей и их заполнение
    wait = WebDriverWait(browser, 30)
    password = wait.until(EC.element_to_be_clickable((By.ID, 'selenium-test-reset-password-password-field')))
    password.send_keys('ilyagubin1')
    confirm_paasword = wait.until(EC.element_to_be_clickable((By.ID, 'selenium-test-reset-password-password-confirm-field')))
    confirm_paasword.send_keys('ilyagubin1')

    # Отправка запроса
    reset_password = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[2]/form/button/span/span')))
    reset_password.click()

    # Вывод сообщения о смене пароля
    time.sleep(3)
    status_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "v-btn__content")))
    status = status_element.text

    if status == "Login":
        print("Пароль успешно восстановлен")
    else:
        print("Пароль не восстановлен")

    time.sleep(50)




