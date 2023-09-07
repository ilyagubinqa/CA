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
driver.get('https://staging-app.clickadilla.com/password/reset?email=ilyagubin1234567%40gmail.com&token=7d392d1a6f72766b8ffd13d2615c1a801107a13758526567228b6f83c1ae0269')

# Ожидание появления полей и их заполнение
wait = WebDriverWait(driver, 30)
password = wait.until(EC.element_to_be_clickable((By.ID, 'selenium-test-reset-password-password-field')))
password.send_keys('ilyagubin1')
confirm_paasword = wait.until(EC.element_to_be_clickable((By.ID, 'selenium-test-reset-password-password-confirm-field')))
confirm_paasword.send_keys('ilyagubin1')

# Отправка запроса
reset_password = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[2]/form/button/span/span')))
reset_password.click()

# Вывод сообщения о смене пароля
time.sleep(3)
status_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "v-btn__content")))
status = status_element.text

if status == "Login":
    print("Пароль успешно восстановлен")
else:
    print("Пароль не восстановлен")

sleep(50)




