from locators.forgot_password_locators import ForgotPasswordPageLocators
from .base_page import BasePage

class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ForgotPasswordPageLocators

    def open(self):
        self.driver.get("https://stellarburgers.education-services.ru/forgot-password")

    def enter_email(self, email):
        self.find_element(self.locators.EMAIL_INPUT).send_keys(email)

    def click_recover_button(self):
        self.click_element(self.locators.RECOVER_BUTTON)

    def wait_for_reset_page(self):
        self.wait_for_url_contains("reset-password")

    def get_password_field(self):
        return self.find_element(self.locators.PASSWORD_INPUT)

    def click_show_hide_icon(self):
        self.click_element(self.locators.SHOW_HIDE_ICON)

    def is_password_visible(self):
        return self.get_password_field().get_attribute("type") == "text"
