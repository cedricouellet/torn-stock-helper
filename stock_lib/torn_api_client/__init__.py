'''
Module containing the TornApiClient class
'''

import os
import requests


__base_url = os.environ['TORN_API_URL']

class TornApiClient:
    '''
    An HTTP client for the Torn REST API
    '''
    __api_key: str
    
    def __init__(self, api_key: str) -> None:
        '''
        Constructor

            Parameters:
                `api_key`: The API key to use to make requests to the Torn API
        '''
        self.__api_key = api_key

    def get(self, uri: str, params: dict = dict()) -> requests.Response:
        '''
        Send a GET request to the Torn API

            Parameters:
                `uri`: The resource to access
                `params`: (optional) The dictionnary containing URL parameters.

            Returns:
                A `Response` resulting from the GET request.    
        '''

        url_params = ''.join([f'&{key}={value}' for key, value in params.items()])
        
        if not uri.endswith('/'):
            uri = uri + '/'

        return requests.get(f'{__base_url}{uri}?key={self.__api_key}{url_params}')