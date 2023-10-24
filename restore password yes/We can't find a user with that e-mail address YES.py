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
    browser.get('https://app.staging1.clickadilla.com/login')

    # пользователь не найден
    wait = WebDriverWait(browser, 30)
    restore_password = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[1]/div/div[2]')))
    restore_password.click()
    time.sleep(2)
    login_input = wait.until(EC.element_to_be_clickable((By.ID, 'selenium-test-login-forgot-password-field')))
    login_input.click()
    pyautogui.typewrite('iliya.gubinn@onlinesup.com')

    # отправка запроса на восстановление пароля
    send = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[3]/div/div/div[3]/div[2]/button/span/span')))
    send.click()

    # Поиск ошибки
    details_element = browser.find_element(By.CLASS_NAME, "v-messages__message")

    # Текст элемента
    details_text = details_element.text

    # Проверка на то, что ошибка содержит текст
    error_message = "We can't find a user with that e-mail address."

    if error_message in details_text:
        print("Test passed successfully")
    else:
        print("Test failed")
    time.sleep(35)
