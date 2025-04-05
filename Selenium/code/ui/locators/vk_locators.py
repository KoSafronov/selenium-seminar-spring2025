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
    SEMESTER_TAB = (By.XPATH, '//li[@intervalid="semester"]')
    EVENT_TYPE_DROPDOWN = (By.XPATH, '//div[contains(@class, "schedule-filters__item_type")]//div[contains(@class, "r-input-flex")]')
    EVENT_TYPE_OPTION = lambda value: (By.XPATH, f'//span[@class="option-label" and normalize-space()="{value}"]')
    DATE_CELL = lambda value: (By.XPATH, f"//td[contains(@class, 'schedule-timetable__item__date')]//*[contains(text(), '{value}')]")
    TITLE_CELL = lambda value: (By.XPATH, f"//td[contains(@class, 'schedule-timetable__item__event')]//a[contains(., '{value}')]")
