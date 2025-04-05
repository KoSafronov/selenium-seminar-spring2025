import pytest
from ui.pages.login_page import LoginPage
from ui.pages.people_page import PeoplePage
from ui.pages.schedule_page import SchedulePage
from test_data import CREDENTIALS, SEARCH_PERSON_NAME, SEMINAR_DATE, SEMINAR_TITLE, SEMINAR_TYPE


class TestVkEducation:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.people_page = PeoplePage(driver)
        self.schedule_page = SchedulePage(driver)

    def test_login_success(self):
        self.login_page.login(CREDENTIALS["login"], CREDENTIALS["password"])
        assert "/feed" in self.driver.current_url, "Логин не удался — нет редиректа на /feed"

    def test_find_person(self):
        self.login_page.login(CREDENTIALS["login"], CREDENTIALS["password"])
        self.driver.get("https://education.vk.company/people/")
        name_found = self.people_page.search(SEARCH_PERSON_NAME)

        assert name_found, f"Пользователь '{SEARCH_PERSON_NAME}' не найден на странице 'Люди'"


    def test_current_seminar(self):
        self.login_page.login(CREDENTIALS["login"], CREDENTIALS["password"])
        self.driver.get("https://education.vk.company/schedule/")
        result = self.schedule_page.check_seminar(SEMINAR_DATE, SEMINAR_TITLE, SEMINAR_TYPE)

        assert result, (
            f"Семинар с датой '{SEMINAR_DATE}', названием '{SEMINAR_TITLE}' и типом '{SEMINAR_TYPE}' не найден "
            f"или переход на его страницу не выполнен"
        )
