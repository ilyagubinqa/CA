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

    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(25)
    return chrome_browser

def test_registration(browser):
    # Открытие браузера и переход на страницу регистрации
    browser.get('https://app.staging1.clickadilla.com/login')

    # Ожидание появления полей и ввод данных для авторизации
    wait = WebDriverWait(browser, 55)
    login_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-email-field")))
    login_input.send_keys('ilyagubin1234567@gmail.com')
    login_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-password-field")))
    login_input.send_keys('ilyagubin1234567@gmail.com')

    # Отправка данных для авторизации и вход в личный кабинет
    send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
    send_button.click()
    wait = WebDriverWait(browser, 40)

    # Переход в раздел персональных настроек
    icon = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div[2]/div[4]/div/button/span')))
    icon.click()
    name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="list-item-418"]')))
    name.click()
    change_password = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div[2]/div[1]/div/div[2]/div/div[1]/button/span/span')))
    change_password.click()
    window = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[5]/div/div/div[3]')))
    send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[5]/div/div/div[3]/button[1]/span/span')))
    send_button.click()

    # Вывод сообщения об отправке письма на почту
    time.sleep(1)
    status_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div/div[1]')))
    status = status_element.text
    if status == "We have e-mailed your password reset link!":
        print("Successfully")
    else:
        print("Failed")
    time.sleep(50)