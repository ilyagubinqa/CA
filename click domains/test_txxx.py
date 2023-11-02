from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pytest

#вебхук Slack
slack_webhook_url = 'https://hooks.slack.com/services/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'

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(6)
    return chrome_browser

def test_domain(browser):
    # Открытие браузера и переход на страницу премиум сайта
    browser.maximize_window()
    browser.get('https://click.txxx.com')

    # Проверка на отображение блока с текстом
    time.sleep(5)
    status_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/div/div/div[3]/div/div/div[1]/button/span')))
    status = status_element.text
    print(status)
    if status == "Total visits":
        print("Test passed successfully")
    else:
        print("Test failed")

    time.sleep(5)