import requests

URL = 'https://httpbin.org/delete'

response = requests.delete(URL,
                        params={'name': 'Leandro'},
                        headers={'version': '3.0'},
                        data={'id': 1})

if response.status_code == 200:
    print(response.status_code)
    print(response.text)

else:
    print(response.status_code)
