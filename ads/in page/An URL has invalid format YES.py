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
    browser.get('https://staging-app.clickadilla.com/login')

    # Ожидание появления полей и ввод данных для авторизации
    wait = WebDriverWait(browser, 55)
    login_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-email-field")))
    login_input.send_keys('ilyagubin1234567@gmail.com')
    password_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-password-field")))
    password_input.send_keys('ilyagubin1234567@gmail.com')
    send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
    send_button.click()
    wait = WebDriverWait(browser, 30)

    # Переход в раздел Ads
    element = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/ads']")))
    element.click()

    # Выбор In page
    create_inpage = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'selenium-test-ads-tab-item-in-page-ad-field')))
    create_inpage.click()
    create_ads = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, "selenium-test-ads-create-ads")))
    create_ads.click()
    time.sleep(1)

    # Заполнение полей для создания креатива
    url = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'selenium-test-ad-form-creative-url-0-field')))
    ActionChains(browser).click(url).perform()
    ActionChains(browser).send_keys('q').perform()
    title = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'selenium-test-ad-form-creative-title-0-field')))
    ActionChains(browser).click(title).perform()
    ActionChains(browser).send_keys('test').perform()
    description = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'selenium-test-ad-form-creative-body-0-field')))
    ActionChains(browser).click(description).perform()
    ActionChains(browser).send_keys('test').perform()
    time.sleep(3)

    # Загрузка файла для креатива
    image = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@type = 'file']")))
    image.send_keys("C:\PycharmProjects\img\jpeg2.jpg")
    done = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'doka--button-action-confirm') and span[text()='Done']]")))
    done.click()
    time.sleep(15)

    # Отправка запроса на создание in page
    send_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, 'selenium-test-ad-form-save')))
    send_button.click()

    # Вывод сообщения об ошибке
    time.sleep(2)

    # Поиск ошибки
    details_element = browser.find_element(By.CLASS_NAME, "v-messages__message")

    # Текст элемента
    details_text = details_element.text

    # Проверка на то, что ошибка содержит текст
    error_message = "An URL has invalid format."

    if error_message in details_text:
        print("Test passed successfully")
    else:
        print("Test failed")
    time.sleep(15)