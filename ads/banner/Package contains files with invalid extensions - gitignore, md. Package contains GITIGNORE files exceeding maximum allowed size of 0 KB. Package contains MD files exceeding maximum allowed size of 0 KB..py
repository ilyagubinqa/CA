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
wait = WebDriverWait(driver, 30)

# Переход в раздел Ads
wait = WebDriverWait(driver, 30)
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/ads']")))
element.click()

# Выбор баннера
create_banner = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[2]/div[1]/div/div[2]/div/div[4]')))
create_banner.click()
create_ads = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/main/div/div/div/div[1]/a/span/span")))
create_ads.click()

# Заполнение полей для создания креатива
select_banner_size = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]')))
select_banner_size.click()
size = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='v-list-item__title' and text()='160x600']")))
size.click()
html5 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div/div[2]/div/div/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div[4]')))
html5.click()
time.sleep(3)

# Загрузка файла для креатива
image = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@type = 'file']")))
image.send_keys("C:\PycharmProjects\html\HTML-5-Banner-Template-master invalid.zip")
time.sleep(35)

# Отправка запроса на создание баннера
send_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="text-subtitle-2 px-8 text-capitalize v-btn v-btn--is-elevated v-btn--has-bg theme--light v-size--large primary"]//span[contains(text(),"Save")]')))
send_button.click()

# Вывод сообщения об ошибке
time.sleep(2)
error_element = driver.find_element(By.CSS_SELECTOR, ".v-messages__message")
error_message = error_element.text
print(error_message)
sleep(30)