class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
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
    
    def __str__(self):
        return f"{self.author.name}: {self.title}"
