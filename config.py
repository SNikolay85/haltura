import os
from dotenv import load_dotenv

load_dotenv()

REAL_DB = os.getenv('REAL_DB')
PG_USER = os.getenv('POSTGRES_USER')
PG_PASSWORD = os.getenv('POSTGRES_PASSWORD')
PG_HOST = os.getenv('POSTGRES_HOST')
PG_PORT = os.getenv('POSTGRES_PORT')

SALT = os.getenv('SALT')

TOKEN_TBOT = os.getenv('TOKEN_TBOT')
SERVICE_KEY = os.getenv('SERVICE_KEY')

TOKEN_HH = os.getenv('TOKEN_HH')


NEW_TBOT = os.getenv('NEW_TBOT')
BASE_SITE = os.getenv('BASE_SITE')
ADMIN_ID = os.getenv('ADMIN_ID')
