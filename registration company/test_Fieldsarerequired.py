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
    browser.get('https://app.staging1.clickadilla.com/register')

    # Переключение на company
    wait = WebDriverWait(browser, 55)
    company = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[2]/div/div/div/div[2]/div/div')))
    company.click()

    # Ожидание появления полей ввода
    wait = WebDriverWait(browser, 55)
    name_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-name-field")))
    email_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-email-field")))
    password_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-password-field")))
    confirm_password_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-password-confirm-field")))
    company_name = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-company-name-field")))
    value_tax = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-value-added-tax-field")))
    company_address = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-company-address-field")))
    company_site = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-company-site-field")))
    add_info = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-additional-info-field")))
    nickname_code_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-nickname-0-field")))
    phone_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-phone-field")))

    # Заполнение полей формы регистрации
    name_input.send_keys('')
    email_input.send_keys('')
    password_input.send_keys('')
    confirm_password_input.send_keys('')
    nickname_code_input.send_keys('')
    company_name.send_keys('')
    value_tax.send_keys('')
    company_address.send_keys('')
    company_site.send_keys('')
    add_info.send_keys('')
    phone_input.send_keys('')

    # Отправка данных для регистрации
    send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
    send_button.click()

    # Поиск ошибки
    details_element = browser.find_element(By.CLASS_NAME, "v-messages__message")

    # Текст элемента
    details_text = details_element.text

    # Проверка на то, что ошибка содержит текст
    error_message = "Fields are required"

    if error_message in details_text:
        print("Test passed successfully")
    else:
        print("Test failed")

    time.sleep(35)