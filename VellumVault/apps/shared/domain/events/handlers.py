from .event_bus import EventBus
from ....books.domain.events.book_borrowed import BookBorrowed
from ....books.domain.events.book_returned import BookReturned
from ....users.domain.events.overdue_notification_sent import OverdueNotificationSent

event_bus = EventBus()

def handle_book_borrowed(event: BookBorrowed):
    print(f"Book with ID {event.book_id} has been borrowed.")

def handle_book_returned(event: BookReturned):
    print(f"Book with ID {event.book_id} has been returned.")
    
def handle_overdue_notification_sent(event: OverdueNotificationSent):
    print(f"Overdue notification has been sent to {event.user}")    

# Register the handler
event_bus.register(BookBorrowed, handle_book_borrowed)
event_bus.register(BookReturned, handle_book_returned)
event_bus.register(OverdueNotificationSent, handle_overdue_notification_sent)