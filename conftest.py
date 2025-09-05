import pytest
from selenium import webdriver
import os
import time

@pytest.fixture(autouse=True)
def browser(request):
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=opts)


    yield browser
    browser.quit()