from .event_bus import EventBus
from ....books.domain.events.book_borrowed import BookBorrowed

event_bus = EventBus()

def handle_book_borrowed(event: BookBorrowed):
    print(f"Book with ID {event.book_id} has been borrowed.")

# Register the handler
event_bus.register(BookBorrowed, handle_book_borrowed)
