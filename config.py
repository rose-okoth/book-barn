import os 

class Config:
    QUOTE_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'

    book_api_base_url =''
    books_api_key = os.environ.get('books_api_key')
    secret_key = os.environ.get('secret_key')
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    
    pass


class DevConfig(Config):
    
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}