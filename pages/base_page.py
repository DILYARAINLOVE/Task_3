from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Открыть страницу {url}")
    def open(self, url=""):
        if url:
            full_url = f"https://stellarburgers.education-services.ru{url}"
        else:
            full_url = "https://stellarburgers.education-services.ru/"
        
        print(f"Opening URL: {full_url}")
        self.driver.get(full_url)
        time.sleep(2)  # Даем время на загрузку
        return self
    
    @allure.step("Найти элемент {locator}")
    def find_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            print(f"Элемент не найден: {locator}")
            # Делаем скриншот для отладки
            self.driver.save_screenshot(f"element_not_found_{locator[1][:20]}.png")
            raise
    
    @allure.step("Найти все элементы {locator}")
    def find_elements(self, locator):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            return []
    
    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            time.sleep(0.5)  # Небольшая пауза после клика
            return element
        except Exception as e:
            print(f"Не удалось кликнуть на элемент {locator}: {e}")
            raise
    
    @allure.step("Ввести текст '{text}' в элемент {locator}")
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return element
    
    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    @allure.step("Проверить, что элемент {locator} видим")
    def is_element_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Сделать скриншот")
    def take_screenshot(self, name="screenshot"):
        filename = f"{name}_{int(time.time())}.png"
        self.driver.save_screenshot(filename)
        print(f"Скриншот сохранен: {filename}")
        return filename
