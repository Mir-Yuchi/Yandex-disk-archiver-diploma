import requests
from app.keys import *


def get_token():
    print("Enter to the link te get code \U0001F447 ")
    print(f"{BASE_URL}?response_type=code&client_id={ID}")
    ver_code = input("Enter the code -> ")
    response = requests.post("https://oauth.yandex.ru/token", data={
        'grant_type': 'authorization_code',
        'code': ver_code,
        'client_id': ID,
        'client_secret': SECRET
    })
    if response.status_code != 200:
        print(response.json()["error_description"])
        return
    return response.json()["access_token"]
