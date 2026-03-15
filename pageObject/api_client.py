import requests
from utilities.token_manager import TokenManager

class APIClient:

    @staticmethod
    def get_users():

        token = TokenManager.get_token()

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(
            "https://api.example.com/users",
            headers=headers
        )

        # handle expired token
        if response.status_code == 401:

            TokenManager.generate_token()

            headers["Authorization"] = f"Bearer {TokenManager.get_token()}"

            response = requests.get(
                "https://api.example.com/users",
                headers=headers
            )

        return response