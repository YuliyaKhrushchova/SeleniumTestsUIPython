import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def browser():
    opts = webdriver.ChromeOptions()
    opts.add_argument("start-maximized")
    browser = webdriver.Chrome(options=opts)
    yield browser
    browser.quit()