from ui.pages.base_page import BasePage
from ui.locators.vk_locators import PeoplePageLocators


class PeoplePage(BasePage):
    locators = PeoplePageLocators

    def search(self, text):
        self.find(self.locators.SEARCH_INPUT).send_keys(text)
        self.click(self.locators.SEARCH_BUTTON)
