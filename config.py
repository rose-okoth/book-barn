import os 

class Config:
    
    # book_api_base_url ='postgresql+psycopg2://moringaaccess:Access@localhost/test'
    # SQLALCHEMY_DATABASE_URI='postgresql+psycopg2:/moringaaccess:Access@localhost/test1'
    books_api_key = os.environ.get('books_api_key')
    SECRET_KEY = os.environ.get('secret_key')

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2:/moringaaccess:Access@localhost/test1'
    pass


class DevConfig(Config):
    # book_api_base_url ='postgresql+psycopg2://moringaaccess:Access@localhost/test'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringaaccess:Access@localhost/test1'
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}