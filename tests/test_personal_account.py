import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage

@allure.feature("Личный кабинет")
class TestPersonalAccount:

    @allure.title("Переход в личный кабинет")
    def test_go_to_personal_account(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_personal_account()

        login_page = LoginPage(driver)
        login_page.wait_for_url_contains("login")
        assert "login" in login_page.get_current_url()
