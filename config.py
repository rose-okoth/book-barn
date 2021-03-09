import os 

class Config:
    
    book_api_base_url =''
    books_api_key = os.environ.get('books_api_key')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True



class ProdConfig(Config):
    
    pass


class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost:5432/books'
    
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}