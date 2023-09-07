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

# Выбор in stream
instream = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div[2]/div[2]/div/div[7]/button/span')))
instream.click()

# Заполнение campaign name
campaign_name = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div[4]/div[1]/div/div[2]/div/div/div')))
campaign_name.click()
pyautogui.typewrite('test_company')

# Заполнение campaign group
campaign_name = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div[4]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]')))
campaign_name.click()
time.sleep(1)
group = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='v-list-item__title' and text()='pamagiti']")))
group.click()

# Выбор креатива
time.sleep(10)
select_ad = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[5]/div[2]/div/div[1]/div/div[2]/div/div/div[1]')))
select_ad.click()
time.sleep(3)
add = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="list-item-1562-2"]/div')))
add.click()

# Заполненеие поля с ценой
amount = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div')))
amount.click()
pyautogui.typewrite('10')

# Заполнение поля operating system
time.sleep(7)
browser= WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[11]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]')))
browser.click()
chrome = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='v-list-item__title' and text()='Chrome']")))
chrome.click()
version = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-735"]')))
version.click()
pyautogui.typewrite('1,5')

# Запрос на создание кампании
create = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[5]/div[3]/button/span')))
create.click()

# Отправка формы для создания кампании
create = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/button/span/span')))
create.click()

# Вывод сообщения об ошибке
time.sleep(2)
error_element = driver.find_element(By.CSS_SELECTOR, ".v-messages__message")
error_message = error_element.text
print(error_message)

sleep(30)