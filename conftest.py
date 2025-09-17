import os

import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import LoginPageLocators
from utils.api_helpers import register_user_api
from utils.config import BASE_URL, LOGIN_URL, USER1_COOKIES, \
    USER1_STORAGE, USER2_COOKIES, USER2_STORAGE
from utils.helpers import (load_local_storage, load_cookies,
                           save_local_storage,
                           save_cookies, gen_creds)
from utils.test_data import VALID_CREDS


# --- Pytest options ---
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Use chrome",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="run browser in headless mode"
    )


def start_browser(request):
    headless = request.config.getoption("--headless")
    opts = webdriver.ChromeOptions()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opts)
    return driver


def start_logged_in_browser(request, creds, cookies_file, storage_file):
    driver = start_browser(request)
    driver.get(BASE_URL)

    try:
        load_local_storage(driver, storage_file)
        load_cookies(driver, cookies_file)
        driver.refresh()

        if "/profile" in driver.current_url:
            return driver
    except FileNotFoundError:
        pass

    driver.get(LOGIN_URL)
    login_email_input = driver.find_element(
        *LoginPageLocators.LOGIN_EMAIL_INPUT)
    login_email_input.send_keys(creds["email"])

    login_pass_input = driver.find_element(
        *LoginPageLocators.LOGIN_PASS_INPUT)
    login_pass_input.send_keys(creds["password"])

    login_submit_btn = driver.find_element(
        *LoginPageLocators.LOGIN_SUBMIT_BTN)
    login_submit_btn.submit()

    try:
        WebDriverWait(driver, 10).until_not(es.url_to_be(LOGIN_URL))
    except TimeoutException:
        raise Exception("Something went wrong: user is not logged in. "
                        "Please, check creds of test user")

    save_local_storage(driver, storage_file)
    save_cookies(driver, cookies_file)

    return driver


@pytest.fixture()
def browser(request):
    browser = start_browser(request)
    yield browser
    browser.close()
    browser.quit()


@pytest.fixture()
def logged_in_browser(request):
    browser = start_logged_in_browser(request, VALID_CREDS, USER1_COOKIES,
                                      USER1_STORAGE)
    yield browser
    browser.quit()


@pytest.fixture()
def logged_in_browser_2(request):
    user_creds = gen_creds("user2")
    register_user_api(user_creds)
    browser = start_logged_in_browser(request, user_creds, USER2_COOKIES,
                                      USER2_STORAGE)
    yield browser, user_creds
    browser.quit()


@pytest.fixture()
def creds():
    return gen_creds()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = None

        for _name, fixture in item.funcargs.items():
            if hasattr(fixture, "save_screenshot"):
                driver = fixture
                break

            if isinstance(fixture, tuple) and hasattr(fixture[0],
                                                      "save_screenshot"):
                driver = fixture[0]
                break

        if driver:
            os.makedirs("artifacts", exist_ok=True)
            screenshot_name = f"artifacts/{item.name}.png"
            driver.save_screenshot(screenshot_name)

