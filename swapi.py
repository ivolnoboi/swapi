"""This module is used for sending requests, getting response from
The Star Wars API and writing received information to a file.
"""


from pathlib import Path
import requests


class APIRequester:
    """The class for sending requests to a server."""

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, url):
        try:
            response = requests.get(self.base_url + url)
            response.raise_for_status()
        except requests.RequestException:
            print('Возникла ошибка при выполнении запроса')
        else:
            return response


class SWRequester(APIRequester):
    """The class for getting information from The Star Wars API."""

    def get_sw_categories(self):
        """Get existing categories from The Star Wars API."""
        response = self.get('/')
        if response:
            return response.json().keys()
        return {}.keys()

    def get_sw_info(self, sw_type):
        """Get information about a specific category."""
        response = self.get('/' + sw_type + '/')
        if response:
            return response.text
        return ''


def save_sw_data():
    """Save information about all categories on The Star Wars to files."""
    Path('data').mkdir(exist_ok=True)

    swapi_requester = SWRequester('https://swapi.dev/api')
    categories = swapi_requester.get_sw_categories()

    for category in categories:
        info = swapi_requester.get_sw_info(category)
        with open(f'data/{category}.txt', 'w') as file:
            file.write(info)
