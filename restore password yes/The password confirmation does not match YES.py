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
    options.add_argument('--headless')
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(25)
    return chrome_browser

def test_registration(browser):
    # Открытие браузера и переход на страницу авторизации
    browser.get('https://app.staging1.clickadilla.com/password/reset?email=ilyagubin1234567%40gmail.com&token=7d392d1a6f72766b8ffd13d2615c1a801107a13758526567228b6f83c1ae0269')

    # Ожидание появления полей и их заполнение
    wait = WebDriverWait(browser, 30)
    password = wait.until(EC.element_to_be_clickable((By.ID, 'selenium-test-reset-password-password-field')))
    password.send_keys('test@test.ru')
    confirm_paasword = wait.until(EC.element_to_be_clickable((By.ID, 'selenium-test-reset-password-password-confirm-field')))
    confirm_paasword.send_keys('test')

    # Отправка запроса
    reset_password = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[2]/form/button/span/span')))
    reset_password.click()

    # Поиск ошибки
    details_element = browser.find_element(By.CLASS_NAME, "v-messages__message")

    # Текст элемента
    details_text = details_element.text

    # Проверка на то, что ошибка содержит текст
    error_message = "The password confirmation does not match."

    if error_message in details_text:
        print("Test passed successfully")
    else:
        print("Test failed")
    time.sleep(35)





