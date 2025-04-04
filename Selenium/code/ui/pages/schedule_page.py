from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import BasePage
from ui.locators.vk_locators import SchedulePageLocators


class SchedulePage(BasePage):
    def check_seminar(self, partial_date: str, partial_title: str):
        self.wait().until(EC.presence_of_element_located(SchedulePageLocators.date_cell(partial_date)))
        self.wait().until(EC.presence_of_element_located(SchedulePageLocators.title_cell(partial_title)))
        return True
