import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def browser():
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--start-maximized")
    opts.add_argument("start-maximized")
    browser = webdriver.Remote(
            command_executor='http://localhost:4444', options=opts)
    yield browser
    browser.quit()