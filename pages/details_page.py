"""Details page object for Selenium tests."""
from .base_page import BasePage
from .locators import DetailsPageLocators


class DetailsPage(BasePage):
    """Class representing the details page."""

    def open(self):
        """Open the details page and wait for its content to load."""
        super().open()
        self.wait_for_content_to_load()

    def wait_for_content_to_load(self):
        """Wait until the details page content is fully loaded."""
        self.wait.until(
            lambda d: len(
                d.find_elements(
                    *DetailsPageLocators.PANE_TITLE)) == 3)
        loc = DetailsPageLocators.DETAILS_IMG
        self.wait.until(self.es.presence_of_element_located(loc))
