from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Order list
    ORDER_LIST = (By.XPATH, "//section[contains(@class, 'OrderFeed_orderList__')]")
    ORDER_ITEMS = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem__')]")
    
    # Order details modal
    ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal__')]")
    ORDER_MODAL_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_title__')]")
    ORDER_MODAL_STATUS = (By.XPATH, "//p[contains(@class, 'Modal_status__')]")
    ORDER_MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_close__')]")
    
    # Statistics
    TOTAL_ORDERS = (By.XPATH, "//p[contains(@class, 'OrderFeed_total__')]")
    TODAY_ORDERS = (By.XPATH, "//p[contains(@class, 'OrderFeed_today__')]")
    
    # In progress orders
    IN_PROGRESS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_inProgress__')]")
    IN_PROGRESS_ITEMS = (By.XPATH, ".//li[contains(@class, 'OrderFeed_item__')]")
