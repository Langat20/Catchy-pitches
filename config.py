import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY =os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI='postgres://uodkpmzmpekuie:2d7b6c2a9707134d6e86aa26322aca70b9feceaa7c15f44060fc6d4b44ee5098@ec2-34-236-94-53.compute-1.amazonaws.com:5432/d2bhrr2jouefpg'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:langat20@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS=True
    MAIL_USERNAME='kipkuruie7.lang@gmail.com'
    MAIL_PASSWORD='evanskip2015'
    SUBJECT_PREFIX='Pitches'
    SENDER_EMAIL='kipkuruie7.lang@gmail.com'

    
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    uri = os.getenv("DATABASE_URL")  # or other relevant config var
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI=uri

DEBUG = True



class TestConfig(Config):
    '''
    Test
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:langat20@localhost/pitches'


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig,
}