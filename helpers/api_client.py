import requests
from typing import Dict, Optional


class ApiClient:
    # Используем правильный URL для тестового окружения
    BASE_URL = "https://stellarburgers.education-services.ru/api"
    
    def __init__(self):
        self.session = requests.Session()
        self.access_token = None
    
    def create_user(self, email: str, password: str, name: str) -> Dict:
        """Создание пользователя через API"""
        url = f"{self.BASE_URL}/auth/register"
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        
        print(f"Creating user with email: {email}")
        response = self.session.post(url, json=payload)
        
        # Если получаем ошибку, логируем детали
        if response.status_code != 200:
            print(f"API Error {response.status_code}: {response.text}")
            response.raise_for_status()
        
        data = response.json()
        
        if "accessToken" in data:
            self.access_token = data["accessToken"]
        
        return data
    
    def delete_user(self, access_token: Optional[str] = None) -> bool:
        """Удаление пользователя через API"""
        if not access_token and not self.access_token:
            return False
        
        token = access_token or self.access_token
        url = f"{self.BASE_URL}/auth/user"
        
        headers = {"Authorization": f"Bearer {token}"}
        response = self.session.delete(url, headers=headers)
        
        return response.status_code in [200, 202]
    
    def login(self, email: str, password: str) -> Dict:
        """Логин пользователя через API"""
        url = f"{self.BASE_URL}/auth/login"
        payload = {
            "email": email,
            "password": password
        }
        
        response = self.session.post(url, json=payload)
        if response.status_code != 200:
            print(f"Login API Error {response.status_code}: {response.text}")
        
        response.raise_for_status()
        data = response.json()
        
        if "accessToken" in data:
            self.access_token = data["accessToken"]
        
        return data