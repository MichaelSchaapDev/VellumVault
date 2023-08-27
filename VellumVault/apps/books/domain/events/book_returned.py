from datetime import datetime

class BookReturned:
    def __init__(self, book_id: int, timestamp: datetime):
        self.book_id = book_id
        self.timestamp = timestamp