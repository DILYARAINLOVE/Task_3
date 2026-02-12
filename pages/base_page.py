from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """Ожидание присутствия элемента и его возврат"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Ожидание присутствия всех элементов по локатору"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        """Ожидание кликабельности и клик по элементу"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url_contains(self, text):
        """Ожидание, что URL содержит подстроку"""
        self.wait.until(EC.url_contains(text))

    def wait_for_url_to_be(self, url):
        """Ожидание точного совпадения URL"""
        self.wait.until(EC.url_to_be(url))

    def is_element_present(self, locator):
        """Проверка присутствия элемента без ожидания"""
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False

    def is_element_visible(self, locator):
        """Проверка видимости элемента"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_element_invisible(self, locator):
        """Ожидание исчезновения элемента"""
        self.wait.until(EC.invisibility_of_element_located(locator))
