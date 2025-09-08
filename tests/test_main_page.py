import pytest
from pages.main_page import MainPage
from utils.config import BASE_URL, REGISTER_URL, LOGIN_URL


class TestMainPage:

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_go_to_login_page(self, browser):
        page = MainPage(browser, BASE_URL)
        page.open()
        page.go_to_login_page()
        # browser.save_screenshot("./artifacts/test_go_to_login_page.png")

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_go_register_page(self, browser):
        page = MainPage(browser, BASE_URL)
        page.open()
        page.go_to_register_page()
