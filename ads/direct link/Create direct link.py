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

# Переход в раздел Ads
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/ads']")))
element.click()

# Выбор direct link
create_direct = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div[8]')))
create_direct.click()
create_ads = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div/div[2]/div/div[1]/a/span/span")))
create_ads.click()
time.sleep(3)

# Заполнение полей для создания креатива
title = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div')))
title.click()
pyautogui.typewrite('test')
url = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div[1]/div')))
url.click()
pyautogui.typewrite('https://app.clickadilla.com')

# Отправка запроса на создание direct link
send_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="text-subtitle-2 px-8 text-capitalize v-btn v-btn--is-elevated v-btn--has-bg theme--light v-size--large primary"]//span[contains(text(),"Save")]')))
send_button.click()

# Вывод сообщения о создании креатива
time.sleep(3)
status_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/div/div/div[3]/div/div/div[1]/button/span')))
status = status_element.text

if status == "Start Another Campaign":
    print("Your Ad Campaign created successfully")
else:
    print("Failed to created Ad Campaign")

sleep(50)