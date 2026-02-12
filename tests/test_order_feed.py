import allure
from pages.order_feed_page import OrderFeedPage

@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Детали заказа")
    def test_order_details_modal(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open()
        order_feed.click_first_order()
        assert order_feed.is_order_modal_open() is True
        order_feed.close_order_modal()
        order_feed.wait_for_element_invisible(order_feed.locators.ORDER_MODAL)

    @allure.title("Счетчики заказов")
    def test_order_counters(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open()
        # Проверяем, что счетчики отображаются и содержат числа
        total = order_feed.get_total_orders_counter()
        today = order_feed.get_today_orders_counter()
        assert total.isdigit()
        assert today.isdigit()
        # Можно также проверить, что они увеличиваются после создания заказа,
        # но это тест с логином — в рамках данного теста просто проверяем наличие
