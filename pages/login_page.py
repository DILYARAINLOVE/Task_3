from locators.login_locators import LoginPageLocators
from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators

    def open(self):
        self.driver.get("https://stellarburgers.education-services.ru/login")

    def click_forgot_password_link(self):
        self.click_element(self.locators.FORGOT_PASSWORD_LINK)

    def login(self, email, password):
        self.find_element(self.locators.EMAIL_INPUT).send_keys(email)
        self.find_element(self.locators.PASSWORD_INPUT).send_keys(password)
        self.click_element(self.locators.LOGIN_BUTTON)
