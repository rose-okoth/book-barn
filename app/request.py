import requests,json
import urllib.request,json
from .models import Book

# Getting api key
api_key = None

#Getting the book base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['BOOKS_API_KEY']
    base_url = app.config['BOOK_API_BASE_URL']

def get_books():
    '''
    Function that gets the json response to our url request
    '''
    get_books_url = base_url.format(api_key)
    
    get_books_response = requests.get(get_books_url).json()
        
    book_results = None
    # import pdb;pdb.set_trace()
        
    if get_books_response['results']['books']:
        book_results_list = get_books_response['results']['books']   
        book_results = process_results(book_results_list)
            
            
    return book_results

def process_results(book_list):
    '''
    Function that processes the movie result and transforms them to a list of Objects
    
    Args:
        book_list:A list of dictionaries that contain book details
        
    Returns:
        book_results:A list of book objects
        
    '''
    
    book_results = []
    
    for book_item in book_list:
        rank = book_item.get('rank')
        publisher = book_item.get('publisher')
        description = book_item.get('description')
        author = book_item.get('author')
        book_image = book_item.get('book_image')
        title = book_item.get('title')
        amazon_product_url = book_item.get('amazon_product_url')
        
        
        if rank:
            book_object = Book(rank,publisher,description,author,book_image,title,amazon_product_url)
            book_results.append(book_object)
            
    return book_results        
