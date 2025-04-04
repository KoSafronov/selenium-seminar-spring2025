from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.locators.vk_locators import LoginPageLocators


class LoginPage(BasePage):
    url = 'https://education.vk.company/pages/index'
    locators = LoginPageLocators

    def login(self, username, password):
        print("Открываем главную страницу...")
        self.driver.get(self.url)

        print("Ожидаем кнопку 'вход / регистрация'...")
        self.wait(timeout=10).until(EC.element_to_be_clickable(self.locators.LOGIN_BUTTON))
        self.click(self.locators.LOGIN_BUTTON)

        print("Ожидаем 'Продолжить с помощью почты и пароля'...")
        self.wait(timeout=10).until(EC.element_to_be_clickable(self.locators.CONTINUE_WITH_EMAIL))
        self.click(self.locators.CONTINUE_WITH_EMAIL)

        print("Ждём поле email...")
        self.wait(timeout=10).until(EC.presence_of_element_located(self.locators.LOGIN_INPUT))

        print("Вводим логин и пароль...")
        self.find(self.locators.LOGIN_INPUT).send_keys(username)
        self.find(self.locators.PASSWORD_INPUT).send_keys(password)

        print("Нажимаем 'Войти с паролем'...")
        self.click(self.locators.SUBMIT_BUTTON)

        print("Ждём редирект на /feed...")
        self.wait(timeout=10).until(lambda d: "/feed" in d.current_url or "/blog" in d.current_url)

        return MainPage(self.driver)
