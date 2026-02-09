from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    # Form fields
    EMAIL_INPUT = (By.XPATH, "//input[@name='name' and @type='text']")
    
    # Buttons
    RESET_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль' or @name='Пароль']")
    
    # Password visibility
    PASSWORD_VISIBLE = (By.CSS_SELECTOR, "input[type='text'][name*='пароль']")
    PASSWORD_HIDDEN = (By.CSS_SELECTOR, "input[type='password'][name*='пароль']")
    
    # Navigation
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    
    # Messages
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(), 'Восстановление пароля')]")