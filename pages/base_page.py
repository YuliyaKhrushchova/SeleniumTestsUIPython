"""Base page object for Selenium tests."""
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import BasePageLocators


class BasePage:
    """Class representing the base page for Selenium tests."""
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.es = es
        self.timeout = timeout
        self.wait = WebDriverWait(self.browser, self.timeout)

    def open(self):
        """ Open page by URL"""
        self.browser.get(self.url)

    def current_url(self):
        """returns current url of page"""
        return self.browser.current_url

    def is_error_notification_visible(self):
        """checks if error notification is visible"""
        error_notification = self.browser.find_elements(
            *BasePageLocators.TOAST_MESSAGE_ERROR)
        return len(error_notification) > 0

    def is_info_notification_visible(self):
        """Check if info notification is visible."""
        info_notification = self.browser.find_elements(
            *BasePageLocators.TOAST_MESSAGE_INFO)
        return len(info_notification) > 0

    def is_confirmation_popup_visible(self):
        """Check if confirmation popup is visible."""
        popup = self.browser.find_elements(
            *BasePageLocators.CONFIRM_POPUP)
        return len(popup) > 0

    def confirm_popup_action(self):
        """Click the confirm button on the popup."""
        confirm_btn = self.browser.find_element(
            *BasePageLocators.CONFIRM_POPUP_ACCEPT_BTN)
        confirm_btn.click()
