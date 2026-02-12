from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")  # уточните селектор, если нужно
    RECOVER_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    SHOW_HIDE_ICON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
