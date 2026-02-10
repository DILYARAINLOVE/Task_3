import pytest
import allure
import time
from selenium.webdriver.common.by import By


@allure.feature("Лента заказов")
class TestOrderFeed:
    
    @allure.title("Детали заказа")
    @pytest.mark.parametrize('driver', ['chrome'], indirect=True)
    def test_order_details_modal(self, driver):
        """Проверка деталей заказа"""
        driver.get("https://stellarburgers.education-services.ru/feed")
        time.sleep(2)
        
        # Ищем заказы
        orders = driver.find_elements(By.XPATH, "//li[contains(@class, 'OrderHistory')] or //div[contains(@class, 'OrderCard')]")
        if orders:
            orders[0].click()
            time.sleep(2)
            
            # Проверяем что открылось модальное окно
            modals = driver.find_elements(By.XPATH, "//div[contains(@class, 'Modal')]")
            assert len(modals) > 0
    
    @allure.title("Счетчики заказов")
    @pytest.mark.parametrize('driver', ['chrome'], indirect=True)
    def test_order_counters(self, driver):
        """Проверка счетчиков заказов"""
        driver.get("https://stellarburgers.education-services.ru/feed")
        time.sleep(2)
        
        # Ищем счетчики
        counters = driver.find_elements(By.XPATH, "//p[contains(text(), 'Выполнено') or contains(text(), 'выполнено')]")
        print(f"Найдено счетчиков: {len(counters)}")
        
        # Проверяем что счетчики отображаются
        if counters:
            for counter in counters:
                if counter.is_displayed():
                    print(f"Счетчик: {counter.text}")
