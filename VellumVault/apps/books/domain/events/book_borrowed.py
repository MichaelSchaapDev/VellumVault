from datetime import datetime

class BookBorrowed:
    def __init__(self, book_id: int, timestamp: datetime):
        self.book_id = book_id
        self.timestamp = timestamp
