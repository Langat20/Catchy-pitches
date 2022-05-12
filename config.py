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
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:langat20@localhost/Pitches'
    SQLALCHEMY_DATABASE_URI=os.environ.get('postgres://exagensvhukiqx:8ba9baf6e6b3074f0ab62a40356a5b96c9575e3f3609ebd733bf04c925311500@ec2-107-22-238-112.compute-1.amazonaws.com:5432/d92h52n2rrp8jo')
    
    # SQLALCHEMY_DATABASE_URI ='postgresql://fskxnlnygsjyvr:2bb31532ffa5036dad1d954632c42bc572041281330a7ea25d20b6c52e0a1559@ec2-3-224-164-189.compute-1.amazonaws.com:5432/d9uc8lt63tehf6'


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