import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = os.environ.get('DEBUG') or True
    TEMPLATES_PATH=os.path.join(os.getcwd(), "View")
    DATABASE='../Model/databaseBig.db'
    FLASK_ENV='development'