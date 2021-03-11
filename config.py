import os 
    
class Config:
    
    BOOK_API_BASE_URL ='https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key={}'
    BOOKS_API_KEY = os.environ.get('books_api_key')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    
class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    DEBUG = True
    ENV = 'development'

config_options = {
'development':DevConfig,
'production':ProdConfig
}