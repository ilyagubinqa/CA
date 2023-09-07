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

wait = WebDriverWait(driver, 15)

# Ввод логина и пароля и вход в личный кабинет
login_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']")))
login_input.send_keys('test_selenium04@gmail.com')
password_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
password_input.send_keys('test_selenium04@gmail.com')
send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
send_button.click()

#Капча
time.sleep(25)

# Выбор локали
wait = WebDriverWait(driver, 5)
language = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'input-240')))
language.click()
de = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'list-item-353-3')))
de.click()

# Проверка локали
time.sleep(3)
status_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[2]/div[2]/div[1]/div[1]')))
status = status_element.text
if status == "Kampagnen":
    print("Немецкая локаль сайта")
else:
    print("Failed")
sleep(50)