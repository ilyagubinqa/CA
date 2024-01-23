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

    # Заполнение campaign name
    campaign_name = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'selenium-test-campaign-form-name-field')))
    ActionChains(browser).click(campaign_name).perform()
    ActionChains(browser).send_keys('test').perform()
    time.sleep(2)

    # Заполнение campaign group
    campaign_name = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'selenium-test-campaign-form-category-select')))
    campaign_name.click()
    time.sleep(1)
    group = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='v-list-item__title' and text()='test']")))
    group.click()
    time.sleep(7)

    # Заполнение поля с ценой
    amount = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'selenium-test-campaign-form-price-field')))
    ActionChains(browser).click(amount).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
    ActionChains(browser).send_keys('8').perform()

    # Заполненеие поля с sub period
    days = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[5]/div[2]/div/div/div/div[2]/button[2]/span')))
    days.click()

    # Заполнение Traffic quality
    qaulity = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[6]/div[2]/div/div[1]/div[1]/div[2]/button[1]/span')))
    qaulity.click()

    # Выбор креатива
    time.sleep(3)
    select_ad = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'selenium-test-campaign-form-ad-select')))
    select_ad.click()
    time.sleep(3)
    add = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='v-list-item__title' and text()='test web push 2  (1 url)']")))
    add.click()

    # Выбор categories
    categories = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[1]/div[1]/div/div/div[8]/div[2]/div/div/div/div[1]/div/div[1]/div/div/div')))
    categories.click()

    # Выбор hourly limits
    hourhy_limits = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'selenium-test-campaign-form-hourly-limit-field')))
    ActionChains(browser).click(hourhy_limits).perform()
    ActionChains(browser).send_keys('10').perform()
    time.sleep(2)

    # Выбор daily limits
    daily_limits = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'selenium-test-campaign-form-daily-limit-field')))
    ActionChains(browser).click(daily_limits).perform()
    ActionChains(browser).send_keys('11').perform()
    time.sleep(2)

    # Выбор total limits
    total_limits = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'selenium-test-campaign-form-total-limit-field')))
    ActionChains(browser).click(total_limits).perform()
    ActionChains(browser).send_keys('12').perform()
    time.sleep(2)

    # Выбор импрессий
    impressions = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'selenium-test-campaign-form-smooth-spend-field')))
    ActionChains(browser).click(impressions).perform()
    ActionChains(browser).send_keys('17').perform()
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