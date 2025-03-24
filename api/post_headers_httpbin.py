import requests

URL = 'https://httpbin.org/post'

headers = {
    'version': '1.0',
    'authorization': '1234567890',
    'content-type': 'application/json',
    'course': 'Python API',
    'author': 'Leo Bax'

}

response = requests.post(URL, headers=headers)

if response.status_code == 200:
    payload = response.text

    print(payload)
