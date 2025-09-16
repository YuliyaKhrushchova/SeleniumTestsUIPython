import pytest
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.support.wait import WebDriverWait

from pages.profile_page import ProfilePage
from utils.config import PROFILE_URL, BASE_URL, LOGIN_URL


class TestProfilePageAuthorized:
    @pytest.mark.flaky
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_logout(self, logged_in_browser):
        page = ProfilePage(logged_in_browser, PROFILE_URL)
        page.log_out()
        assert page.is_error_notification_visible(), ("Error notification is "
                                                      "not displayed")
        assert page.current_url() == LOGIN_URL, f"URL is {page.current_url()} "

    @pytest.mark.flaky
    @pytest.mark.regression
    def test_add_pet(self, logged_in_browser_2):
        driver, creds = logged_in_browser_2
        page = ProfilePage(driver, PROFILE_URL)
        page.open()
        page.add_pet_btn_click()
        WebDriverWait(driver, 10).until_not(
            es.url_to_be(PROFILE_URL))
        driver.save_screenshot('./artifacts/add.png')

    @pytest.mark.regression
    def test_delete_user(self, logged_in_browser_2):
        driver, creds = logged_in_browser_2
        page = ProfilePage(driver, PROFILE_URL)
        page.open()
        page.delete_btn_click()
        assert page.is_confirmation_popup_visible(), ("Confirmation popup is "
                                                      "not displayed")
        page.confirm_popup_action()
        assert page.is_info_notification_visible(), ("Info notification is "
                                                     "not displayed")
        assert page.is_error_notification_visible(), ("Error notification is "
                                                      "not displayed")
        assert page.current_url() == LOGIN_URL, f"URL is {page.current_url()} "
