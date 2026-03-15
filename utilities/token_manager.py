import requests
import time

class TokenManager:

    token = None
    expiry_time = 0

    @classmethod
    def generate_token(cls):

        url = "https://api.example.com/auth"

        payload = {
            "username": "testuser",
            "password": "test123"
        }

        response = requests.post(url, json=payload)

        data = response.json()

        cls.token = data["access_token"]
        expires_in = data["expires_in"]   # seconds

        cls.expiry_time = time.time() + expires_in


    @classmethod
    def get_token(cls):

        if cls.token is None or time.time() >= cls.expiry_time:
            print("Token expired... generating new token")
            cls.generate_token()

        return cls.token