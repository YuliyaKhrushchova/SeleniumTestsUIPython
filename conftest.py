import base64

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
    browser.close()
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browser")
        if driver:
            screenshot_name = f"artifacts/{item.name}.png"
            driver.save_screenshot(screenshot_name)

def pytest_selenium_capture_debug(item, report, extra):
    for log_type in extra:
        if log_type["name"] == "Screenshot":
            content = base64.b64decode(log_type["content"].encode("utf-8"))
            with open(item.name + ".png", "wb") as f:
                f.write(content)