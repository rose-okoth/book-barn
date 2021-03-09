import urllib.request,json
from .models import Book

def configure_request(app):
    global api_key,base_url
    # api_key = app.config['books_api_key']
    # base_url = app.config["book_api_base_url"]

#
