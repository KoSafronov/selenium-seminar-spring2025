class TestLogin(BaseCase):
    authorize = False  # отключаем авто-логин

    def test_login(self, credentials):
        page = LoginPage(self.driver)
        main_page = page.login(credentials["username"], credentials["password"])

        assert "feed" in self.driver.current_url
