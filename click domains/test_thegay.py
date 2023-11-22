from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pytest

# вебхук Slack
slack_webhook_url = 'https://hooks.slack.com/services/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'

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(6)
    return chrome_browser

def test_domain(browser):
    try:
        # Открытие браузера и переход на страницу премиум сайта
        browser.maximize_window()
        browser.get('https://click.thegay.porn')

        # Проверка на отображение блока с текстом
        time.sleep(5)
        status_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__nuxt"]/div/div/main/section[2]/div/div[1]/div[1]/div[1]/p')))
        status = status_element.text
        print(status)
        result = "Test passed successfully" if status == "Total visits" else "Test failed"

        # Сохранение результата теста
        with open("test_thegay_results.txt", "w") as file:
            file.write(result)
    except Exception as e:
        result = "Test failed"
        with open("test_thegay_results.txt", "w") as file:
            file.write(result)
        raise e
    time.sleep(5)