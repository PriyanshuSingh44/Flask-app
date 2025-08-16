import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # Email configauration
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 8025
    MAIL_USE_TLS = False 
    MAIL_USE_SSL = False
    MAIL_USERNAME = None 
    MAIL_PASSWORD = None 
    ADMINS = ['priyanshu3303@gmail.com']
    POSTS_PER_PAGE = 25