from pages.base_page import BasePage
from locators.profile_locators import ProfilePageLocators
import allure


class ProfilePage(BasePage):
    
    @allure.step("Открыть страницу профиля")
    def open_profile_page(self):
        self.open("/account/profile")
        return self
    
    @allure.step("Перейти в раздел 'Профиль'")
    def go_to_profile(self):
        self.click(ProfilePageLocators.PROFILE_LINK)
        return self
    
    @allure.step("Перейти в раздел 'История заказов'")
    def go_to_order_history(self):
        self.click(ProfilePageLocators.ORDER_HISTORY_LINK)
        return self
    
    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)
        return self
    
    @allure.step("Проверить, что открыта страница профиля")
    def is_profile_page(self):
        return "/account/profile" in self.get_current_url()
    
    @allure.step("Проверить, что открыта история заказов")
    def is_order_history_page(self):
        return "/account/order-history" in self.get_current_url()
    
    @allure.step("Получить количество заказов в истории")
    def get_order_count(self):
        orders = self.find_elements(ProfilePageLocators.ORDER_ITEMS)
        return len(orders)
    
    @allure.step("Получить информацию о последнем заказе")
    def get_last_order_info(self):
        orders = self.find_elements(ProfilePageLocators.ORDER_ITEMS)
        if orders:
            first_order = orders[0]
            number = first_order.find_element(*ProfilePageLocators.ORDER_NUMBER).text
            status = first_order.find_element(*ProfilePageLocators.ORDER_STATUS).text
            return {"number": number, "status": status}
        return None
    
    @allure.step("Получить текущее имя пользователя")
    def get_current_name(self):
        element = self.find_element(ProfilePageLocators.NAME_INPUT)
        return element.get_attribute("value")
    
    @allure.step("Получить текущий email пользователя")
    def get_current_email(self):
        element = self.find_element(ProfilePageLocators.EMAIL_INPUT)
        return element.get_attribute("value")