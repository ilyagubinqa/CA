from time import sleep
import requests
import response as response
from _cffi_backend import callback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

API_KEY = 'c08a94ac3b58ce18f575e00cfe44d27f'
SITE_KEY = '6LeVHLkUAAAAAC16N9EasV6cFfStTFaG9wF3tpOj'
PAGE_URL = 'https://app.clickadilla.com/register'


def solve_captcha(api_key, site_key, page_url, callback):
    # Отправить запрос на создание задания на решение капчи
    response = requests.post('https://rucaptcha.com/in.php', data={
        'key': api_key,
        'method': 'userrecaptcha',
        'googlekey': site_key,
        'pageurl': page_url,
        'json': 1,
        'callback': callback
    })

    # Получить ID задания на решение капчи из ответа API
    captcha_id = response.json()['request']
    # Ожидать, пока решение капчи не будет готово
    while True:
        response = requests.get(f'https://rucaptcha.com/res.php?key={api_key}&action=get&id={captcha_id}&json=1')
        response_json = response.json()

        if response_json['status'] == 1:
            # Решение капчи готово, возвратить правильный ответ
            return response_json['request']
        elif response_json['status'] == 0:
            # Решение капчи еще не готово, ожидать
            sleep(45)
        else:
            # Произошла ошибка при решении капчи, вызвать исключение
            raise Exception(response_json['request'])


        # Обработка ответа от API с помощью колбэк-функции
        def callback(response):
            driver.execute_script("document.getElementById('g-recaptcha-response').value = '{}'".format(response))

# Получить правильный ответ на капчу с помощью функции solve_captcha
captcha_response = solve_captcha(API_KEY, SITE_KEY, PAGE_URL, callback)

# инициализация драйвера и переход на страницу с капчей
driver_service = Service(executable_path="C://chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.get('https://app.clickadilla.com/register')

# ожидание появления полей ввода
wait = WebDriverWait(driver, 55)
name_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='input-49']")))
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='input-51']")))
password_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='input-55']")))
confirm_password_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='input-58']")))
referral_code_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='input-69']")))
nickname_code_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='input-78']")))
captcha_frame = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@title='reCAPTCHA']")))

# переключение на iframe
driver.switch_to.frame(captcha_frame)

# вставка решения капчи
captcha_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-checked='false']")))
captcha_checkbox.click()
driver.execute_script("arguments[0].setAttribute('value', '{}');".format(captcha_response), captcha_checkbox)

captcha_frame = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='rc-anchor-content']")))
captcha_check_box_frame = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-checked='false']")))
wait = WebDriverWait(driver, 55)
captcha_check_box_frame.click()

# возврат на главный frame
driver.switch_to.default_content()

# заполнение полей формы регистрации
name_input.send_keys('test_selenium')
email_input.send_keys('selenium1005test@mail.com')
password_input.send_keys('clickadilla12345')
confirm_password_input.send_keys('clickadilla12345')
referral_code_input.send_keys('clickadilla12345')
nickname_code_input.send_keys('skypeclickadilla')

send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
send_button.click()
sleep(45)
solver = TwoCaptcha(API_KEY)

try:
    result = solver.recaptcha(
        sitekey='6LeVHLkUAAAAAC16N9EasV6cFfStTFaG9wF3tpOj',
        url='https://app.clickadilla.com/register')

except Exception as e:
    sys.exit(e)

else:
    print('solved: ' + str(result))
captcha_check_box_frame = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-checked='false']")))
captcha_check_box_frame.click()
# Извлечение значения решения капчи из ответа
captcha_response = result['code']
# Установка значения решения капчи в поле ввода
captcha_checkbox.send_keys(captcha_response)
sleep(120)
