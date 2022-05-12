from distutils.debug import DEBUG
import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY =os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL').replace("://","ql://", 1)

    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:langat20@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    SUBJECT_PREFIX='Pitches'
    SENDER_EMAIL='kipkuruie7.lang@gmail.com'
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL').replace("://","ql://", 1)

DEBUG=True

    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:langat20@localhost/Pitches'
    # SQLALCHEMY_DATABASE_URI=os.environ.get('ostgres://exagensvhukiqx:8ba9baf6e6b3074f0ab62a40356a5b96c9575e3f3609ebd733bf04c925311500@ec2-107-22-238-112.compute-1.amazonaws.com:5432/d92h52n2rrp8jo')
    
   


class TestConfig(Config):
    
   SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL').replace("://","ql://", 1)

    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:langat20@localhost/pitches_test'


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL').replace("://","ql://", 1)

    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:langat20@localhost/pitches'
    
    # DEBUG = True


 
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}