from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    ORDER_CARD = (By.XPATH, "//div[contains(@class, 'OrderHistory')] | //div[contains(@class, 'OrderCard')]")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")
    MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_close')]")
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за всё время:')]/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p")
