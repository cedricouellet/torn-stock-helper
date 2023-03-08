import os
import requests


BASE_URL = os.environ['TORN_API_URL']

class TornApi:
    __api_key: str
    
    def __init__(self, api_key: str) -> None:
        self.__api_key = api_key

    def get(self, uri: str, params: dict):
        url_params = ''.join([f'&{key}={value}' for key, value in params.items()])
        
        if not uri.endswith('/'):
            uri = uri + '/'

        return requests.get(f'{BASE_URL}{uri}?key={self.__api_key}{url_params}')