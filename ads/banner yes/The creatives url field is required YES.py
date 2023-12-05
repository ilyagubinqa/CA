from selenium import webdriver
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
    chrome_browser.implicitly_wait(25)
    return chrome_browser

def test_banner(browser):
    # Открытие браузера и переход на страницу регистрации
    browser.maximize_window()
    browser.get('https://staging-app.clickadilla.com/login')

    # Ожидание появления полей и ввод данных для авторизации
    wait = WebDriverWait(browser, 55)
    login_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-email-field")))
    login_input.send_keys('test_selenium04@gmail.com')
    password_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-password-field")))
    password_input.send_keys('test_selenium04@gmail.com')
    send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
    send_button.click()

    # Переход в раздел Ads
    wait = WebDriverWait(browser, 30)
    element = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/ads']")))
    element.click()

    # Выбор баннера
    create_banner = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'selenium-test-ads-tab-item-banner-field')))
    create_banner.click()
    create_ads = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, "selenium-test-ads-create-ads")))
    create_ads.click()

    # Заполнение полей для создания креатива
    select_banner_size = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, 'selenium-test-ad-form-size')))
    select_banner_size.click()
    size = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='v-list-item__title' and text()='160x600']")))
    size.click()

    # Загрузка файла для креатива
    image = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@type = 'file']")))
    image.send_keys("C:\PycharmProjects\img\jpeg2.jpg")
    done = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'doka--button-action-confirm') and span[text()='Done']]")))
    done.click()
    time.sleep(15)

    # Отправка запроса на создание баннера
    send_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, 'selenium-test-ad-form-save')))
    send_button.click()

    # Вывод сообщения об ошибке
    time.sleep(2)

    # Поиск ошибки
    details_element = browser.find_element(By.CLASS_NAME, "v-messages__message")

    # Текст элемента
    details_text = details_element.text

    # Проверка на то, что ошибка содержит текст
    error_message = "The creatives.0.url field is required."

    if error_message in details_text:
        print("Test passed successfully")
    else:
        print("Test failed")
    time.sleep(20)