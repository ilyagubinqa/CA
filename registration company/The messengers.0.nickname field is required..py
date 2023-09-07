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
driver.get('https://app.staging1.clickadilla.com/register')

# Переключение на company
wait = WebDriverWait(driver, 55)
company = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[2]/div/div/div/div[2]/div/div')))
company.click()

# Ожидание появления полей ввода
wait = WebDriverWait(driver, 55)
name_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-name-field")))
email_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-email-field")))
password_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-password-field")))
confirm_password_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-password-confirm-field")))
company_name = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-company-name-field")))
value_tax = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-value-added-tax-field")))
company_address = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-company-address-field")))
company_site = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-company-site-field")))
nickname_code_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-nickname-0-field")))

# Заполнение полей формы регистрации
name_input.send_keys('test_selenium')
email_input.send_keys('ilyagubin1234567543@gmail.com')
password_input.send_keys('clickadilla12345')
confirm_password_input.send_keys('clickadilla12345')
nickname_code_input.send_keys('')
company_name.send_keys('company test')
value_tax.send_keys('value tax test')
company_address.send_keys('company address test')
company_site.send_keys('company site  test')

# Отправка данных для регистрации
send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
send_button.click()

# Вывод сообщения об ошибке
time.sleep(3)
error_element = driver.find_element(By.CSS_SELECTOR, ".v-messages__message")
error_message = error_element.text
print(error_message)
sleep(10)