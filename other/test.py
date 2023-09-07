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

# Инициализация драйвера и переход на страницу с капчей
driver_service = Service(executable_path="C://chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.get('https://app.clickadilla.com/register')
# ожидание появления полей ввода
wait = WebDriverWait(driver, 55)
# Ожидание появления полей ввода
captcha_frame = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@title='reCAPTCHA']")))
# Функция решения капчи
solver = TwoCaptcha(API_KEY)

try:
    result = solver.recaptcha(
        sitekey='6LeVHLkUAAAAAC16N9EasV6cFfStTFaG9wF3tpOj',
        url='https://app.clickadilla.com/register')

except Exception as e:
    sys.exit(e)

else:
    print('solved: ' + str(result))


def solve_captcha(api_key, site_key, page_url, callback):
    # Вставка решения капчи
    captcha_checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "g-recaptcha-response")))
    driver.execute_script("arguments[0].style.display = 'block';", captcha_checkbox)
    time.sleep(3)
    token_captacha = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@title='reCAPTCHA']").get.attribute('sitekey')))
    response = requests.post('https://rucaptcha.com/in.php', data={

        'key': API_KEY,
        'method': 'userrecaptcha',
        'googlekey': SITE_KEY,
        'pageurl': PAGE_URL,
        'json': 1,
        'callback': callback
    })
    result = solver.recaptcha
    print(result)
    captcha_checkbox.send_keys(result)
sleep(90)

