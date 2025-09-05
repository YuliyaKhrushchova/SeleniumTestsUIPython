from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "[href='#/login'] > span")

class LoginPageLocators:
    LOGIN_EMAIL_INPUT = (By.ID, "login")
    LOGIN_PASS_INPUT = (By.CSS_SELECTOR, "#password > input")
    LOGIN_SUBMIT_BTN = (By.CLASS_NAME, "p-button")