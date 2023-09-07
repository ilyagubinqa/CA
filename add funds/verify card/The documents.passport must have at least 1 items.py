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
# Отправка данных для авторизации и вход в личный кабинет
send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
send_button.click()
wait = WebDriverWait(driver, 50)

# Переход в раздел Add funds
element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div[2]/div[1]/div[1]/div[1]/a/span')))
element.click()

# Выбор verify card
bitcoin = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[1]/a/span/span')))
bitcoin.click()

# Загрузка файла на 1 шаге
image = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//input[@type = 'file']")))
image.send_keys("C:\PycharmProjects\img\card.png")
time.sleep(10)

# Загрузка файла на 2 шаге
step2 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[3]/div/button[2]/span/span')))
step2.click()

# Загрузка файла на 3 шаге
step3 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[3]/div/button[2]/span/span')))
step3.click()

# Загрузка файла на 4 шаге
step4 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[3]/div/button[2]/span/span')))
step4.click()

# Отправка данных для авторизации и вход в личный кабинет
send_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[3]/div/button[2]/span')))
send_button.click()

# Вывод сообщения об ошибке
time.sleep(2)
error_element = driver.find_element(By.CSS_SELECTOR, ".v-messages__message")
error_message = error_element.text
print(error_message)
sleep(70)
