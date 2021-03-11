from flask import render_template
import requests
from flask import Flask
from . import main

# Views
# @main.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     title = 'Home'
#     return render_template('index.html', title=title)



api_key = '0KY0nS7PPPmkuZZwEcAazTcv3Ncb36cO'
url = f'https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key={api_key}'
response = requests.get(url) 
app = Flask(__name__)
@main.route('/')
def home():
    books = []
    for data in response.json()['results']['books']:
        books.append(data)
        
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)    