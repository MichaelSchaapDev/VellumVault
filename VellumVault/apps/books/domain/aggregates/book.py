from ....shared.domain.events.handlers import event_bus
from ..events.book_borrowed import BookBorrowed
from ..events.book_returned import BookReturned
from ..value_objects.isbn import ISBN
from datetime import datetime

class Book:
    def __init__(self, book_id: int, title: str, isbn: ISBN, status: str = "available"):
        if not title:
            raise ValueError("Title cannot be empty")

        if not isbn:
            raise ValueError("ISBN cannot be empty")
        
        self.book_id = book_id
        self.title = title
        self.isbn = isbn
        self.status = status

    def change_title(self, new_title: str):
        """
        Change the title of the book to the given new title.
        
        :param new_title: The new title to be set
        :type new_title: str
        """
        if not new_title:
            raise ValueError("Title cannot be empty")
        self.title = new_title

    def change_isbn(self, new_isbn: ISBN):
        """
        Change the ISBN of the book to the given new ISBN.
        
        :param new_isbn: The new ISBN to be set
        :type new_isbn: ISBN
        """
        self.isbn = new_isbn

    def borrow(self):
        if self.status == "available":
            self.status = "borrowed"
            event = BookBorrowed(book_id=self.book_id, timestamp=datetime.now())
            event_bus.dispatch(event)

    def return_book(self):
        if self.status == "borrowed":
            self.status = "available"
            event = BookReturned(book_id=self.book_id, timestamp=datetime.now())
            event_bus.dispatch(event)