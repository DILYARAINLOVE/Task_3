import random
import string
from datetime import datetime


class DataGenerator:
    @staticmethod
    def generate_email():
        """Генерация случайного email"""
        username = ''.join(random.choices(string.ascii_lowercase, k=8))
        domain = ''.join(random.choices(string.ascii_lowercase, k=6))
        return f"{username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}@{domain}.com"
    
    @staticmethod
    def generate_password():
        """Генерация случайного пароля"""
        letters = string.ascii_letters
        digits = string.digits
        return ''.join(random.choices(letters + digits, k=10))
    
    @staticmethod
    def generate_name():
        """Генерация случайного имени"""
        names = ['Иван', 'Мария', 'Алексей', 'Екатерина', 'Дмитрий', 'Ольга']
        surnames = ['Иванов', 'Петрова', 'Сидоров', 'Кузнецова', 'Смирнов']
        return f"{random.choice(names)} {random.choice(surnames)}"