from library_encapsulated import Library, Book, Author

if __name__ == "__main__":
    library = Library("Tromsø Folkebibliotek")
    tove_jansson = Author("Tove Jansson")
    book1 = Book(library, "Mummitrollet 1", tove_jansson)

    # Try to break it

    # library.add_book(tove_jansson)
    # library.books = "Hei"
    print(library._books)
    
    print(library._Library__budget) # Name
