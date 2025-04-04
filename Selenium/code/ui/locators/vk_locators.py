from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'a.gtm-auth-header-btn')
    CONTINUE_WITH_EMAIL = (By.XPATH, '//button[contains(text(), "почты")]')
    LOGIN_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    SUBMIT_BUTTON = (By.XPATH, '//button[contains(text(), "Войти с паролем")]')


class PeoplePageLocators:
    SEARCH_INPUT = (By.NAME, 'q')  # input name="q"
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'input.input-submit')


class SchedulePageLocators:
    @staticmethod
    def date_cell(partial_date):
        return (By.XPATH, f'//td[contains(@class, "schedule-timetable__item__date")]//strong[contains(text(), "{partial_date}")]')

    @staticmethod
    def title_cell(partial_title):
        return (By.XPATH, f'//td[contains(@class, "schedule-timetable__item__event")]//strong[contains(text(), "{partial_title}")]')
