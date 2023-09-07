import time
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha
import sys
import os
solver = TwoCaptcha('c08a94ac3b58ce18f575e00cfe44d27f')
API_KEY = 'c08a94ac3b58ce18f575e00cfe44d27f'
SITE_KEY = '6LeVHLkUAAAAAC16N9EasV6cFfStTFaG9wF3tpOj'
PAGE_URL = 'https://app.clickadilla.com/register'

api_key = os.getenv('6LeVHLkUAAAAAC16N9EasV6cFfStTFaG9wF3tpOj', 'c08a94ac3b58ce18f575e00cfe44d27f')
# Инициализация драйвера и переход на страницу с капчей
driver_service = Service(executable_path="C:\Program Files\Webdriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.get('https://app.clickadilla.com/register')

# ожидание появления полей ввода
wait = WebDriverWait(driver, 55)
captcha_frame = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@title='reCAPTCHA']")))
captcha_checkbox = driver.find_element(By.ID, "g-recaptcha-response")
driver.execute_script("arguments[0].style.display = 'block';", captcha_checkbox)
solver = TwoCaptcha(API_KEY)

try:
    result = solver.recaptcha(
        sitekey='6LeVHLkUAAAAAC16N9EasV6cFfStTFaG9wF3tpOj',
        url='https://app.clickadilla.com/register')

except Exception as e:
    sys.exit(e)

else:
    print('solved: ' + str(result))

# Извлечение значения решения капчи из ответа
captcha_response = result['code']

# Установка значения решения капчи в поле ввода
captcha_checkbox.send_keys(captcha_response)
sleep(90)
