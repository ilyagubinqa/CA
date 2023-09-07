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

# Переход в раздел Create campaign
wait = WebDriverWait(driver, 60)
element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div[4]/a/span/span[2]')))
element.click()

# Выбор in stream
instream = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div[2]/div[2]/div/div[7]/button/span')))
instream.click()

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

# Заполнение campaign name
campaign_name = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div[4]/div[1]/div/div[2]/div/div/div')))
campaign_name.click()
pyautogui.typewrite('test_company')

# Заполнение campaign group
campaign_name = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div[4]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]')))
campaign_name.click()
time.sleep(1)
group = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='v-list-item__title' and text()='pamagiti']")))
group.click()

# Выбор креатива
time.sleep(10)
select_ad = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[5]/div[2]/div/div[1]/div/div[2]/div/div/div[1]')))
select_ad.click()
time.sleep(3)
add = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="list-item-1562-2"]/div')))
add.click()

# Заполнение Traffic quality
qaulity = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[6]/div[2]/div/div[1]/div[1]/div[2]/button[1]/span')))
qaulity.click()

# Выбор categories
categories = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[8]/div[2]/div/div/div/div[1]/div/div[1]/div/div/div')))
categories.click()

# Выбор hourly limits
hourhy_limits = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div[1]/div[1]/div/div/div[12]/div[2]/div[1]/div/div[2]/div/div/div')))
hourhy_limits.click()
pyautogui.typewrite('10')

# Выбор daily limits
daily_limits = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div[1]/div[1]/div/div/div[12]/div[2]/div[2]/div/div[2]/div/div/div')))
daily_limits.click()
pyautogui.typewrite('11')

# Выбор total limits
total_limits = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div[1]/div[1]/div/div/div[12]/div[2]/div[3]/div/div[2]/div/div/div')))
total_limits.click()
pyautogui.typewrite('12')

# Выбор импрессий
impressions = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div[1]/div[1]/div/div/div[12]/div[2]/div[3]/div/div[2]/div/div/div')))
impressions.click()
pyautogui.typewrite('17')

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