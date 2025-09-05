from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGO = (By.CLASS_NAME, "logo")
    NOTIFICATION_TOAST = (By.CLASS_NAME, "p-toast")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "[href='#/login'] > span")
    def card_by_name (string_param):
        return By.XPATH, f"//div[contains(@class,'product-name') and text()='{string_param}']/ancestor::div[contains(@class,'card')]']"

class LoginPageLocators:
    LOGIN_EMAIL_INPUT = (By.ID, "login")
    LOGIN_PASS_INPUT = (By.CSS_SELECTOR, "#password > input")
    LOGIN_SUBMIT_BTN = (By.CLASS_NAME, "p-button")
    LOGIN_ERROR_MESSAGE = (By.CLASS_NAME, "p-message-error")
    REGISTER_LINK = (By.CSS_SELECTOR, "[href='#/register'] > span")

class RegisterPageLocators:
    REGISTER_EMAIL_INPUT = (By.ID, "login")
    REGISTER_PASS_INPUT = (By.ID, "password")
    REGISTER_PASS_CONFIRM_INPUT = (By.ID, "confirm_password")
    REGISTER_SUBMIT_BTN = (By.CLASS_NAME, "p-button")

