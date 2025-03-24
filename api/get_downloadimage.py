import requests

URL = 'http://codigofacilito.com/images/cody'

response = requests.get(URL, stream=True)

if response.status_code == 200:
    with open('images/cody.png', 'wb') as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)
