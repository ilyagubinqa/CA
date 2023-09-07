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

# Ожидание появления полей ввода
wait = WebDriverWait(driver, 15)
name_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-name-field")))
email_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-email-field")))
password_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-password-field")))
confirm_password_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-password-confirm-field")))
nickname_code_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-register-nickname-0-field")))
captcha_frame = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@title='reCAPTCHA']")))


# Заполнение полей формы регистрации
name_input.send_keys('')
email_input.send_keys('')
password_input.send_keys('')
confirm_password_input.send_keys('')
nickname_code_input.send_keys('')
captcha_frame.send_keys('03ADUVZwC8rB_HJ3q0aJRZGi1IlNCn6wePXirAexfL0xoI2YX4eCOAtMKKrI-QTGwMYccOdPUtrWWm0T0538CdfIzO4JxIAgayiKsN5bGfeMMPafDTBbRTt9WvIPImsWib0XeT15gRwpMIWlzVwR4XrZKY51R6TjMNgixwvEbgpihWfsivZ4zi2vwAtjEbRq49P8p8pPQ3AyGK8YiTL5b3DXk3HLha_02wC27sgZwe712zf0Hp1Ge0UyfGJYw8tNKFYlKhNvuqw0pzUMS6NK2iqZGHvKHA5e7goI1-xzicMRIt7-EagsrBuUxLetTfT2ZipqqaXfu5J9oYwJrNad6Lcu--6jE_K89U7b50--2ftJGP6Qx2s8emrqNOqyTC8NeL-HtoaYnGrjQREejlvZAJ8fj60RpNoosIQNwCrCRpfakP2OKTzv7OeMveg1xLGNFC-cWvhcEBw9iK4r60KdQSd6C1UNJ2zxYpQNSxauVK2-kEd8kN-rBs1M1-jvmPZ3FGh2j1x7CVajSZq0UZJFtYUPaimzNIudEd2aC9__ohIQqxZf47L8ShBiSx6kfY0Gu5IXsQkKr8YRpglMF7qUxAAQDHs8gjx1eJIw')

# Отправка данных по кнопке Sign up
send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
send_button.click()

# Вывод сообщения об ошибке
time.sleep(1)
error_element = driver.find_element(By.CSS_SELECTOR, ".v-messages__message")
error_message = error_element.text
print(error_message)
sleep(5)