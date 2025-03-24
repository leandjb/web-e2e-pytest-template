import requests

URL = 'https://httpbin.org/cookies'

cookie = {
    'sessions': 'abc123',
    'name': 'Cody',
    'email': 'info@codigofacilito.com'
}

response = requests.get(url=URL, cookies=cookie)

if response.status_code == 200:
    print(response.json())
