from selenium.webdriver.common.by import By


class ProfilePageLocators:
    # Navigation
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    
    # Form fields
    NAME_INPUT = (By.XPATH, "//input[@name='name' and @value]")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name' and @type='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    
    # Buttons
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    CANCEL_BUTTON = (By.XPATH, "//button[text()='Отмена']")
    
    # Order history
    ORDER_ITEMS = (By.XPATH, "//div[contains(@class, 'OrderHistory_list__')]//li")
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'OrderHistory_number__')]")
    ORDER_STATUS = (By.XPATH, ".//p[contains(@class, 'OrderHistory_status__')]")