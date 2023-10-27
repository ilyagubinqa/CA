from selenium import webdriver
from selenium.webdriver import ActionChains
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

def test_banner(browser):
    # Открытие браузера и переход на страницу регистрации
    browser.maximize_window()
    browser.get('https://app.staging1.clickadilla.com/login')

    # Ожидание появления полей и ввод данных для авторизации
    wait = WebDriverWait(browser, 55)
    login_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-email-field")))
    login_input.send_keys('test_selenium04@gmail.com')
    password_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-password-field")))
    password_input.send_keys('test_selenium04@gmail.com')
    send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
    send_button.click()
    wait = WebDriverWait(browser, 30)

    # Переход в раздел Ads
    element = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/ads']")))
    element.click()

    # Выбор gallery
    create_gallery = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div[11]')))
    create_gallery.click()
    create_ads = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div/div[2]/div/div[1]/a/span/span")))
    create_ads.click()
    time.sleep(1)

    # Заполнение полей для создания креатива
    url = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div[1]/div')))
    ActionChains(browser).click(url).perform()
    ActionChains(browser).send_keys('https://app.clickadilla.com').perform()
    content_feed_name = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div')))
    ActionChains(browser).click(content_feed_name).perform()
    ActionChains(browser).send_keys('q').perform()
    provider = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[4]/div[2]/div/div[1]/div')))
    ActionChains(browser).click(provider).perform()
    ActionChains(browser).send_keys('q').perform()

    # Отправка запроса на создание gallery
    send_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="text-subtitle-2 px-8 text-capitalize v-btn v-btn--is-elevated v-btn--has-bg theme--light v-size--large primary"]//span[contains(text(),"Save")]')))
    send_button.click()

    # Вывод сообщения об ошибке
    time.sleep(2)

    # Поиск ошибки
    details_element = browser.find_element(By.CLASS_NAME, "v-messages__message")

    # Текст элемента
    details_text = details_element.text

    # Проверка на то, что ошибка содержит текст
    error_message = "The provider website should be valid URL."

    if error_message in details_text:
        print("Test passed successfully")
    else:
        print("Test failed")
    time.sleep(30)