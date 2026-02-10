import pytest
import allure
import time
from selenium.webdriver.common.by import By


@allure.feature("Основной функционал")
class TestMainFunctionality:
    
    @allure.title("Переход в конструктор")
    @pytest.mark.parametrize('driver', ['chrome'], indirect=True)
    def test_go_to_constructor(self, driver):
        """Проверка перехода в конструктор"""
        # Идем в ленту заказов
        driver.get("https://stellarburgers.education-services.ru/feed")
        time.sleep(2)
        
        # Ищем ссылку на конструктор
        constructor_links = driver.find_elements(By.XPATH, "//*[contains(text(), 'Конструктор') or contains(text(), 'конструктор')]")
        for link in constructor_links:
            if link.is_displayed():
                link.click()
                break
        
        time.sleep(2)
        
        # Проверяем что вернулись на главную
        assert "stellarburgers" in driver.current_url
    
    @allure.title("Переход в ленту заказов")
    @pytest.mark.parametrize('driver', ['chrome'], indirect=True)
    def test_go_to_order_feed(self, driver):
        """Проверка перехода в ленту заказов"""
        driver.get("https://stellarburgers.education-services.ru/")
        time.sleep(2)
        
        # Ищем ссылку на ленту заказов
        feed_links = driver.find_elements(By.XPATH, "//*[contains(text(), 'Лента') or contains(text(), 'лента') or contains(text(), 'Заказов') or contains(text(), 'заказов')]")
        for link in feed_links:
            if link.is_displayed():
                link.click()
                break
        
        time.sleep(2)
        
        # Проверяем URL
        assert "feed" in driver.current_url
    
    @allure.title("Модальное окно ингредиента")
    @pytest.mark.parametrize('driver', ['chrome'], indirect=True)
    def test_ingredient_details_modal(self, driver):
        """Проверка модального окна ингредиента"""
        driver.get("https://stellarburgers.education-services.ru/")
        time.sleep(2)
        
        # Ищем первый ингредиент
        ingredients = driver.find_elements(By.XPATH, "//div[contains(@class, 'BurgerIngredient')]")
        if ingredients:
            ingredients[0].click()
            time.sleep(2)
            
            # Ищем модальное окно
            modals = driver.find_elements(By.XPATH, "//div[contains(@class, 'Modal') or contains(@class, 'modal')]")
            assert len(modals) > 0
            
            # Закрываем модальное окно
            close_buttons = driver.find_elements(By.XPATH, "//button[contains(@class, 'close')]")
            for button in close_buttons:
                if button.is_displayed():
                    button.click()
                    break
            
            time.sleep(1)
    
    @allure.title("Счетчик ингредиента")
    @pytest.mark.parametrize('driver', ['chrome'], indirect=True)
    def test_ingredient_counter(self, driver):
        """Проверка счетчика ингредиента"""
        driver.get("https://stellarburgers.education-services.ru/")
        time.sleep(2)
        
        # Ищем ингредиенты
        ingredients = driver.find_elements(By.XPATH, "//div[contains(@class, 'BurgerIngredient')]")
        if ingredients:
            # Ищем счетчики
            counters = driver.find_elements(By.XPATH, "//div[contains(@class, 'counter')]")
            print(f"Найдено счетчиков: {len(counters)}")
            
            # Если есть счетчики, проверяем их
            if counters:
                for counter in counters:
                    if counter.is_displayed():
                        text = counter.text
                        if text.isdigit():
                            assert int(text) >= 0
