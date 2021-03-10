import os 

class Config:
    
    BOOK_API_BASE_URL ='https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key={}'
    BOOKS_API_KEY = os.environ.get('BOOKS_API_KEY')
    secret_key = os.environ.get('secret_key')

class ProdConfig(Config):
    
    pass


class DevConfig(Config):
    
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}