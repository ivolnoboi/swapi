from pathlib import Path
import requests


class APIRequester:
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
    def get_sw_categories(self):
        response = self.get('/')
        if response:
            return response.json().keys()
        return {}.keys()

    def get_sw_info(self, sw_type):
        response = self.get('/' + sw_type + '/')
        if response:
            return response.text
        return ''


def save_sw_data():
    Path('data').mkdir(exist_ok=True)
    swapi_requester = SWRequester('https://swapi.dev/api')
    categories = swapi_requester.get_sw_categories()
    for category in categories:
        info = swapi_requester.get_sw_info(category)
        with open(f'data/{category}.txt', 'w') as file:
            file.write(info)
