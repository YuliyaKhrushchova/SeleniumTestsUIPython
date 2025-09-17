from .base_page import BasePage
from .locators import RegisterPageLocators, BasePageLocators


class RegisterPage(BasePage):
    def email_input_click(self):
        register_email_input = self.browser.find_element(
            *RegisterPageLocators.REGISTER_EMAIL_INPUT)
        register_email_input.click()

    def insert_email(self, email):
        register_email_input = self.browser.find_element(
            *RegisterPageLocators.REGISTER_EMAIL_INPUT)
        register_email_input.send_keys(email)

    def insert_pass(self, password):
        register_pass_input = self.browser.find_element(
            *RegisterPageLocators.REGISTER_PASS_INPUT)

        register_pass_input.send_keys(password)
        self.wait.until(
            lambda d: len(
                d.find_elements(*BasePageLocators.PASS_STRENGTH_PANEL)) > 0
        )

    def insert_confirm_pass(self, password):
        register_confirm_pass_input = self.browser.find_element(
            *RegisterPageLocators.REGISTER_PASS_CONFIRM_INPUT)
        register_confirm_pass_input.send_keys(password)
        self.wait.until(
            lambda d: len(
                d.find_elements(*BasePageLocators.PASS_STRENGTH_PANEL)) > 0
        )

    def submit_registration(self):
        registration_submit_btn = (
            self.browser.find_element(
                *RegisterPageLocators.REGISTER_SUBMIT_BTN))
        registration_submit_btn.submit()

    def close_password_panel(self):
        element = self.browser.find_element(
            *BasePageLocators.PASS_STRENGTH_PANEL)
        element.click()

    def register(self, user_email, password1, password2):
        self.insert_email(user_email)
        self.insert_pass(password1)
        self.insert_confirm_pass(password2)
        self.submit_registration()

    def go_to_main_page(self):
        main_page_link = self.browser.find_element(*BasePageLocators.LOGO)
        main_page_link.click()


    def is_error_message_visible(self):
        error_message = self.browser.find_elements(
            *RegisterPageLocators.REGISTER_ERROR_MESSAGE)
        return len(error_message) > 0

