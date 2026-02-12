import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage

@allure.feature("Восстановление пароля")
class TestForgotPassword:

    @allure.title("Переход на страницу восстановления пароля")
    def test_go_to_forgot_password_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_personal_account()

        login_page = LoginPage(driver)
        login_page.click_forgot_password_link()

        forgot_page = ForgotPasswordPage(driver)
        forgot_page.wait_for_url_contains("forgot-password")
        assert "forgot-password" in forgot_page.get_current_url()

    @allure.title("Восстановление пароля с вводом email")
    def test_password_recovery_with_email(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open()
        forgot_page.enter_email("test@example.com")
        forgot_page.click_recover_button()
        forgot_page.wait_for_reset_page()
        assert "reset-password" in forgot_page.get_current_url()

    @allure.title("Показать/скрыть пароль")
    def test_show_hide_password(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open()
        forgot_page.enter_email("test@example.com")
        forgot_page.click_recover_button()
        forgot_page.wait_for_reset_page()

        password_field = forgot_page.get_password_field()
        assert password_field.get_attribute("type") == "password"

        forgot_page.click_show_hide_icon()
        assert forgot_page.is_password_visible() is True
