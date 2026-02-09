from pages.base_page import BasePage
from locators.login_locators import LoginPageLocators
import allure


class LoginPage(BasePage):
    
    @allure.step("Открыть страницу логина")
    def open_login_page(self):
        self.open("/login")
        return self
    
    @allure.step("Ввести email: {email}")
    def enter_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        return self
    
    @allure.step("Ввести пароль: {password}")
    def enter_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        return self
    
    @allure.step("Нажать кнопку 'Войти'")
    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)
        return self
    
    @allure.step("Нажать 'Зарегистрироваться'")
    def click_register_button(self):
        self.click(LoginPageLocators.REGISTER_BUTTON)
        return self
    
    @allure.step("Нажать 'Восстановить пароль'")
    def click_forgot_password_button(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_BUTTON)
        return self
    
    @allure.step("Выполнить логин с email: {email} и паролем: {password}")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        return self
    
    @allure.step("Проверить, отображается ли ошибка")
    def is_error_displayed(self):
        return self.is_element_visible(LoginPageLocators.ERROR_MESSAGE)
    
    @allure.step("Получить текст ошибки")
    def get_error_text(self):
        if self.is_error_displayed():
            return self.get_text(LoginPageLocators.ERROR_MESSAGE)
        return ""