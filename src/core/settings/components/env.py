import os

SECRET_KEY = os.getenv('SECRET_KEY')

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

SUPER_USER_LOGIN = os.getenv('SUPER_USER_LOGIN')
SUPER_USER_PASSWORD = os.getenv('SUPER_USER_PASSWORD')