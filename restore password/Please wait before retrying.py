import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time

# Инициализация драйвера и переход на страницу логина
driver_service = Service(executable_path="C:\Program Files\Webdriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.get('https://app.staging1.clickadilla.com/login')

wait = WebDriverWait(driver, 30)
restore_password = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[1]/div/div[2]')))
restore_password.click()
time.sleep(2)
login_input = wait.until(EC.element_to_be_clickable((By.ID,'selenium-test-login-forgot-password-field')))
login_input.click()
pyautogui.typewrite('ilyagubin1234567@gmail.com')
send = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[3]/div/div/div[3]/div[2]/button/span/span')))
send.click()
time.sleep(20)
close = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[3]/div/div/div[3]/button/span/span')))
close.click()
time.sleep(20)
restore_password = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[1]/div/div[2]')))
restore_password.click()
send = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[3]/div/div/div[3]/div[2]/button/span/span')))
send.click()
sleep(30)