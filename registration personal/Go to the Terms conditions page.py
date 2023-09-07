from time import sleep
import requests
import response as response
from _cffi_backend import callback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC

# инициализация драйвера и переход на страницу с регистрацией
driver_service = Service(executable_path="C://chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.get('https://staging-app.clickadilla.com/register')

# Ожидание появления полей ввода
wait = WebDriverWait(driver, 15)
terms = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[3]/div[1]/span[1]/a')))
terms.click()

# Добавляем задержку в 25 секунд перед проверкой URL
time.sleep(3)

expected_url = 'https://staging-app.clickadilla.com/terms-conditions'
current_url = driver.current_url

if current_url == expected_url:
    print("Переход на страницу Terms conditions произошел")
else:
    print("Переход на страницу Terms conditions не произошел")

sleep(10)