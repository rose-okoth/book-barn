import urllib.request,json
# from .models import Book

def configure_request(app):
    global api_key,base_url
    # api_key = app.config['books_api_key']
    # base_url = app.config["book_api_base_url"]
    # base_url = app.config['QUOTE_API_BASE_URL']

def get_quote():
    get_quote_url ='http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(get_quote_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

    return get_quote_response
