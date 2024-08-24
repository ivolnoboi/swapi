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
            return None
        else:
            return response


class SWRequester(APIRequester):
    def get_sw_categories(self):
        pass

    def get_sw_info(self, sw_type):
        pass


def save_sw_data():
    pass


apr = APIRequester('https://swapi.dev/')
print(apr.get('api/'))
