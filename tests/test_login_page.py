import pytest

from pages.login_page import LoginPage
from utils.config import LOGIN_URL, PROFILE_URL, REGISTER_URL, BASE_URL
from utils.test_data import VALID_CREDS, INVALID_CREDS


class TestLoginPage:

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_valid_login(self, browser):
        page = LoginPage(browser, LOGIN_URL)
        page.open()
        page.insert_email(VALID_CREDS["email"])
        page.insert_pass(VALID_CREDS["password"])
        page.submit_login()
        page.wait.until_not(page.es.url_to_be(LOGIN_URL))
        assert browser.current_url == PROFILE_URL, f"URL is {browser.current_url} "

    @pytest.mark.regression
    def test_invalid_login(self, browser):
        page = LoginPage(browser, LOGIN_URL)
        page.open()
        page.login(INVALID_CREDS["email"], INVALID_CREDS["password"])
        assert page.is_error_message_visible(), \
            "Error message is not displayed"
        assert page.is_error_notification_visible(), ("Error notification is "
                                                      "not displayed")
        assert browser.current_url == LOGIN_URL, \
            f"User is redirected to {browser.current_url} "

    @pytest.mark.regression
    def test_go_to_register_page(self, browser):
        page = LoginPage(browser, LOGIN_URL)
        page.open()
        page.go_to_register_page()
        assert browser.current_url == REGISTER_URL, f"URL is {browser.current_url} "

    @pytest.mark.regression
    def test_go_to_main_page(self, browser):
        page = LoginPage(browser, LOGIN_URL)
        page.open()
        page.go_to_main_page()
        assert browser.current_url == BASE_URL, f"URL is {browser.current_url} "
