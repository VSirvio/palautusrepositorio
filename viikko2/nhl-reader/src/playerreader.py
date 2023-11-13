import requests

class PlayerReader:
    def __init__(self, url):
        self.__url = url

    def get_players(self):
        return requests.get(self.__url).json()
