from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

CLIENT_ID = os.getenv('YANDEX_CLIENT_ID')
CLIENT_SECRET = os.getenv('YANDEX_CLIENT_SECRET')
CALLBACK_URL = os.getenv('YANDEX_CALLBACK_URL')
YANDEX_BASE_AUTH_URL = os.getenv('YANDEX_BASE_AUTH_URL')
VK_TOKEN = os.getenv('VK_TOKEN')
VK_VERSION = os.getenv('VK_VERSION')
