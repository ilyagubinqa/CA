from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открытие браузера и переход на страницу авторизации
driver_service = Service(executable_path="C:\Program Files\Webdriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.get('https://staging-app.clickadilla.com/login')

# Ожидание появления полей и ввод данных для авторизации
wait = WebDriverWait(driver, 55)
login_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-email-field")))
login_input.send_keys('ilyagubin1234567@gmail.com')
login_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-password-field")))
login_input.send_keys('ilyagubin1234567@gmail.com')

# Переход в раздел campaigns
element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/campaigns']")))
element.click()

# Выбор кампании
campaign = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[1]/div[1]/div/div/div[2]/table/tbody/tr[2]/td[3]/div/a')))
campaign.click()
adjust = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="1435"]/div[4]/div/div[1]/div/div[2]/div/div[1]/div/table/tbody/tr[3]/td[2]/div/div/div[2]/button/span/span')))
adjust.click()

# Вывод сообщения о применении adjust price
status_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div/div[1]')))
status = status_element.text
if status == "Price successfully adjusted":
    print("Price successfully adjusted")
else:
    print("Price not adjusted")

sleep(70)
