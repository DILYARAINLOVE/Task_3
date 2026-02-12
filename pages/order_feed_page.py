from locators.order_feed_locators import OrderFeedPageLocators
from .base_page import BasePage

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedPageLocators

    def open(self):
        self.driver.get("https://stellarburgers.education-services.ru/feed")

    def click_first_order(self):
        orders = self.find_elements(self.locators.ORDER_CARD)
        if orders:
            orders[0].click()

    def is_order_modal_open(self):
        return self.is_element_visible(self.locators.ORDER_MODAL)

    def close_order_modal(self):
        self.click_element(self.locators.MODAL_CLOSE)

    def get_total_orders_counter(self):
        # Возвращает текст счетчика "Выполнено за всё время"
        element = self.find_element(self.locators.TOTAL_ORDERS_COUNTER)
        return element.text

    def get_today_orders_counter(self):
        element = self.find_element(self.locators.TODAY_ORDERS_COUNTER)
        return element.text
