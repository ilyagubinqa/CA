from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pytest
import pyautogui

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(12)
    return chrome_browser


def test_create_banner(browser):
    # Открытие браузера и переход на страницу регистрации
    browser.get('https://app.staging1.clickadilla.com/login')

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
    create_banner = WebDriverWait(browser, 30).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[2]/div[1]/div/div[2]/div/div[4]')))
    create_banner.click()

    create_ads = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/main/div/div/div/div[1]/a/span/span")))
    create_ads.click()

    # Заполнение полей для создания креатива
    select_banner_size = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]')))
    select_banner_size.click()

    size = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='v-list-item__title' and text()='160x600']")))
    size.click()

    url = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div/div[2]/div/div/div[2]/div/div[5]/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div/div[1]/div')))
    url.click()
    pyautogui.typewrite('https://clickadilla.com')
    time.sleep(3)

    # Загрузка файла для креатива
    image = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@type = 'file']")))
    image.send_keys("C:\\PycharmProjects\\img\\jpeg2.jpg")

    done = WebDriverWait(browser, 30).until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(@class, 'doka--button-action-confirm') and span[text()='Done']]")))
    done.click()

    time.sleep(15)

    # Отправка запроса на создание баннера
    send_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="text-subtitle-2 px-8 text-capitalize v-btn v-btn--is-elevated v-btn--has-bg theme--light v-size--large primary"]//span[contains(text(),"Save")]')))
    send_button.click()

    # Вывод сообщения о создании креатива
    time.sleep(3)
    status_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/div/div/div[3]/div/div/div[1]/button/span')))
    status = status_element.text

    if status == "Start Another Campaign":
        print("Your Ad Campaign created successfully")
    else:
        print("Failed to create Ad Campaign")

    time.sleep(50)
