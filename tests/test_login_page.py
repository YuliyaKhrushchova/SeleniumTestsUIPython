"""Module providing a function printing python version."""
from pages.login_page import LoginPage
from utils.config import LOGIN_URL


def test_go_to_login(browser):
    """Function printing python version."""
    page = LoginPage(browser, LOGIN_URL)
    page.open()
    page.login()
    browser.save_screenshot('login2.png')
