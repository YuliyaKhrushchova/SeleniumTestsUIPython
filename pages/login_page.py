from .base_page import BasePage
from .locators import LoginPageLocators
from utils.test_data import CREDS

class LoginPage(BasePage):
    def login(self):
        login_email_input = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_INPUT)
        login_email_input.send_keys(CREDS["email"])
        login_pass_input = self.browser.find_element(*LoginPageLocators.LOGIN_PASS_INPUT)
        login_pass_input.send_keys(CREDS["pass"])
        login_submit_btn = self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT_BTN)
        login_submit_btn.submit()