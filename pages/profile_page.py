from .base_page import BasePage
from .locators import ProfilePageLocators


class ProfilePage(BasePage):
    def log_out(self):
        quit_btn = self.browser.find_element(*ProfilePageLocators.QUIT_BTN)
        quit_btn.click()

    def add_pet_btn_click(self):
        add_btn = self.browser.find_element(*ProfilePageLocators.ADD_PET_BTN)
        add_btn.click()

    def delete_btn_click(self):
        delete_btn = self.browser.find_element(*ProfilePageLocators.DELETE_BTN)
        delete_btn.click()

    def is_add_pet_btn_visible(self):
        add_btn = self.browser.find_elements(*ProfilePageLocators.ADD_PET_BTN)
        return len(add_btn) > 0

    def is_list_empty(self):
        placeholder = self.browser.find_elements(
            *ProfilePageLocators.NO_RECORDS_PLACEHOLDER)
        list_items = self.browser.find_elements(*ProfilePageLocators.PET_CARD_ITEM)
        if len(placeholder) > 0 and len(list_items)==0:
            return True
        else:
            return False
