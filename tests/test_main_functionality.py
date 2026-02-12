import allure
from pages.main_page import MainPage

@allure.feature("Основной функционал")
class TestMainFunctionality:

    @allure.title("Переход в конструктор")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        # Сначала переходим в ленту заказов, чтобы проверить возврат в конструктор
        main_page.click_order_feed()
        main_page.wait_for_url_contains("feed")
        main_page.click_constructor()
        main_page.wait_for_url_to_be("https://stellarburgers.education-services.ru/")
        assert main_page.get_current_url() == "https://stellarburgers.education-services.ru/"

    @allure.title("Переход в ленту заказов")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_feed()
        main_page.wait_for_url_contains("feed")
        assert "feed" in main_page.get_current_url()

    @allure.title("Модальное окно ингредиента")
    def test_ingredient_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient(0)
        assert main_page.is_modal_open() is True
        main_page.close_modal()
        main_page.wait_for_modal_closed()
        # Дополнительная проверка, что модальное окно закрыто
        assert main_page.is_modal_open() is False

    @allure.title("Счетчик ингредиента")
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        counter_value = main_page.get_ingredient_counter_value(0)
        assert isinstance(counter_value, int)
        assert counter_value >= 0
