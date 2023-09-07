from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time

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
wait = WebDriverWait(driver, 30)

#Капча
time.sleep(25)
# Ожидание появления полей ввода
wait = WebDriverWait(driver, 55)
article = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div[6]/div[2]/div/div[1]/a')))
article.click()

# Добавляем задержку в 25 секунд перед проверкой URL
time.sleep(3)

# Проверяем, что произошел переход на страницу статьи
expected_url = 'https://clickadilla.com/help/advertisers/3115644-video-guide-how-to-start-your-first-advertising-campaign'
current_url = driver.current_url

if current_url == expected_url:
    print("Переход на страницу статьи произошел")
else:
    print("Переход на страницу статьи не произошел")

sleep(10)