class Library:
    def __init__(self, name):
        self.name = name
        self._books = []
        self.__budget = 1999 # private field, gets name mangled

    def _validate_new_book(self, book): # internal method
        if not isinstance(book, Book):
            return False
        if book.title.strip() == "":
            return False
        if book.author.name.strip() == "":
            return False
        author_name =  book.author.name.split(" ")
        if len(author_name) < 2:
            return False
        return True
    
    def add_book(self, book):
        if not self._validate_new_book(book):
            raise Exception(f"Book: '{book}' does not satisfy library criteria")
        self._books.append(book)
    
    def remove_book_by_title(self,title):
        for book in self._books:
            if book.title == title:
                self._books.remove(book)

    @property # getter
    def books(self):
        return self._books.copy()
    
    @books.setter # setter
    def books(self,value):
        raise PermissionError("Use add_book or remove_book_by_title methods")

    def all_book_titles(self):
        return [book.title for book in self._books]

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
        self.title = title
        self.author = author
        self.author.books.append(self)
        self.library.add_book(self) # moved to the last line

    
    def __str__(self):
        return f"{self.author.name}: {self.title}"
