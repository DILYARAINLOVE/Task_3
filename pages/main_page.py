from locators.main_locators import MainPageLocators
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators

    def open(self):
        self.driver.get("https://stellarburgers.education-services.ru/")

    def click_personal_account(self):
        self.click_element(self.locators.PERSONAL_ACCOUNT_BUTTON)

    def click_constructor(self):
        self.click_element(self.locators.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        self.click_element(self.locators.ORDER_FEED_BUTTON)

    def click_ingredient(self, index=0):
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        if len(ingredients) > index:
            ingredients[index].click()

    def is_modal_open(self):
        """Проверяет, открыто ли модальное окно ингредиента"""
        return self.is_element_visible(self.locators.MODAL)

    def close_modal(self):
        self.click_element(self.locators.MODAL_CLOSE)

    def wait_for_modal_closed(self):
        self.wait_for_element_invisible(self.locators.MODAL)

    def get_ingredient_counter_value(self, index=0):
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        if len(ingredients) > index:
            counter = ingredients[index].find_element(*self.locators.INGREDIENT_COUNTER)
            return int(counter.text) if counter.text.isdigit() else 0
        return 0
