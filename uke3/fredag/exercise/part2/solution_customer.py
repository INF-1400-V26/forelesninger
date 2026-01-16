class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.customers = [] # lagt til
    
    def __str__(self):
        return self.name  

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        return f"{self.name}: {[book.title for book in self.books]}"

class Book:
    def __init__(self, library, title, author):
        self.library = library
        self.library.books.append(self)
        self.title = title
        self.author = author
        self.author.books.append(self)

        # lagt til
        self.available = True
        self.loaned_by = None

    def loan(self, customer): # lagt til
         self.available = False
         self.loaned_by = customer

    def return_loan(self): # lagt til
        self.available = True
        self.loaned_by = None
    
    def __str__(self):
        return f"{self.author.name}: {self.title}"

class Customer: # lagt til hele klassen
    def __init__(self, library, name):
        self.library = library
        self.name = name
        self.loans = []
    
    def loan_book(self, book):
        if book.available:
            book.loan(self)
            self.loans.append(book)
            return
        print("Could not loan", book.title)
    
    def return_book(self, book):
        if book in self.loans:
            book.return_loan()
            self.loans.remove(book)
            return
        print("Could not return", book.title)


    def loans_by_title(self):
        return [book.title for book in self.loans]

