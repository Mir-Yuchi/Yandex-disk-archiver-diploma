from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

CLIENT_ID = os.getenv('YANDEX_CLIENT_ID')
CLIENT_SECRET = os.getenv('YANDEX_CLIENT_SECRET')
CALLBACK_URL = 'https://oauth.yandex.ru/verification_code'
YANDEX_BASE_AUTH_URL = 'https://oauth.yandex.ru/authorize'
VK_TOKEN = os.getenv('VK_TOKEN')
VK_VERSION = os.getenv('VK_VERSION')
INSTAGRAM_BASE_URL_API = 'https://api.instagram.com/v11.0/'
INSTAGRAM_BASE_URL_GRAPH = 'https://graph.instagram.com/v11.0/'

