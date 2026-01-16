from solution_customer import Library, Customer, Book, Author

if __name__ == "__main__":
    library = Library("UiT Kultur og samfunnsfag")
    knut = Author("Knut Hamsun")
    markens_grode = Book(library,"Markens Grøde", knut)

    anne = Customer(library, "Anne B")
    gunnar = Customer(library, "Gunnar H")

    anne.loan_book(markens_grode)
    print(anne.loans_by_title())

    gunnar.loan_book(markens_grode)
    print(gunnar.loans_by_title())
    
    # anne.return_book(markens_grode)
    # print(anne.loans_by_title())
    # anne.return_book(markens_grode)