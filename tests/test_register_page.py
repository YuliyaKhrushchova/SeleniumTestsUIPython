import pytest

from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.register_page import RegisterPage
from utils.config import REGISTER_URL, PROFILE_URL, BASE_URL
from utils.test_data import VALID_CREDS
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es


class TestRegisterPage:

    @pytest.mark.regression
    def test_go_main_page(self, browser):
        page = RegisterPage(browser, REGISTER_URL)
        page.open()
        page.go_to_main_page()
        page.wait.until_not(page.es.url_to_be(REGISTER_URL))
        assert browser.current_url == BASE_URL, \
            f"User is redirected to {browser.current_url} "

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_register_user(self, browser, creds):
        register_page = RegisterPage(browser, REGISTER_URL)
        register_page.open()
        register_page.insert_email(creds["email"])
        register_page.insert_pass(creds["password"])
        register_page.insert_confirm_pass(creds["password"])
        register_page.submit_registration()
        register_page.wait.until_not(register_page.es.url_to_be(REGISTER_URL))
        assert browser.current_url == PROFILE_URL, (f"URL is "
                                                    f"{browser.current_url} ")
        profile_page = ProfilePage(browser, PROFILE_URL)
        assert profile_page.is_add_pet_btn_visible(), ("Profile page is not "
                                                       "displayed")
        assert profile_page.is_list_empty(), ("List of items is not empty for"
                                              " newly created user")

    @pytest.mark.flaky
    @pytest.mark.regression
    def test_register_existing_user(self, browser):
        page = RegisterPage(browser, REGISTER_URL)
        page.open()
        page.register(VALID_CREDS["email"], VALID_CREDS["password"],
                      VALID_CREDS["password"])
        assert page.is_error_message_visible(), \
            "Error message is not displayed"
        assert browser.current_url == REGISTER_URL, \
            f"User is redirected to {browser.current_url} "

