import requests
from getpass import getpass

URL = 'https://httpbin.org/basic-auth/gakpo/cody'

password = getpass('Enter password:')

session = requests.Session()
session.auth = ('gakpo', password)

response = session.get(url=URL)

if response.status_code == 200:
    print(response.json())

if response.status_code == 401:
    print("Authentication failed")
