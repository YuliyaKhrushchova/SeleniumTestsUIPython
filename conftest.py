import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def browser():
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    opts.add_argument("start-maximized")
    browser = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub', options=opts)
    yield browser
    browser.quit()