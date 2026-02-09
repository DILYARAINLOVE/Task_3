import pytest
import allure
import time
from selenium.webdriver.common.by import By


@allure.feature("Личный кабинет")
class TestPersonalAccount:
    
    @allure.title("Переход в личный кабинет")
    @pytest.mark.parametrize('driver', ['chrome'], indirect=True)
    def test_go_to_personal_account(self, driver):
        """Проверка перехода в личный кабинет"""
        driver.get("https://stellarburgers.education-services.ru/")
        time.sleep(2)
        
        # Ищем ссылку на личный кабинет
        links = driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            href = link.get_attribute("href")
            if href and ("account" in href or "login" in href or "profile" in href):
                link.click()
                break
        else:
            # Если не нашли по href, ищем по тексту
            account_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Личный') or contains(text(), 'личный')]")
            for elem in account_elements:
                if elem.is_displayed():
                    elem.click()
                    break
        
        time.sleep(2)
        
        # Проверяем что на странице есть форма входа
        assert any(keyword in driver.page_source.lower() 
                  for keyword in ["войти", "вход", "email", "пароль", "login"])
        allure.attach(driver.get_screenshot_as_png(), 
                     name="personal_account_page",
                     attachment_type=allure.attachment_type.PNG)
