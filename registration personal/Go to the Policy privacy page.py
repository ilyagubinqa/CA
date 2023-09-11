from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time

# Открытие браузера и переход на страницу регистрации
driver_service = Service(executable_path="C:\Program Files\Webdriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.get('https://app.staging1.clickadilla.com/register')

# Ожидание появления полей ввода
wait = WebDriverWait(driver, 20)
policy = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[3]/div[1]/span[2]/a')))
policy.click()


# Добавляем задержку в 25 секунд перед проверкой URL
time.sleep(3)

# Проверяем, что произошел переход на страницу Privacy Policy
expected_url = 'https://clickadilla.com/privacy-policy'
current_url = driver.current_url

if current_url == expected_url:
    print("Переход на страницу Privacy Policy произошел")
else:
    print("Переход на страницу Privacy Policy не произошел")

sleep(25)