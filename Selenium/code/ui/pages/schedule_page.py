from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import BasePage
from ui.locators.vk_locators import SchedulePageLocators as Locators
import time


class SchedulePage(BasePage):
    def check_seminar(self, partial_date: str, partial_title: str, event_type: str):
        print("Ожидаем загрузку React-компонента расписания...")
        self.wait(10).until(EC.presence_of_element_located((By.ID, "react-schedule")))

        print("Переходим на вкладку 'Весь семестр'...")
        tab = self.wait(15).until(EC.element_to_be_clickable(Locators.SEMESTER_TAB))
        tab.click()

        print("Открываем фильтр 'Тип события'...")
        dropdown = self.wait().until(
            EC.presence_of_element_located(Locators.EVENT_TYPE_DROPDOWN)
        )
        self.driver.execute_script("arguments[0].click();", dropdown)

        print(f"Выбираем тип события '{event_type}'...")
        self.wait().until(
            EC.element_to_be_clickable(Locators.EVENT_TYPE_OPTION(event_type))
        ).click()

        print("Ждем появления нужной даты...")
        self.wait().until(
            EC.presence_of_element_located(Locators.DATE_CELL(partial_date))
        )

        print("Ждем появления названия семинара...")
        seminar_link = self.wait().until(
            EC.element_to_be_clickable(Locators.TITLE_CELL(partial_title))
        )

        print("Нажимаем на название семинара...")
        windows_before = self.driver.window_handles
        seminar_link.click()
        time.sleep(1)

        windows_after = self.driver.window_handles
        if len(windows_after) > len(windows_before):
            print("Обнаружена новая вкладка. Переключаемся...")
            self.driver.switch_to.window(windows_after[-1])

        print("Ждем, пока загрузится страница семинара...")
        self.wait(15).until(EC.url_contains("/curriculum/program/lesson/"))

        print("Успешный переход на страницу семинара:", self.driver.current_url)
        return True
