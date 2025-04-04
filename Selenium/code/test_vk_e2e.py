import pytest
from ui.pages.login_page import LoginPage
from ui.pages.people_page import PeoplePage
from ui.pages.schedule_page import SchedulePage
from user_data import CREDENTIALS, SEARCH_PERSON_NAME, SEMINAR_DATE, SEMINAR_TITLE

class TestVkEducation:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.people_page = PeoplePage(driver)
        self.schedule_page = SchedulePage(driver)

    def test_login_success(self):
        self.login_page.login(CREDENTIALS["login"], CREDENTIALS["password"])

    def test_find_person(self):
        self.login_page.login(CREDENTIALS["login"], CREDENTIALS["password"])
        self.driver.get("https://education.vk.company/people/")
        self.people_page.search(SEARCH_PERSON_NAME)

    def test_current_seminar(self):
        self.login_page.login(CREDENTIALS["login"], CREDENTIALS["password"])
        self.driver.get("https://education.vk.company/schedule/")
        assert self.schedule_page.check_seminar(SEMINAR_DATE, SEMINAR_TITLE)
