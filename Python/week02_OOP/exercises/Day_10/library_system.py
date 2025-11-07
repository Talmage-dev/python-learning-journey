""" Day 10: Object-Oriented Programming (OOP) - Part 1 """

# Practice Exercise 4: Library system

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def get_info(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
    
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if title == book.title:
                return book
        return None
    
    def display_books(self):
        print("Library Inventory:")
        for book in self.books:
            print(f"{book.title} by {book.author}. isbn: {book.isbn}")

# Test
library = Library()
library.add_book(Book("Yo", "Me", 321))
library.add_book(Book("Python for Beginners", "Claude", 987))
library.find_book("Yo")
library.find_book("What's up")
library.display_books()