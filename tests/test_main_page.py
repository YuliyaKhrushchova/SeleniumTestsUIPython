from pages.main_page import MainPage
from utils.config import BASE_URL


def test_go_to_login_page(browser):
    page = MainPage(browser, BASE_URL)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot("./artifacts/test_go_to_login_page.png")


