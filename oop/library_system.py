# Base Class
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


# Derived Class - EBook
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)  # Initialize base class attributes
        self.file_size = file_size       # Unique attribute


# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)  # Initialize base class attributes
        self.page_count = page_count     # Unique attribute


# Composition - Library
class Library:
    def __init__(self):
        self.books = []  # List to store Book, EBook, and PrintBook instances

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            # Detect type of book and print appropriate details
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:  # Regular Book
                print(f"Book: {book.title} by {book.author}")
