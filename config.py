import os 

class Config:
    
    book_api_base_url =''
    books_api_key = os.environ.get('books_api_key')
    secret_key = os.environ.get('secret_key')


class ProdConfig(Config):
    
    pass


class DevConfig(Config):
    
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}