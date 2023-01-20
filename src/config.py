import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'mysql+pymysql://admin:admin@db:3306/autobahn_user?charset=utf8mb4')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

