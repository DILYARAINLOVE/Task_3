from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators
import allure


class ForgotPasswordPage(BasePage):
    
    @allure.step("Открыть страницу восстановления пароля")
    def open_forgot_password_page(self):
        self.open("/forgot-password")
        return self
    
    @allure.step("Ввести email для восстановления: {email}")
    def enter_email(self, email):
        self.send_keys(ForgotPasswordLocators.EMAIL_INPUT, email)
        return self
    
    @allure.step("Нажать кнопку 'Восстановить'")
    def click_reset_button(self):
        self.click(ForgotPasswordLocators.RESET_BUTTON)
        return self
    
    @allure.step("Нажать на иконку показать/скрыть пароль")
    def click_show_password_button(self):
        self.click(ForgotPasswordLocators.SHOW_PASSWORD_BUTTON)
        return self
    
    @allure.step("Проверить, что поле пароля активно (подсвечено)")
    def is_password_field_active(self):
        element = self.find_element(ForgotPasswordLocators.PASSWORD_INPUT)
        classes = element.get_attribute("class")
        return "input_status_active" in classes or "input__status_active" in classes
    
    @allure.step("Проверить, виден ли пароль")
    def is_password_visible(self):
        return self.is_element_visible(ForgotPasswordLocators.PASSWORD_VISIBLE)
    
    @allure.step("Проверить, скрыт ли пароль")
    def is_password_hidden(self):
        return self.is_element_visible(ForgotPasswordLocators.PASSWORD_HIDDEN)
    
    @allure.step("Восстановить пароль для email: {email}")
    def reset_password(self, email):
        self.enter_email(email)
        self.click_reset_button()
        return self
    
    @allure.step("Проверить, открыта ли страница восстановления пароля")
    def is_forgot_password_page(self):
        return "/forgot-password" in self.get_current_url()