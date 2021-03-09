import urllib.request,json
from .models import Book

def configure_request(app):
    global api_key,base_url
    # api_key = app.config['books_api_key']
    # base_url = app.config["book_api_base_url"]

#
import requests
from flask import Flask
from flask import render_template
api_key = '67786b6df7f94b37b826f0360c99094c'
url = f'https://newsapi.org/v2/sources?apiKey={api_key}'
response = requests.get(url) 
app = Flask(__name__)
@app.route('/')
def home():
    sources = []
    for data in response.json()['sources']:
        sources.append(data)
    return render_template('test.html', sources=sources)
if __name__ == '__main__':
    app.run(debug=True)