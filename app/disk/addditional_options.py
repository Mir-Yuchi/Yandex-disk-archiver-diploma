from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


class PlusFunction:
    @staticmethod
    def from_vk(is_token):
        resources = 'https://cloud-api.yandex.net/v1/disk/resources/'
        token = '34e9587d34e9587d34e9587de337fbbcb8334e934e9587d50e929d9a48d0e9356ae13c5'
        version = 5.131
        domain = input("Enter vk id or username --> ")
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain
                                }).json()
        url = response['response']['items'][1]['attachments'][0]['photo']['sizes'][6]['url']
        print("HERE IS LINK: -> ", url)
        path = input("Enter PATH\U000023E9: ")
        publish = requests.post(resources + f"upload?url={url}&path=%2F{path}",
                                headers={'Authorization': f'OAuth {is_token}'}).json()
        print(publish)
        if 'description' in publish:
            print(publish['description'])
        else:
            print("Successfully downloaded :)")
