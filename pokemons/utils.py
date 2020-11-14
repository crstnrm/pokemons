import requests


def generate_request(url, **kwargs):
    response = requests.get(url, **kwargs)

    if response.status_code == 200:
        return response.json()
