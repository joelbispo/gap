import requests

from infrastructure.firebase_sdka_admin import api_key
from model.user import user_logged
from utils.api_tools import error_formatter


class LoginController:
    WEB_API_KEY = api_key
    URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

    def login(self, email: str, password: str,  secure_token: bool = True):
        data = {
            "email": email,
            "password": password,
            "secure_token": secure_token
        }

        response = requests.post(self.URL,
                                 params={"key": self.WEB_API_KEY},
                                 data=data)

        if response.ok:
            user_logged.from_dict(response.json())
            return True, "Sucesso"
        else:
            return False, error_formatter(response.json()['error']['message'])
