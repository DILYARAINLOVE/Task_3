class TestData:
    BASE_URL = "https://stellarburgers.nomoreparties.site"
    
    # Тестовые данные для разных окружений
    TEST_EMAILS = {
        "valid": "test_user@example.com",
        "invalid": "not_a_user@example.com"
    }
    
    TEST_PASSWORDS = {
        "valid": "TestPassword123",
        "invalid": "WrongPassword"
    }
    
    TEST_NAMES = {
        "valid": "Test User",
        "invalid": ""
    }
    
    # URL эндпоинтов
    ENDPOINTS = {
        "main": "/",
        "login": "/login",
        "register": "/register",
        "forgot_password": "/forgot-password",
        "reset_password": "/reset-password",
        "profile": "/account/profile",
        "order_history": "/account/order-history",
        "order_feed": "/feed"
    }