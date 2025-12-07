class Book:
    """
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The publication year of the book.

    Magic Methods:
        __init__: Initializes a Book instance.
        __del__: Prints "Deleting (title of the book)" when the object is deleted.
        __str__: Returns "(title) by (author), published in (year)".
        __repr__: Returns "Book('title', 'author', year)".
    """

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
