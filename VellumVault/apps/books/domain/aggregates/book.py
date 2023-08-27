from ....shared.domain.events.handlers import event_bus
from ..events.book_borrowed import BookBorrowed
from ..events.book_returned import BookReturned
from ..value_objects.isbn import ISBN
from datetime import datetime, timedelta

class Book:
    """
    Represents a book in the library.
    
    Attributes:
        book_id (int): The unique identifier for the book.
        title (str): The title of the book.
        isbn (ISBN): The ISBN of the book.
        status (str): The current status of the book (available or borrowed).
        due_date (datetime): The due date if the book is borrowed.
        
    Domain Events:
        BookBorrowed: Triggered when the book is borrowed.
        BookReturned: Triggered when the book is returned.
    """
    
    def __init__(self, book_id: int, title: str, isbn: ISBN, status: str = "available"):
        """Initializes a new instance of the Book class."""
        if not title:
            raise ValueError("Title cannot be empty")
        if not isbn:
            raise ValueError("ISBN cannot be empty")
        
        self.book_id = book_id
        self.title = title
        self.isbn = isbn
        self.status = status
        self.due_date = None

    def change_title(self, new_title: str):
        """
        Change the title of the book to the given new title.
        
        Args:
            new_title (str): The new title to be set.
            
        Raises:
            ValueError: If the new title is empty.
        """
        if not new_title:
            raise ValueError("Title cannot be empty")
        self.title = new_title

    def change_isbn(self, new_isbn: ISBN):
        """
        Change the ISBN of the book to the given new ISBN.
        
        Args:
            new_isbn (ISBN): The new ISBN to be set.
        """
        self.isbn = new_isbn

    def borrow(self):
        """
        Borrow the book, changing its status to 'borrowed' and setting the due date.
        
        Domain Events:
            BookBorrowed: Triggered when the book is borrowed.
        """
        if self.status == "available":
            self.status = "borrowed"
            self.due_date = datetime.now() + timedelta(days=14)  # Calculate due date
            event = BookBorrowed(book_id=self.book_id, timestamp=datetime.now())
            event_bus.dispatch(event)

    def return_book(self):
        """
        Return the book, changing its status to 'available' and resetting the due date.
        
        Domain Events:
            BookReturned: Triggered when the book is returned.
        """
        if self.status == "borrowed":
            self.status = "available"
            self.due_date = None  # Reset the due date to None
            event = BookReturned(book_id=self.book_id, timestamp=datetime.now())
            event_bus.dispatch(event)

    def is_overdue(self):
        """
        Check if the book is overdue.
        
        Returns:
            bool: True if the book is overdue, False otherwise.
        """
        if self.status != "borrowed" or self.due_date is None:
            return False
        return datetime.now() > self.due_date
