from solution import Library, Book, Author

if __name__ == "__main__":
    library = Library("Tromsø Folkebibliotek")

    knut_hamsun = Author("Knut Hamsun")
    book1 = Book(library, "Markens grøde", knut_hamsun)
    book2 = Book(library, "Pan", knut_hamsun)
    
    george_orwell = Author("George Orwell")
    book3 = Book(library, "1984", george_orwell)

    print("-----------------")
    print(library)
    print("-----------------")
    print(knut_hamsun)
    print("-----------------")
    print(book1)
    print("-----------------")
    print(book2)
    print("-----------------")
    # print(george_orwell)
    # print("-----------------")
    # print(book3)
    # print("-----------------")
    # print(library.books)
