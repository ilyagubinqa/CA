from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
import pyautogui

# Открытие браузера и переход на страницу регистрации
driver_service = Service(executable_path="C:\Program Files\Webdriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.get('https://app.staging1.clickadilla.com/login')

# Ожидание появления полей и ввод данных для авторизации
wait = WebDriverWait(driver, 55)
login_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-email-field")))
login_input.send_keys('test_selenium04@gmail.com')
password_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-password-field")))
password_input.send_keys('test_selenium04@gmail.com')

# Отправка данных для авторизации и вход в личный кабинет
send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
send_button.click()
wait = WebDriverWait(driver, 30)

# Переход в раздел Add funds
element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div[2]/div[1]/div[1]/div[1]/a/span')))
element.click()

# Выбор perfect money
perfect_money = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[2]/div[2]/div[1]/div/div[7]/div/div/div[2]/div[2]')))
perfect_money.click()

# Установление суммы пополнения
amount = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/div')))
amount.click()
pyautogui.typewrite('53')

# Отправка запроса на пополнение
send_proceed = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div/div/div[3]/button/span/span')))
send_proceed.click()

# Вывод сообщения о создании платежки
time.sleep(3)
status_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table/tbody/tr/td/div/form/table[1]/tbody/tr/td[1]/h1/font')))
status = status_element.text
if status == "Perfect Money®":
    print("successfully")
else:
    print("Failed")

sleep(50)