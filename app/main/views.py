from flask import render_template,request
from . import main
from ..request import get_books

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
  
    title = 'Home'
    return render_template('index.html', title=title)

@main.route('/library/')
def library():
    '''
    View library page function that returns library page and its
    data
    '''
    my_books = get_books()
    
    return render_template('library.html',books = my_books)
