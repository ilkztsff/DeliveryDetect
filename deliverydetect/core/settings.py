from dotenv import load_dotenv
from os import environ


load_dotenv()

BOT_TOKEN = environ['BOT_TOKEN']
HOST = environ['HOST']
WEBHOOK_PATH: str = f'bot/{BOT_TOKEN}'
WEB_SERVER_URL: str = environ['WEB_SERVER_URL']
WEBHOOK_URL: str = f'{WEB_SERVER_URL}{"/" if not WEB_SERVER_URL.endswith("/") else ""}{WEBHOOK_PATH}'

REDIS_HOST: str = environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = int(environ['REDIS_PORT'])
REDIS_PASSWORD: str = environ['REDIS_PASSWORD']

POSTGRES_PORT: str = environ['POSTGRES_PORT']
POSTGRES_USER: str = environ['POSTGRES_USER']
POSTGRES_PASSWORD: str = environ['POSTGRES_PASSWORD']
POSTGRES_DB: str = environ['POSTGRES_DB']

DATABASE_URL = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
