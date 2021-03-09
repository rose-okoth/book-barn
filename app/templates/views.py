import requests
from flask import Flask
from flask import render_template


api_key = ''
url = f'https://?apiKey={api_key}'
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