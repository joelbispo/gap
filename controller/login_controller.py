import requests


from model.user import User
from utils.api_tools import error_formatter



class LoginController:
    WEB_API_KEY = "AIzaSyDoJWnoD_jj4RcrB_Ft7PprrUJoHfIbP80"
    URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
    _user = None

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
            self._user = User().from_dict(response.json())
            return self._user, "Sucesso"
        else:
            return self._user, error_formatter(response.json()['error']['message'])

    def logout(self):
        self._user = None

    def get_user_logged(self):
        return self._user