from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es

from pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.es = es
        self.timeout = timeout
        self.wait = WebDriverWait(self.browser, self.timeout)

    def open(self):
        self.browser.get(self.url)

    def current_url(self):
        return self.browser.current_url

    def is_error_notification_visible(self):
        error_notification = self.browser.find_elements(
            *BasePageLocators.TOAST_MESSAGE_ERROR)
        return len(error_notification) > 0

    def is_info_notification_visible(self):
        info_notification = self.browser.find_elements(
            *BasePageLocators.TOAST_MESSAGE_INFO)
        return len(info_notification) > 0

    def is_confirmation_popup_visible(self):
        popup = self.browser.find_elements(
            *BasePageLocators.CONFIRM_POPUP)
        return len(popup) > 0

    def confirm_popup_action(self):
        confirm_btn = self.browser.find_element(*BasePageLocators.CONFIRM_POPUP_ACCEPT_BTN)
        confirm_btn.click()
