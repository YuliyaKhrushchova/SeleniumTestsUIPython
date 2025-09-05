from pages.login_page import LoginPage
from utils.config import LOGIN_URL
from utils.test_data import VALID_CREDS, INVALID_CREDS
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es


def test_valid_login(browser):
    page = LoginPage(browser,LOGIN_URL)
    page.open()
    page.insert_email(VALID_CREDS["email"])
    page.insert_pass(VALID_CREDS["pass"])
    page.submit_login()
    WebDriverWait(browser, 10).until_not(es.url_to_be(LOGIN_URL))
    browser.save_screenshot('./artifacts/login_valid.png')


def test_invalid_login(browser):
    page = LoginPage(browser,LOGIN_URL)
    page.open()
    page.login(INVALID_CREDS["email"], INVALID_CREDS["pass"])
    assert page.is_error_message_visible(), "Error message is not displayed"
    assert browser.current_url == LOGIN_URL, f"User is redirected to {browser.current_url} "
    browser.save_screenshot('./artifacts/login_invalid.png')

def test_go_to_register_page(browser):
    page = LoginPage(browser, LOGIN_URL)
    page.open()
    page.go_to_register_page()
    WebDriverWait(browser, 10).until_not(es.url_to_be(LOGIN_URL))
    browser.save_screenshot('./artifacts/login_to_register.png')

def test_go_to_main_page(browser):
    page = LoginPage(browser, LOGIN_URL)
    page.open()
    page.go_to_main_page()
    WebDriverWait(browser, 10).until_not(es.url_to_be(LOGIN_URL))
    browser.save_screenshot('./artifacts/login_to_main.png')
