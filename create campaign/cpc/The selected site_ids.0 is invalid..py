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
send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
send_button.click()

# Переход в раздел Create campaign
wait = WebDriverWait(driver, 60)
element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div[4]/a/span/span[2]')))
element.click()

# Заполнение поля с ценой
amount = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div')))
amount.click()
pyautogui.typewrite('10')

# Выбор веб пуша
webpush = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div[2]/div[2]/div/div[5]/button/span/div')))
webpush.click()

# Выбор креатива
time.sleep(3)
select_ad = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[7]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div[1]')))
select_ad.click()
time.sleep(3)
add = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div')))
add.click()

# Заполненеие поля multiple search
multiple_search = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[8]/div/div[2]/div[3]/span[3]')))
multiple_search.click()
search_sites = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[8]/div/div[4]/div[1]/div/div[2]/div/div/div[1]')))
search_sites.click()
pyautogui.typewrite('10000000050')
search1 = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[8]/div/div[4]/div[1]/button')))
search1.click()
time.sleep(2)

# Запрос на создание кампании
create = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[5]/div[3]/button/span')))
create.click()

# Вывод сообщения об ошибке
time.sleep(2)
error_element = driver.find_element(By.CSS_SELECTOR, ".v-messages__message")
error_message = error_element.text
print(error_message)

sleep(30)
