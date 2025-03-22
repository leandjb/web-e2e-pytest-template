import requests

URL = 'https://httpbin.org/post'

data = {
    'username': 'Leandb',
    'password': 'c0ntr4s3n4',
    'email': 'info@simetrik.org'
}

response = requests.post(URL, data=data)

if response.status_code == 200:
    payload = response.json()

    print(response.status_code)
    print(response.url)
    print(response.text)
    print(payload)
