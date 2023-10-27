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
    wait = WebDriverWait(driver, 55)
    login_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-email-field")))
    login_input.send_keys('test_selenium04@gmail.com')
    password_input = wait.until(EC.element_to_be_clickable((By.ID, "selenium-test-login-password-field")))
    password_input.send_keys('test_selenium04@gmail.com')
    send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content")))
    send_button.click()
    wait = WebDriverWait(driver, 30)

    # Переход в раздел Ads
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/ads']")))
    element.click()

    # Выбор In page
    create_inpage = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[2]/div[1]/div/div[2]/div/div[12]')))
    create_inpage.click()
    create_ads = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div/div/div/div[1]/a/span/span")))
    create_ads.click()
    time.sleep(1)

    # Заполнение полей для создания креатива
    url = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[4]/div/div/div/div/div[1]/div[1]/div[2]/div/div[1]/div')))
    url.click()
    pyautogui.typewrite('https://app.clickadilla.com')
    title = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[4]/div/div/div/div/div[1]/div[3]/div[2]/div/div[1]/div')))
    title.click()
    pyautogui.typewrite('test')
    description = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[4]/div/div/div/div/div[1]/div[5]/div[2]/div/div[1]/div')))
    description.click()
    pyautogui.typewrite('testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest')
    time.sleep(3)

    # Загрузка файла для креатива
    image = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@type = 'file']")))
    image.send_keys("C:\PycharmProjects\img\jpeg2.jpg")
    done = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'doka--button-action-confirm') and span[text()='Done']]")))
    done.click()
    time.sleep(15)

    # Отправка запроса на создание in page
    send_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="text-subtitle-2 px-8 text-capitalize v-btn v-btn--is-elevated v-btn--has-bg theme--light v-size--large primary"]//span[contains(text(),"Save")]')))
    send_button.click()

    # Вывод сообщения о создании креатива
    time.sleep(3)
    status_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/div/div/div[3]/div/div/div[1]/button/span')))
    status = status_element.text

    if status == "Start Another Campaign":
        print("Your Ad Campaign created successfully")
    else:
        print("Failed to created Ad Campaign")

    sleep(50)