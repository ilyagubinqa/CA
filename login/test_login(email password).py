from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открытие браузера и переход на страницу регистрации
driver_service = Service(executable_path="C:\\Program Files\\Webdriver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://app.staging1.clickadilla.com/login')

# Ожидание появления полей и ввод данных для авторизации
wait = WebDriverWait(driver, 50)
login_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-email-field")))
login_input.send_keys('test_selenium04@gmail.com')
password_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-password-field")))
password_input.send_keys('test_selenium04@gmail.com')
send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
send_button.click()

# Отправка данных для авторизации и вход в личный кабинет
send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
send_button.click()

time.sleep(15)

# Проверяем, что произошел вход в личный кабинет
expected_url = 'https://app.staging1.clickadilla.com/dashboard'
print(expected_url)
current_url = driver.current_url

if current_url == expected_url:
    print("Вход в личный кабинет произошел")
else:
    print("Вход в личный кабинет не произошел")

sleep(15)



