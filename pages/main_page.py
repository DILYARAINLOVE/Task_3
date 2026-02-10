from pages.base_page import BasePage
from locators.main_locators import MainPageLocators
from selenium.webdriver import ActionChains
import allure
import time


class MainPage(BasePage):
    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get("https://stellarburgers.education-services.ru/")
        time.sleep(2)
        return self
    
    @allure.step("Кликнуть на 'Конструктор'")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)
        return self
    
    @allure.step("Кликнуть на 'Лента Заказов'")
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)
        return self
    
    @allure.step("Кликнуть на 'Личный Кабинет'")
    def click_personal_account(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        return self
    
    @allure.step("Выбрать раздел 'Булки'")
    def select_buns_section(self):
        self.click(MainPageLocators.BUN_SECTION)
        return self
    
    @allure.step("Выбрать раздел 'Соусы'")
    def select_sauces_section(self):
        self.click(MainPageLocators.SAUCE_SECTION)
        return self
    
    @allure.step("Выбрать раздел 'Начинки'")
    def select_fillings_section(self):
        self.click(MainPageLocators.FILLING_SECTION)
        return self
    
    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self, ingredient_type="bun"):
        if ingredient_type == "bun":
            locator = MainPageLocators.BUN_ITEM
        elif ingredient_type == "sauce":
            locator = MainPageLocators.SAUCE_ITEM
        else:
            locator = MainPageLocators.FILLING_ITEM
        
        self.click(locator)
        time.sleep(1)
        return self
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE)
        return self
    
    @allure.step("Проверить, открыто ли модальное окно")
    def is_modal_displayed(self):
        return self.is_element_visible(MainPageLocators.MODAL, timeout=5)
    
    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self, ingredient_type="bun"):
        # Находим ингредиент и область конструктора
        if ingredient_type == "bun":
            source = self.find_element(MainPageLocators.BUN_ITEM)
        elif ingredient_type == "sauce":
            source = self.find_element(MainPageLocators.SAUCE_ITEM)
        else:
            source = self.find_element(MainPageLocators.FILLING_ITEM)
        
        target = self.find_element(MainPageLocators.DROP_AREA)
        
        # Выполняем перетаскивание
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()
        time.sleep(1)
        return self
    
    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter(self, ingredient_type="bun"):
        if ingredient_type == "bun":
            ingredient = self.find_element(MainPageLocators.BUN_ITEM)
        elif ingredient_type == "sauce":
            ingredient = self.find_element(MainPageLocators.SAUCE_ITEM)
        else:
            ingredient = self.find_element(MainPageLocators.FILLING_ITEM)
        
        try:
            counter = ingredient.find_element(*MainPageLocators.INGREDIENT_COUNTER)
            return int(counter.text)
        except:
            return 0
    
    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)
        return self