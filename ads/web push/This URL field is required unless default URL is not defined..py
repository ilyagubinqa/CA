import time
from time import sleep
from tokenize import String

import pyautogui as pyautogui
import pywinauto
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.common.keys import Keys

API_KEY = 'c08a94ac3b58ce18f575e00cfe44d27f'
SITE_KEY = '6LeVHLkUAAAAAC16N9EasV6cFfStTFaG9wF3tpOj'

# Открытие браузера и переход на страницу авторизации
driver_service = Service(executable_path="C://chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.get('https://staging-app.clickadilla.com/login')
wait = WebDriverWait(driver, 30)

# Ввод логина и пароля и вход в личный кабинет
login_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']")))
login_input.send_keys('ilyagubin1234567@gmail.com')
login_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
login_input.send_keys('ilyagubin1234567@gmail.com')
send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
send_button.click()
wait = WebDriverWait(driver, 30)

# Переход в раздел Ads
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/ads']")))
element.click()

# Выбор Web push
create_webpush = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[2]/div[1]/div/div[2]/div/div[5]')))
create_webpush.click()
create_ads = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[1]/a/span/span')))
create_ads.click()

# Заполнение полей для создания креатива
title = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[4]/div/div/div/div/div[1]/div[3]/div[2]/div/div[1]/div')))
title.click()
pyautogui.typewrite('tc-advertising3-client')
body = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[4]/div/div/div/div/div[1]/div[5]/div[2]/div/div[1]/div')))
body.click()
pyautogui.typewrite('test')
time.sleep(3)

# Загрузка файла для креатива
image = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@type = 'file']")))
image.send_keys("C:\PycharmProjects\img\jpeg2.jpg")
done = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'doka--button-action-confirm') and span[text()='Done']]")))
done.click()
time.sleep(15)

# Отправка запроса на создание Web push
send_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="text-subtitle-2 px-8 text-capitalize v-btn v-btn--is-elevated v-btn--has-bg theme--light v-size--large primary"]//span[contains(text(),"Save")]')))
send_button.click()

# Вывод сообщения о создании креатива
time.sleep(1)
status_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[4]/span/span/span')))
status = status_element.text

if status == "Creating":
    print("Successfully saved")
else:
    print("Failed to save")

sleep(30)
