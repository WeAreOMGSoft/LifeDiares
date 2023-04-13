import requests
import json

class API:
    def __init__(self):
        self.url = ''
        self.session = requests.Session()

    def login(self, user_id: int) -> json:
        params = {"user_id": user_id}
        return self.session.get(url=self.url + '/login', params=params).json()

    def register(self, user_id: int) -> json:
        params = {"user_id": user_id}
        return self.session.get(url=self.url + '/register', params=params).json()
