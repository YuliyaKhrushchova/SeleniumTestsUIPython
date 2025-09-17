from .base_page import BasePage
from .locators import MainPageLocators, BasePageLocators


class MainPage(BasePage):

    def open(self):
        super().open()
        self.wait_for_cards_to_load()

    def wait_for_cards_to_load(self, cnt=1):
        self.wait.until(
            lambda d: len(d.find_elements(*MainPageLocators.CARD_LIST)) >= cnt
        )

    def go_to_login_page(self):
        login_link = self.browser.find_element(
            *MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_register_page(self):
        register_link = self.browser.find_element(
            *MainPageLocators.REGISTER_LINK)
        register_link.click()

    def get_card_type(self, card):
        return card.find_element(*MainPageLocators.CARD_CATEGORY).text

    def get_card_price(self, card):
        return card.find_element(*MainPageLocators.CARD_PRICE).text

    def get_all_cards(self):
        return self.browser.find_elements(*MainPageLocators.CARD_LIST)

    def get_card_by_index(self, index: int):
        cards = self.get_all_cards()
        return cards[index - 1]

    def get_card_by_name(self, name: str):
        for card in self.get_all_cards():
            title_element = card.find_element(*MainPageLocators.CARD_NAME)
            if title_element.text.strip() == name:
                return card
        raise Exception(f"Card with name '{name}' not found")

    def get_card_price_by_name(self, name: str) -> str:
        card = self.get_card_by_name(name)
        return self.get_card_price(card)

    def click_details_by_card_name(self, name: str):
        card = self.get_card_by_name(name)
        details_btn = card.find_element(*MainPageLocators.CARD_DETAILS_BTN)
        details_btn.click()

    def get_card_name_by_index(self, index: int):
        card = self.get_card_by_index(index)
        return card.find_element(*MainPageLocators.CARD_NAME).text

    def click_details_button_by_index(self, index: int):
        card = self.get_card_by_index(index)
        button = card.find_element(*MainPageLocators.CARD_DETAILS_BTN)
        button.click()

    def get_cards_count(self):
        return len(self.browser.find_elements(*MainPageLocators.CARD_LIST))

    def get_filter_type_value(self):
        types_dropdown = self.browser.find_element(
            *MainPageLocators.TYPE_DROPDOWN)
        return types_dropdown.text

    def filter_cards_by_type(self, pet_type):
        if not type:
            raise ValueError("List of types cannot be empty")

        types_dropdown = self.browser.find_element(
            *MainPageLocators.TYPE_DROPDOWN)
        types_dropdown.click()
        self.wait.until(self.es.visibility_of_element_located(
            BasePageLocators.OPTIONS_PANEL))

        option_locator = BasePageLocators.dropdown_option_by_text(pet_type)
        option = self.browser.find_element(*option_locator)
        option.click()
