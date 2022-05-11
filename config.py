import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = ('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:langat20@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME ='kipkuruie7.lang@gmail.com'
    MAIL_PASSWORD ='evanskip2015'
    SUBJECT_PREFIX = 'Pitches'
    SENDER_EMAIL = 'kipkuruie7.lang@gmail.com'
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:langat20@localhost/Pitches'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:langat20@localhost/pitches_test'


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:langat20@localhost/pitches'
    DEBUG = True


 
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}