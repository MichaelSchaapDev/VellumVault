from apps.books.domain.value_objects import ISBN

class Book:
    def __init__(self, book_id: int, title: str, isbn: ISBN):
        self.book_id = book_id
        self.title = title
        self.isbn = isbn
