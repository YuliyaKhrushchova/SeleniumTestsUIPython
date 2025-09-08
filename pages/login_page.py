from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def insert_email(self, email):
        login_email_input = self.browser.find_element(
            *LoginPageLocators.LOGIN_EMAIL_INPUT)
        login_email_input.send_keys(email)

    def insert_pass(self, password):
        login_pass_input = self.browser.find_element(
            *LoginPageLocators.LOGIN_PASS_INPUT)
        login_pass_input.send_keys(password)

    def submit_login(self):
        login_submit_btn = self.browser.find_element(
            *LoginPageLocators.LOGIN_SUBMIT_BTN)
        login_submit_btn.submit()

    def login(self, email, password):
        self.insert_email(email)
        self.insert_pass(password)
        self.submit_login()

    def is_error_message_visible(self):
        error_message = self.browser.find_elements(
            *LoginPageLocators.LOGIN_ERROR_MESSAGE)
        return len(error_message) > 0

    def go_to_register_page(self):
        register_link = self.browser.find_element(
            *LoginPageLocators.REGISTER_LINK)
        register_link.click()

    def go_to_main_page(self):
        main_page_link = self.browser.find_element(*BasePageLocators.LOGO)
        main_page_link.click()
