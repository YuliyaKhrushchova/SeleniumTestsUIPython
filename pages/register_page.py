from .base_page import BasePage
from .locators import RegisterPageLocators

class RegisterPage(BasePage):
    def insert_email(self, email):
        register_email_input = self.browser.find_element(*RegisterPageLocators.REGISTER_EMAIL_INPUT)
        register_email_input.send_keys(email)

    def insert_pass(self,password):
        register_pass_input = self.browser.find_element(*RegisterPageLocators.REGISTER_PASS_INPUT)
        register_pass_input.send_keys(password)

    def register(self, user_email, password):
        register_email_input = self.browser.find_element(*RegisterPageLocators.REGISTER_EMAIL_INPUT)