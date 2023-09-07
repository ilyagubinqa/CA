from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера и переход на страницу логина
driver_service = Service(executable_path="C://chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.get('https://staging-app.clickadilla.com/login')

# Ожидание появления полей и ввод данных для авторизации
wait = WebDriverWait(driver, 55)
login_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-email-field")))
login_input.send_keys('ilyagubin1234567@gmail.com')
login_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-password-field")))
login_input.send_keys('ilyagubin1234567@gmail.com')

# Отправка данных для авторизации и вход в личный кабинет
send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
send_button.click()
wait = WebDriverWait(driver, 40)

# Отображение поля для ввода кода с почты
google_code = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-78--0"]')))
google_code.click()

time.sleep(40)

# Проверяем, что произошел вход в личный кабинет
expected_url = 'https://staging-app.clickadilla.com/dashboard'
print(expected_url)
current_url = driver.current_url

if current_url == expected_url:
    print("Вход в личный кабинет произошел")
else:
    print("Вход в личный кабинет не произошел")

sleep(30)