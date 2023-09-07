import time
from time import sleep

import pyautogui as pyautogui
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

driver_service = Service(executable_path="C:\Program Files\Webdriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.get('https://app.clickadilla.com/login')

# Ввод логина и пароля и вход в личный кабинет
wait = WebDriverWait(driver, 50)
login_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']")))
login_input.send_keys('iliya.gubin@onlinesup.com')
login_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
login_input.send_keys('CG7NvXT4XdKB5zf')
send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
send_button.click()
wait = WebDriverWait(driver, 50)

# Переход в раздел Add funds
element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div[2]/div[1]/div[1]/div[1]/a/span/span[2]')))
element.click()

# Заполнение полей с платежкой
wire = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div')))
wire.click()
amount = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/div')))
amount.click()
pyautogui.typewrite('52')

# Отправка запроса
send_proceed = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div/div/div[3]/button/span/span')))
send_proceed.click()

# Вывод сообщения о проверке реквизитов
time.sleep(5)
status_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page"]/div/div/div[2]/div[4]')))
status = status_element.text
expected_status = """
COMPANY DETAILS:
Company: AMBITIOUS GAIN LP
Address: 39/5 Granton Crescent, Edinburgh, United Kingdom, EH5 1BN
Company number: SL026648

To send USD or EUR via SWIFT:
Bank: IFX PAYMENTS
Address: 119 MARYLEBONE ROAD, LONDON, NW1 5PU, United Kingdom
Swift/BIC: IFXSGB2L
IBAN: GB86IFXS23229047610564
Intermediary Bank: BARCLAYS BANK PLC
Intermediary bank SWIFT: BARCUS33XXX

To send EUR via SEPA:
Bank: Bitsafe Payments
Address: Danzigerkade 23D, 1013 AP, Amsterdam, Netherlands
Swift/BIC: BITSNL2A
IBAN: NL02BITS0318680769
If you make payment in EUR received amount will be recalculated to USD according to the
ECB exchange rate on the day of receipt of the transfer.
https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exc
hange_rates/html/index.en.html

IMPORTANT:
We strongly recommend processing the payment according to
the guidelines below to avoid any issues:
- We do not accept payments from UK. All payments from UK will be refunded automatically
- The payment description must contain invoice number to identify your payment
- All the transferring fees must be paid from your side, otherwise all our side taxes will be withheld from the payment.
- Once the funds are sent, please, inform your manager or contact customer service to submit it.
- We may request proof of the payment from your bank to identify your payment
"""
if status.strip() == expected_status.strip():
    print("The company details are specified correctly")
else:
    print("The company details are specified incorrectly")

time.sleep(50)