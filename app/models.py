class Book:
    '''
    Book class to define Book Objects
    '''
    book=[]
    
    def __init__(self,rank,publisher,description,title,book_image,author,amazon_product_url):
        self.rank = rank
        self.publisher = publisher
        self.description = description
        self.author = author
        self.book_image = book_image
        self.title = title
        self.amazon_product_url = amazon_product_url
        
    def save_book(self):
        book.all_books.append(self)
        
        return response