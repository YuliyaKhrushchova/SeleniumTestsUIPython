import pytest
from pages.main_page import MainPage
from pages.details_page import DetailsPage
from utils.config import BASE_URL, REGISTER_URL, LOGIN_URL, DETAILS_URL


class TestMainPage:

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_go_to_login_page(self, browser):
        page = MainPage(browser, BASE_URL)
        page.open()
        page.go_to_login_page()
        assert browser.current_url == LOGIN_URL, \
            (f"User is redirected to {browser.current_url} "
             f"instead of {LOGIN_URL}")

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_go_register_page(self, browser):
        page = MainPage(browser, BASE_URL)
        page.open()
        page.go_to_register_page()
        assert browser.current_url == REGISTER_URL, \
            (f"User is redirected to {browser.current_url} "
             f"instead of {REGISTER_URL}")

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_open_pet_details(self, browser):
        main_page = MainPage(browser, BASE_URL)
        main_page.open()
        main_page.click_details_button_by_index(8)
        assert browser.current_url.startswith(DETAILS_URL), \
            (f"User is redirected to {browser.current_url} "
             f"instead of {REGISTER_URL}")

        details_page = DetailsPage(browser, DETAILS_URL)
        details_page.wait_for_content_to_load()


    @pytest.mark.flaky
    @pytest.mark.parametrize("pet_types", ('cat', 'parrot'))
    def test_filter_by_type(self, browser, pet_types):
        main_page = MainPage(browser, BASE_URL)
        main_page.open()
        main_page.filter_cards_by_type(pet_types)

        assert main_page.get_filter_type_value() == pet_types, \
            "Incorrect type is selected in filter"
        cards = main_page.get_all_cards()

        assert len(cards) > 0, "No Filtering result is displayed"

        for card in cards:
            card_type = main_page.get_card_type(card)
            assert card_type == pet_types, f"incorrect type {card_type}"
