import os
import sys

from sayhello import app

# basic config
DEBUG = True
HOST = '0.0.0.0'
PORT = '5000'

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')

SECRET_KEY = 'secret string'
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', dev_db)
SQLALCHEMY_TRACK_MODIFICATIONS = False


