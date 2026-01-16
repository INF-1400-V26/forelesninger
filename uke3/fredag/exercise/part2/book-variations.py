"""Løsningsforslag til siste punkt i Del 2 av oppgaven
Book1 løser oppgaven uten arv
Book2 løser oppgaver med arv (men uten bruk av abstrakt baseklasse)

Det finnes andre måter å gjøre dette på.
"""
from solution_customer import Library, Author

class Book1:
    def __init__(self, library, title, author, loan_period=28):
        self.library = library
        self.library.books.append(self)
        self.title = title
        self.author = author
        self.author.books.append(self)

        self.available = True
        self.loaned_by = None
        self.loan_period = loan_period # lagt til

    def loan(self, customer): 
         if not self.loan_period: # lagt til
             return False 
         self.available = False
         self.loaned_by = customer
         return True # lagt til

    def return_loan(self): 
        if not self.loan_period: # lagt til
            return False 
        self.available = True
        self.loaned_by = None
        return True # lagt til
    
    def __str__(self):
        return f"{self.author.name}: {self.title}"
    
class Customer: 
    def __init__(self, library, name):
        self.library = library
        self.name = name
        self.loans = []
    
    def loan_book(self, book):
        if book.available:
            if book.loan(self): # lagt til
                self.loans.append(book)
            return
        print("Could not loan", book.title)
    
    def return_book(self, book):
        if book in self.loans:
            if book.return_loan():
                self.loans.remove(book)
            return
        print("Could not return", book.title)


    def loans_by_title(self):
        return [book.title for book in self.loans]
    
class Book2: # standard loans
    def __init__(self, library, title, author):
        self.library = library
        self.library.books.append(self)
        self.title = title
        self.author = author
        self.author.books.append(self)

        self.available = True
        self.loaned_by = None
        self.loan_period = 28 # endret her

    def loan(self, customer): 
         if not self.loan_period: 
             return False 
         self.available = False
         self.loaned_by = customer
         return True 

    def return_loan(self): 
        if not self.loan_period: 
            return False 
        self.available = True
        self.loaned_by = None
        return True 
    
    def __str__(self):
        return f"{self.author.name}: {self.title}"

class BookQuickLoan(Book2):
    def __init__(self, library, title, author):
        super().__init__(library, title, author)
        self.loan_period = 7

class BookNoLoan(Book2):
    def __init__(self, library, title, author):
        super().__init__(library, title, author)
        self.loan_period = None
        self.available = False
    
    def loan(self,customer):
        print("Book cannot be loaned")
        return False
    
    def return_loan(self,customer):
        print("Book cannot be loaned, no return possible")
        return False

if __name__ == "__main__":
    library = Library("UiT Kultur og samfunnsfag")
    knut = Author("Knut Hamsun")
    
    b1 = Book1(library, "Sult", knut,7)
    print(b1.loan_period)
    
    b2 = Book2(library, "Den gaadefulde", knut)
    print(b2.loan_period)

    b3 = BookQuickLoan(library, "Victoria", knut)
    print(b3.loan_period)

    b4 = BookNoLoan(library, "Snorre Saga", Author("Snorre"))
    print(b4.loan_period)

    booklist = [b2,b3,b4]

    customer = Customer(library, "Anne B")

    for book in booklist:
        customer.loan_book(book)
    print(customer.loans_by_title())