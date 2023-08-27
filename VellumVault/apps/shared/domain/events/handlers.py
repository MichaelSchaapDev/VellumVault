from .event_bus import EventBus
from ....books.domain.events.book_borrowed import BookBorrowed
from ....books.domain.events.book_returned import BookReturned

event_bus = EventBus()

def handle_book_borrowed(event: BookBorrowed):
    print(f"Book with ID {event.book_id} has been borrowed.")

def handle_book_returned(event: BookReturned):
    print(f"Book with ID {event.book_id} has been returned.")

# Register the handler
event_bus.register(BookBorrowed, handle_book_borrowed)
event_bus.register(BookReturned, handle_book_returned)
