from selenium.webdriver.common.by import By


class MainPageLocators:
    # Основные элементы навигации - УПРОЩЕННЫЕ
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[text()='Лента Заказов']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[text()='Личный Кабинет']")
    
    # Разделы конструктора
    BUN_SECTION = (By.XPATH, "//span[text()='Булки']/..")
    SAUCE_SECTION = (By.XPATH, "//span[text()='Соусы']/..")
    FILLING_SECTION = (By.XPATH, "//span[text()='Начинки']/..")
    
    # Ингредиенты
    BUN_ITEM = (By.XPATH, "(//div[contains(@class, 'BurgerIngredient_ingredient')])[1]")
    SAUCE_ITEM = (By.XPATH, "(//div[contains(@class, 'BurgerIngredient_ingredient')])[6]")
    FILLING_ITEM = (By.XPATH, "(//div[contains(@class, 'BurgerIngredient_ingredient')])[11]")
    
    # Конструктор
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    
    # Модальные окна
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_close')]")
    
    # Счетчик
    INGREDIENT_COUNTER = (By.XPATH, ".//div[contains(@class, 'counter_counter__num')]")
