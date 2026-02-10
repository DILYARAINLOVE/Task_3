import pytest
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Восстановление пароля")
class TestForgotPassword:
    
    @allure.title("Переход на страницу восстановления пароля")
    @pytest.mark.parametrize('driver', ['chrome'], indirect=True)
    def test_go_to_forgot_password_page(self, driver):
        """Проверка перехода на страницу восстановления пароля"""
        driver.get("https://stellarburgers.education-services.ru/")
        time.sleep(3)
        
        # Кликаем на Личный Кабинет - ищем по любому тексту
        try:
            # Пробуем разные варианты поиска
            account_links = driver.find_elements(By.XPATH, "//*[contains(text(), 'Личный') or contains(text(), 'Кабинет') or contains(text(), 'личный') or contains(text(), 'кабинет')]")
            if account_links:
                for link in account_links:
                    if link.is_displayed():
                        link.click()
                        break
        except:
            # Если не нашли, пробуем другой способ
            driver.find_element(By.XPATH, "//header//a[last()]").click()
        
        time.sleep(2)
        
        # Кликаем на Восстановить пароль
        forgot_links = driver.find_elements(By.XPATH, "//*[contains(text(), 'Восстановить') or contains(text(), 'восстановить')]")
        for link in forgot_links:
            if link.is_displayed():
                link.click()
                break
        
        time.sleep(2)
        
        # Проверяем URL
        assert "forgot-password" in driver.current_url
        allure.attach(driver.get_screenshot_as_png(), 
                     name="forgot_password_page",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("Восстановление пароля с вводом email")
    @pytest.mark.parametrize('driver', ['chrome'], indirect=True)
    def test_password_recovery_with_email(self, driver):
        """Проверка восстановления пароля с вводом почты"""
        driver.get("https://stellarburgers.education-services.ru/forgot-password")
        time.sleep(2)
        
        # Вводим email
        inputs = driver.find_elements(By.TAG_NAME, "input")
        for input_field in inputs:
            if input_field.get_attribute("type") in ["text", "email"]:
                input_field.send_keys("test@example.com")
                break
        
        # Нажимаем кнопку Восстановить
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            if "Восстановить" in button.text or "восстановить" in button.text:
                button.click()
                break
        
        time.sleep(2)
        
        # Проверяем что появилось поле для пароля
        password_fields = driver.find_elements(By.XPATH, "//input[@type='password']")
        assert len(password_fields) > 0
    
    @allure.title("Показать/скрыть пароль")
    @pytest.mark.parametrize('driver', ['chrome'], indirect=True)
    def test_show_hide_password(self, driver):
        """Проверка показа/скрытия пароля"""
        driver.get("https://stellarburgers.education-services.ru/reset-password")
        time.sleep(2)
        
        # Ищем поле пароля
        password_field = driver.find_element(By.XPATH, "//input[@type='password']")
        
        # Ищем иконку глаза
        icons = driver.find_elements(By.XPATH, "//div[contains(@class, 'input__icon')]")
        if icons:
            icons[0].click()
            time.sleep(1)
            
            # Проверяем что тип изменился
            new_type = password_field.get_attribute("type")
            assert new_type == "text"
