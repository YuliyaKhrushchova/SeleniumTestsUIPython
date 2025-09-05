import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def browser():
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=opts)
    yield browser
    browser.quit()