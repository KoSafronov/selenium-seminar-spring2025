from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import BasePage
from ui.locators.vk_locators import PeoplePageLocators


class PeoplePage(BasePage):
    locators = PeoplePageLocators

    def search(self, text):
        print(f"Вводим в поиск: {text}")
        self.find(self.locators.SEARCH_INPUT).send_keys(text)
        self.click(self.locators.SEARCH_BUTTON)

        print("Ожидаем появление результатов поиска...")
        self.wait(10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr")))

        # Получаем список найденных пользователей
        user_rows = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")

        print(f"Найдено записей: {len(user_rows)}")

        if len(user_rows) != 1:
            print("Ожидался один результат, но найдено другое количество")
            return False

        # Переход по ссылке на профиль
        profile_link = user_rows[0].find_element(By.CSS_SELECTOR, ".cell-name .realname a")
        profile_href = profile_link.get_attribute("href")

        print(f"Переход по ссылке: {profile_href}")
        profile_link.click()

        # Проверка, что мы на нужной странице
        self.wait(10).until(EC.url_contains("/profile/"))

        return "/profile/" in self.driver.current_url
