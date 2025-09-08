import pytest

from pages.register_page import RegisterPage
from utils.config import REGISTER_URL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es


class TestRegisterPage:

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_go_main_page(self, browser):
        page = RegisterPage(browser, REGISTER_URL)
        page.open()
        page.go_to_main_page()
        WebDriverWait(browser, 10).until_not(es.url_to_be(REGISTER_URL))
        # browser.save_screenshot('./artifacts/login_to_main.png')
