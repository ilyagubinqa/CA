from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time

# Открытие браузера и переход на страницу регистрации
driver_service = Service(executable_path="C:\Program Files\Webdriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.get('https://app.staging1.clickadilla.com/register')

# Ожидание появления полей ввода
wait = WebDriverWait(driver, 15)
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

# Добавляем задержку в 25 секунд перед проверкой URL
time.sleep(10)

expected_url = 'https://app.staging1.clickadilla.com/registration-succeeded'
current_url = driver.current_url

if current_url == expected_url:
    print("Пользователь успешно зарегистрирован")
else:
    print("Пользователь не зарегистрирован")

sleep(20)