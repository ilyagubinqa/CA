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
    goal = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, ("//*[contains(text(),' cpc goal ')]"))))
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
    ActionChains(browser).send_keys('5').perform()

    # Выбор креатива
    time.sleep(3)
    select_ad = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'selenium-test-campaign-form-ad-select')))
    select_ad.click()
    time.sleep(3)
    add = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='v-list-item__title' and text()='test web push 2  (1 url)']")))
    add.click()

    # Заполнение поля multiple search
    multiple_search = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, ("//*[contains(text(),' Multiple search ')]"))))
    multiple_search.click()
    search_sites = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'selenium-test-campaign-form-multiple-adder-field')))
    ActionChains(browser).click(search_sites).perform()
    ActionChains(browser).send_keys('test').perform()
    search1 = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, ("//*[contains(text(),'Search ')]"))))
    search1.click()
    add_sites = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, ("//*[contains(text(),' Add found sites ')]"))))
    add_sites.click()
    time.sleep(2)

    # Запрос на создание кампании
    create = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Create campaign"]')))
    create.click()

    # Вывод сообщения о создании кампании
    time.sleep(3)
    status_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[1]/div/text()')))
    status = status_element.text

    if status == "campaign has been":
        print("Your Campaign created successfully")
    else:
        print("Failed to created Campaign")

    time.sleep(70)