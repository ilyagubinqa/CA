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

    # Заполнение поля с ценой
    amount = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'selenium-test-campaign-form-price-field')))
    ActionChains(browser).click(amount).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
    ActionChains(browser).send_keys('8').perform()

    # Включение уников
    uniques = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div[1]/div[1]/div/div/div[12]/div[3]/div[1]/div/button[1]/span')))
    uniques.click()
    visitor = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'selenium-test-campaign-form-unique-count-field')))
    ActionChains(browser).click(visitor).perform()
    ActionChains(browser).send_keys('0').perform()
    time.sleep(2)

    # Запрос на создание кампании
    create = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Create campaign"]')))
    create.click()

    # Поиск ошибки
    details_element = browser.find_element(By.CLASS_NAME, ("v-messages__message"))

    # Текст элемента
    details_text = details_element.text

    # Проверка на то, что ошибка содержит текст
    error_message = "The view capping must be between 1 and 4294967295."

    if error_message in details_text:
        print("Test passed successfully")
    else:
        print("Test failed")
    time.sleep(30)