from .base_page import BasePage
from .locators import RegisterPageLocators, BasePageLocators


class RegisterPage(BasePage):
    def insert_email(self, email):
        register_email_input = (
            self.browser.find_element(
                *RegisterPageLocators.REGISTER_EMAIL_INPUT))
        register_email_input.send_keys(email)

    def insert_pass(self, password):
        register_pass_input = (
            self.browser.find_element(
                *RegisterPageLocators.REGISTER_PASS_INPUT))
        register_pass_input.send_keys(password)

    def insert_confirm_pass(self, password):
        register_confirm_pass_input = (
            self.browser.find_element(
                *RegisterPageLocators.REGISTER_PASS_CONFIRM_INPUT))
        register_confirm_pass_input.send_keys(password)

    def submit_registration(self):
        registration_submit_btn = (
            self.browser.find_element(
                *RegisterPageLocators.REGISTER_SUBMIT_BTN))
        registration_submit_btn.submit()

    def register(self, user_email, password1, password2):
        self.insert_email(user_email)
        self.insert_pass(password1)
        self.insert_pass(password2)
        self.submit_registration()

    def go_to_main_page(self):
        main_page_link = self.browser.find_element(*BasePageLocators.LOGO)
        main_page_link.click()
