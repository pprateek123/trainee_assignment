class book:
    def __init__(self,title,author,isbn,genre, availability=True):
        self.title= title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.availability = availability

    def __str__(self):
        return (f'Author name:{self.author},Title: {self.title}, ISBN:{self.isbn},Genre: {self.genre}, availability:{self.availability}')
    

class LibraryCatalog:
    def __init__(self):
        self.books=[]

    def add_book(self,book_obj):
        self.books.append(book_obj)
    
    def get_book_details(self,isbn):
            for book in self.books:
                if book.isbn == isbn:
                    return book
            return ("book not found")
            
           
        
    def borrow_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn and book.availability:
                book.availability = False
                return ('book borrowed')
        return('book not available')
    

cat = LibraryCatalog()
book1 = book("Harry Potter","JK Rowling","1234","Horror")
book2 = book('atomic habits',"James clear","5678","self help")

cat.add_book(book1)
cat.add_book(book2)



print(cat.borrow_book("5678"))
print(cat.get_book_details("5678"))






    

    

            
    