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

# Инициализация драйвера и переход на страницу логина
driver_service = Service(executable_path="C:\Program Files\Webdriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.get('https://staging-app.clickadilla.com/login')
wait = WebDriverWait(driver, 40)

# Ввод логина и пароля и вход в личный кабинет
login_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']")))
login_input.send_keys('ilyagubin1234567@gmail.com')
login_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
login_input.send_keys('ilyagubin1234567@gmail.com')
send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
send_button.click()

wait = WebDriverWait(driver, 40)

# Переход в раздел Add funds
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/nav/div[1]/div[1]/div[10]/span')))
element.click()

# Выбор ads formats
ads_formats = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/main/div/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[1]')))
ads_formats.click()
popunder = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div")))
popunder.click()

# Выбор operating system
system = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/main/div/div/div/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[1]')))
system.click()
windows = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[5]/div/div[2]/div[2]/div')))
windows.click()

# Выбор countries
countries = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/main/div/div/div/div[3]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/div[1]/div[1]')))
countries.click()
afganistan = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[6]/div/div[2]/div[2]/div')))
afganistan.click()

create_campaign = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/main/div/div/div/div[4]/div[3]/table/tbody/tr[5]/td[5]/button/span/span')))
create_campaign.click()

# Выбор креатива
time.sleep(10)
select_ad = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[5]/div[2]/div/div[1]/div/div[2]/div/div/div[1]')))
select_ad.click()
time.sleep(3)
add = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="list-item-1562-2"]/div')))
add.click()

# Заполнение поля с ценой
amount = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div')))
amount.click()
pyautogui.typewrite('10')

# Запрос на создание кампании
create = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[5]/div[3]/button/span')))
create.click()

# Вывод сообщения о создании кампании
time.sleep(3)
status_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[1]/div/text()')))
status = status_element.text

if status == "campaign has been":
    print("Your Campaign created successfully")
else:
    print("Failed to created Campaign")

sleep(70)