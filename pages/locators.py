from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO = (By.CLASS_NAME, "logo")
    NOTIFICATION_TOAST = (By.CLASS_NAME, "p-toast")
    TOAST_MESSAGE_INFO = (By.CSS_SELECTOR, ".p-toast .p-toast-message-info")
    TOAST_MESSAGE_ERROR = (By.CSS_SELECTOR, ".p-toast .p-toast-message-error")
    BTN = (By.CLASS_NAME, "p-button")
    OPTIONS_PANEL = (By.CLASS_NAME, "p-dropdown-panel")
    PASSWORD_STRENGTH_PANEL = (By.CLASS_NAME, "p-password-panel")
    CONFIRM_POPUP = (By.CLASS_NAME, "p-confirm-popup")
    CONFIRM_POPUP_ACCEPT_BTN = (By.CSS_SELECTOR,
                                ".p-confirm-popup "
                                ".p-button.p-confirm-popup-accept")
    CONFIRM_POPUP_REJECT_BTN = (By.CSS_SELECTOR,
                                ".p-confirm-popup "
                                ".p-button.p-confirm-popup-reject")

    def dropdown_option_by_text(self, option_text):
        return (By.CSS_SELECTOR, f"li[aria-label='{option_text}']")



class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "[href='#/login'] > span")
    REGISTER_LINK = (By.CSS_SELECTOR, "[href='#/register'] > span")
    CARD_LIST = (By.CSS_SELECTOR, 'div.product-grid-item.card')
    CARD_NAME = (By.CSS_SELECTOR, 'div.product-name')
    CARD_DETAILS_BTN = (By.CSS_SELECTOR, 'button[aria-label="Details"]')
    CARD_PRICE = (By.CSS_SELECTOR, 'span.ml-2')
    CARD_CATEGORY = (By.CLASS_NAME, "product-category")
    TYPE_DROPDOWN = (By.ID, "typesSelector")


class DetailsPageLocators:
    PANE_TITLE = (By.CLASS_NAME, 'p-card-title')
    DETAILS_IMG = (By.CSS_SELECTOR, '.p-card-content > .p-image .pi-eye')


class LoginPageLocators:
    LOGIN_EMAIL_INPUT = (By.ID, "login")
    LOGIN_PASS_INPUT = (By.CSS_SELECTOR, "#password > input")
    PASSWORD_STRENGTH_PANEL = (By.CLASS_NAME, "p-password-panel")
    LOGIN_SUBMIT_BTN = (By.CLASS_NAME, "p-button")
    LOGIN_ERROR_MESSAGE = (By.CLASS_NAME, "p-message-error")
    REGISTER_LINK = (By.CSS_SELECTOR, "[href='#/register'] > span")


class RegisterPageLocators:
    REGISTER_EMAIL_INPUT = (By.ID, "login")
    REGISTER_PASS_INPUT = (By.CSS_SELECTOR, "#password > input")
    REGISTER_PASS_CONFIRM_INPUT = (By.CSS_SELECTOR, "#confirm_password > "
                                                    "input")
    REGISTER_SUBMIT_BTN = (By.CLASS_NAME, "p-button")
    REGISTER_ERROR_MESSAGE = (By.CLASS_NAME, "p-message-error")


class ProfilePageLocators:
    PROFILE_LINK = (By.CSS_SELECTOR, "[href='#/register'] > span")
    QUIT_BTN = (By.XPATH, "//span[contains(@class, "
                          "'pi-power-off')]/parent::a")
    NO_RECORDS_PLACEHOLDER = (By.CLASS_NAME, "p-dataview-emptymessage")
    PET_CARD_ITEM = (By.CLASS_NAME, "product-list-item")
    ADD_PET_BTN = (By.CSS_SELECTOR,
                   ".p-dataview-header .p-button.p-button-primary")
    DELETE_BTN = (By.CSS_SELECTOR,
                  ".p-dataview-header .p-button:not(.p-button-primary)")

    def pet_item_by_name(self, pet_name):
        return By.XPATH, (f"//div[contains(@class,'product-name') and "
                          f"text()='{pet_name}']/ancestor::div[contains("
                          f"@class,'product-list-item')]']")


class NewPetPageLocators:
    NAME_INPUT = (By.ID, "name")
    AGE_INPUT = (By.ID, "age")
    TYPE_DROPDOWN = (By.ID, "typeSelector")
    GENDER_DROPDOWN = (By.ID, "genderSelector")
    NEW_PET_SUBMIT_BTN = (By.CSS_SELECTOR, f"button[type='Submit']")
