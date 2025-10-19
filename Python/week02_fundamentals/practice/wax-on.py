class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append({"title": title, "author": author})

    def get_book_count(self):
        return len(self.books)
    
    def display_books(self):
        for book in self.books:
            print(book["title"])

lib = Library()  
lib.add_book("Yo", "Poo")
lib.add_book("Wax On", "Daniel")

lib.display_books()
print(lib.get_book_count())