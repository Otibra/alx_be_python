class Book:
    def __init__(self, title, author):
        self.title = title            # public
        self.author = author          # public
        self._is_checked_out = False  # private (convention)

    def check_out(self):
        """Mark the book as checked out if it is available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book to the library if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private list of Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f"'{title}' checked out successfully."
                else:
                    return f"'{title}' is already checked out."
        return f"Book titled '{title}' not found."

    def return_book(self, title):
        """Return a checked-out book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f"'{title}' returned successfully."
                else:
                    return f"'{title}' was not checked out."
        return f"Book titled '{title}' not found."

    def list_available_books(self):
        """Return a list of titles of all available books."""
        return [book.title for book in self._books if book.is_available()]
