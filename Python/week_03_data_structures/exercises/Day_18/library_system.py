""" Day 18: Individual Project - Library Book Tracker """

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrower = None
    
    def is_available(self):
        return self.borrower is None
    
    def __str__(self):
        status = f"Checked out to {self.borrower}" if self.borrower else "Available"
        return f"{self.title} by {self.author} - {status}"

class Library:
    def __init__(self):
        self.books = {}
        self.id = 1

    def add_book(self, title, author):
        if title in self.books:
            print(f"'{title}' already in library")
            return False
        self.books[title] = Book(title, author, self.id)
        print(f"'{title}' added successfully.")
        self.id += 1
        return True

    def check_out(self, title, borrower):
        book = self.books.get(title)
        if not book:
            print(f"No book found with title: '{title}'.")
            return False
        if not book.is_available():
            print(f"'{title}' is already checked out by {book.borrower}.")
            return False
        book.borrower = borrower
        print(f"'{title}' checked out to {borrower}.")
        return True
    
    def return_book(self, title):
        book = self.books.get(title)
        if not book:
            print(f"No book found with title '{title}'.")
            return False
        if book.is_available():
            print(f"'{title}' is not currently checked out.")
            return False
        borrower = book.borrower
        book.borrower = None
        print(f"'{title}' returned by {borrower}.")
    
    def search_book(self, title):
        book = self.books.get(title)
        if not book:
            print(f"No book found with title '{title}'.")
            return None
        print(book)
        return book
    
    def list_books(self):
        if not self.books:
            print("No books in library.")
            return
        for book in self.books.values():
            print(book)
    
    def display(self):
        print(self.books)
        print(self.checked_out)

lib = Library()    
lib.add_book("Yo Ho Ho", "Santa")
lib.add_book("python", "claude")
lib.add_book("Yo Ho Ho", "Santa")
lib.check_out("python", "John")
lib.search_book("python")
lib.return_book("python")
lib.search_book("python")
lib.list_books()