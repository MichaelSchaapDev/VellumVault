import pytest
from VellumVault.apps.books.domain.aggregates.book import Book
from VellumVault.apps.books.domain.value_objects.isbn import ISBN

def test_book_creation():
    isbn = ISBN("978-3-16-148410-0")
    book = Book(book_id=1, title="Domain-Driven Design", isbn=isbn)

    assert book.book_id == 1
    assert book.title == "Domain-Driven Design"
    assert book.isbn == isbn
