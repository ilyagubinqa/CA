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

    # Выбор попандера
    webpush = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, ("//*[contains(text(),' Popunder ')]"))))
    webpush.click()
    time.sleep(5)

    # Выбор гол модели
    goal = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, ("//*[contains(text(),' cpm goal ')]"))))
    goal.click()
    time.sleep(2)

    # Выбор Conversion type
    select_conversion_type = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//span[text()=" View Content "]')))
    select_conversion_type.click()

    # Выбор страны
    select_countries = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, 'selenium-test-campaign-form-goal-countries-select-0')))
    select_countries.click()
    countries = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='v-list-item__title' and text()='Afghanistan']")))
    countries.click()
    goal_countries = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, 'selenium-test-campaign-form-goal-value-field-0')))
    ActionChains(browser).click(goal_countries).perform()
    ActionChains(browser).send_keys('10').perform()

    # Выбор креатива
    time.sleep(3)
    select_ad = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'selenium-test-campaign-form-ad-select')))
    select_ad.click()
    time.sleep(3)
    add = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='v-list-item__title' and contains(text(), 'ID 1017 \"test test 1\"')]")))
    add.click()

    # Заполнение поля browser
    time.sleep(7)
    browser = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'selenium-test-campaign-form-browsers-select')))
    browser.click()
    chrome = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='v-list-item__title' and text()='Chrome']")))
    chrome.click()
    version = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'selenium-test-campaign-form-browsers-chrome-version-field')))
    version.click()
    ActionChains(browser).send_keys('0').perform()

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
    error_message = "The targets.browser_target.browser_ids.0.browser_version must be at least 1."

    if error_message in details_text:
        print("Test passed successfully")
    else:
        print("Test failed")
    time.sleep(30)