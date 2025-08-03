class Book:
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        _is_checked_out (bool): A private attribute indicating if the book is checked out.
    """
    def __init__(self, title, author):
        """Initializes a new Book instance."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is not checked out, False otherwise."""
        return not self._is_checked_out

    def __str__(self):
        """Returns a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}"

class Library:
    """
    Manages a collection of Book objects.

    Attributes:
        _books (list): A private list to store Book instances.
    """
    def __init__(self):
        """Initializes a new Library instance with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Adds a new Book object to the library's collection."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Error: Only Book objects can be added to the library.")

    def check_out_book(self, title):
        """Checks out a book by its title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: {title}")
                return
        print(f"Error: '{title}' is not available or does not exist.")

    def return_book(self, title):
        """Returns a book by its title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: {title}")
                return
        print(f"Error: '{title}' was not checked out or does not exist.")

    def list_available_books(self):
        """Prints a list of all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")