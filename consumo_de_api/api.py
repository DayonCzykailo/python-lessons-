import requests

class Api():
    def __init__(self, url):
        self.url = url

    def get(self):
        response = requests.get(self.url)
        return response.json()

    def post(self, data):
        response = requests.post(self.url, data)
        return response.json()

    def put(self, data):
        response = requests.put(self.url, data)
        return response.json()

    def delete(self):
        response = requests.delete(self.url)
        return response.json()