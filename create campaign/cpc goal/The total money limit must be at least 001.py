from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pytest

@pytest.fixture()
def browser():
    options = Options()

    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(26)
    return chrome_browser

def test_web_push(browser):
    # Открытие браузера и переход на страницу регистрации
    browser.maximize_window()
    browser.get('https://staging-app.clickadilla.com/login')

    # Ожидание появления полей и ввод данных для авторизации
    wait = WebDriverWait(browser, 55)
    login_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-email-field")))
    login_input.send_keys('ilyagubin1234567@gmail.com')
    password_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-password-field")))
    password_input.send_keys('ilyagubin1234567@gmail.com')

    # Отправка данных для авторизации и вход в личный кабинет
    send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
    send_button.click()

    # Переход в раздел Create campaign
    wait = WebDriverWait(browser, 60)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div[4]/a/span/span[2]')))
    element.click()

    # Выбор веб пуша
    webpush = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, ("//*[contains(text(),'Web-push ')]"))))
    webpush.click()
    time.sleep(5)

    # Выбор гол модели
    goal = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div')))
    goal.click()
    time.sleep(2)

    # Выбор Conversion type
    select_conversion_type = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//span[text()=" View Content "]')))
    select_conversion_type.click()

    # Выбор страны
    select_countries = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/div[1]/div[1]')))
    select_countries.click()
    countries = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='v-list-item__title' and text()='Afghanistan']")))
    countries.click()
    goal_countries = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div')))
    ActionChains(browser).click(goal_countries).perform()
    ActionChains(browser).send_keys('4').perform()

    # Выбор креатива
    time.sleep(3)
    select_ad = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'selenium-test-campaign-form-ad-select')))
    select_ad.click()
    time.sleep(3)
    add = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='v-list-item__title' and text()='test web push 2  (1 url)']")))
    add.click()

    # Выбор total limits
    total_limits = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'selenium-test-campaign-form-total-limit-field')))
    ActionChains(browser).click(total_limits).perform()
    ActionChains(browser).send_keys('-1').perform()
    time.sleep(2)

    # Запрос на создание кампании
    create = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Create campaign"]')))
    create.click()
    continue_button = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Continue"]')))
    time.sleep(2)
    continue_button.click()

    # Поиск ошибки
    details_element = browser.find_element(By.CLASS_NAME, ("v-messages__message"))

    # Текст элемента
    details_text = details_element.text

    # Проверка на то, что ошибка содержит текст
    error_message = "The total money limit must be at least 0.01."

    if error_message in details_text:
        print("Test passed successfully")
    else:
        print("Test failed")
    time.sleep(30)