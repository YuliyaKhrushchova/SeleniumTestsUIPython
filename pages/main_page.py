from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(
            *MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_register_page(self):
        register_link = self.browser.find_element(
            *MainPageLocators.REGISTER_LINK)
        register_link.click()
