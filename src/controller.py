import requests


class ApiHandler:

    def get_data_from_api(self, url):
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()['data']
        else:
            return []
