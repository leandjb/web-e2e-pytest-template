import requests
import json
from typing import List, Dict

URL = 'https://randomuser.me/api/'
PARAMS = {
    'results': 10
}

def fetch_random_users(url: str) -> List[Dict]:
    try:
        response = requests.get(url, params=PARAMS)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json().get('results', [])
    except requests.RequestException as e:
        print(f"Error: Network issue occurred - {e}")
        return []
    except json.JSONDecodeError:
        print("Error: Unable to decode JSON response")
        return []


def print_user_names(users: List[Dict]) -> None:
    for user in users:
        name = user.get('name', {})
        first_name = name.get('first')
        last_name = name.get('last')

        location = user.get('location', {})
        country = location.get('country')
        
        print(f'{last_name}, {first_name} ({country})')


if __name__ == "__main__":
    users = fetch_random_users(URL)
    print_user_names(users)
