import os 
DATABASE_URL='postgresql+psycopg2://oem:m3stravaill3s@localhost/book1'
class Config:
    
    book_api_base_url =''
    books_api_key = os.environ.get('books_api_key')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://oem:m3stravaill3s@localhost/book1'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    
class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://oem:m3stravaill3s@localhost/book1'


class DevConfig(Config):
    
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://oem:m3stravaill3s@localhost/book1'

    DEBUG = True
    ENV = 'development'

config_options = {
'development':DevConfig,
'production':ProdConfig
}