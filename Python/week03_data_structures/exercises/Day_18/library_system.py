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

    def _normalize_title(self, title):
        return title.strip().lower()

    def add_book(self, title, author, isbn):
        if not title.strip() or not author.strip():
            print("Error: Title and author cannot be empty.")
            return False
        
        key = self._normalize_title(title)
        if key in self.books:
            print(f"Error: '{title}' already exists in the library.")
            return False
        
        self.books[key] = Book(title, author, isbn)
        print(f"'{title}' added successfully.")
        return True

    def check_out(self, title, borrower):
        if not title.strip() or not borrower.strip():
            print("Error: Title and borrower name cannot be empty.")
            return False
        
        key = self._normalize_title(title)
        book = self.books.get(key)

        if not book:
            print("Book not found")
            return False
        if not book.is_available():
            print(f"Book is already checked out to {book.borrower}.")
            return False
        
        book.borrower = borrower
        print(f"{book.title} checked out to {borrower}.")
        return True
    
    def return_book(self, title):
        if not title.strip():
            print("Error: Title cannot be empty.")
            return False
        
        key = self._normalize_title(title)
        book = self.books.get(key)

        if not book:
            print("Book not found.")
            return False
        if book.is_available():
            print("Book is not checked out.")
            return False
        
        borrower = book.borrower
        book.borrower = None
        print(f"{book.title} returned successfully by {borrower}.")
        return True
    
    def search_book(self, query):
        if not query.strip():
            print("Error: Search query cannot be empty.")
            return []
        
        results = [book for book in self.books.values() if query.lower() in book.title.lower() or query.lower() in book.author.lower()]

        if not results:
            print("No matching books found.")
        else:
            print("\nSearch results:")
            for b in results:
                print(" ", b)
        return results

    def view_all_books(self):
        if not self.books:
            print("No books in library.")
            return
        for book in self.books.values():
            print(" ", book)
    
    def view_available_books(self):
        available = [b for b in self.books.values() if b.is_available()]
        if not available:
            print("No available books.")
            return
        print("\nAvailable books:")
        for b in available:
            print(" ", b)

    def view_checked_out_books(self):
        checked_out = [b for b in self.books.values() if not b.is_available()]
        if not checked_out:
            print("No books currently checked out.")
            return
        print("\nChecked out books:")
        for b in checked_out:
            print(f" '{b.title}' by {b.author} - borrowed by {b.borrower}.")

def main():
    library = Library()
    menu = """
Library Book Tracker
---------------------
1. Add a book
2. Check out a book
3. Return a book
4. Search books
5. View all books
6. View available book
7. View checked out books
8. Exit
"""

    while True:
        print(menu)
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            isbn = input("Enter ISBN: ").strip()
            library.add_book(title, author, isbn)
        
        elif choice == "2":
            title = input("Enter book title: ").strip()
            borrower = input("Enter borrower's name: ").strip()
            library.check_out(title, borrower)

        elif choice == "3":
            title = input("Enter book title: ").strip()
            library.return_book(title)
        
        elif choice == "4":
            query = input("Enter title or author to search: ").strip()
            library.search_book(query)
        
        elif choice == "5":
            library.view_all_books()
        
        elif choice == "6":
            library.view_available_books()
        
        elif choice == "7":
            library.view_checked_out_books()
        
        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 8.")

if __name__ == "__main__":
    main()
