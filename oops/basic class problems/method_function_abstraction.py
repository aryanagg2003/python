# Question:

# Imagine you are designing a system to model a library. Create a class called Book with the following attributes: title, author, and publication_year. 
# Implement methods to get and set each of these attributes. Additionally, include a method called display_info() that prints the information about
# the book.

# Create another class called Library that represents a collection of books. Implement methods to add a book to the library, remove a book, and 
# display information about all the books in the library.

# Demonstrate the usage of these classes by creating instances of the Book and Library classes, adding books to the library, removing books, and 
# displaying the information.

class Book:
    def __init__(self,title,author,publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_publication_year(self):
        return self.publication_year
    
    def set_title(self,title):
        self.title = title

    def set_author(self,author):
        self.author = author

    def set_publication_year(self,publication_year):
        self.publication_year = publication_year

    def display_info(self):
        print(f"Information of books Title : {self.title} Author : {self.author} Publicaton Year : {self.publication_year}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        print("Book added")

    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book)
            print("Book removed")
        else:
            print("Book Not present")

    def display_book(self):
        for book in self.books:
            book.display_info()

book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

library = Library()

library.add_book(book1)
library.add_book(book2)

library.display_book()

library.remove_book(book1)

library.display_book()