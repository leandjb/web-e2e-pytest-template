import requests

# URL: str = 'https://httpbin.org/get?name=leandro&age=31'      # URL + Query String\

URL = 'https://httpbin.org/get'                                 # URL
parameters = {
    'name': 'Leandro',
    'age': 31,
    'email': 'info@demo.com'
}

response = requests.get(URL, params=parameters)

if response.status_code == 200:
    payload = response.json()
    parameters = payload['args']

    print(parameters['name'])
    print(parameters['age'])
    print(parameters['email'])
    print(URL)