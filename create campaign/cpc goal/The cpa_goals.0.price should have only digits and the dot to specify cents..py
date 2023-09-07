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

# Выбор гол модели
goal = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div')))
goal.click()

# Выбор страны
select_countries = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/div[1]/div[1]')))
select_countries.click()
countries = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='v-list-item__title' and text()='Afghanistan']")))
countries.click()
goal_countries = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div')))
goal_countries.click()
pyautogui.typewrite('-1')

# Выбор креатива
select_ad = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[7]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div[1]')))
select_ad.click()
time.sleep(2)
add = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div')))
add.click()

# Создание кампании
create = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/button/span')))
create.click()
continue_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,  '//*[@id="app"]/div[6]/div/div/div[3]/button/span/span')))
continue_button.click()

# Вывод сообщения об ошибке
time.sleep(2)
error_element = driver.find_element(By.CSS_SELECTOR, ".v-messages__message")
error_message = error_element.text
print(error_message)

sleep(30)


