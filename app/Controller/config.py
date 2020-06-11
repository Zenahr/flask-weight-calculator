import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = os.environ.get('DEBUG') or True
    HOST= os.environ.get('HOST') or "192.168.1.63"
    PORT= os.environ.get('PORT') or "7979"
    TEMPLATES_PATH=os.path.join(os.getcwd(), "View")
    DATABASE='databaseBig.db'