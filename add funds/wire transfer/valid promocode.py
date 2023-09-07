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
send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
send_button.click()
wait = WebDriverWait(driver, 30)

# Переход в раздел Add funds
element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div[2]/div[1]/div[1]/div[1]/a')))
element.click()

# Заполнение полей с платежкой
wire = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div')))
wire.click()
amount = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/div')))
amount.click()
pyautogui.typewrite('520')

# Заполнение промокода
promocode = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/div[3]/div[1]/div[2]/div/div[1]/div[1]')))
promocode.click()
pyautogui.typewrite('MOSTBET77')
strelka = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/div[3]/div[1]/div[2]/div/div[1]/div[2]')))
strelka.click()

# Вывод сообщения о валидных данных
time.sleep(3)
status_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/div/div/div[2]/div[3]/div[2]')))
status = status_element.text
if status == "Promo bonus: $ 77.00 (0%)":
    print("successfully")
else:
    print("failed")

sleep(50)