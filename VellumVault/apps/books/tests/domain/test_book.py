import pytest
from VellumVault.apps.books.domain.aggregates.book import Book
from VellumVault.apps.books.domain.value_objects.isbn import ISBN
from datetime import datetime, timedelta

# Test for successfully creating a book with valid attributes
def test_book_creation():
    isbn = ISBN("978-3-16-148410-0")
    book = Book(book_id=1, title="Domain-Driven Design", isbn=isbn)

    assert book.book_id == 1
    assert book.title == "Domain-Driven Design"
    assert book.isbn == isbn

# Test for ISBN validation. Should raise a ValueError for an invalid ISBN.
def test_invalid_isbn_creation():
    with pytest.raises(ValueError):
        ISBN("invalid-isbn")

# Test for changing a book's ISBN to a new valid ISBN.
def test_change_book_attributes():
    isbn = ISBN("978-1-86197-271-2")
    book = Book(book_id=1, title="Domain-Driven Design", isbn=isbn)
    
    new_isbn = ISBN("978-0-596-52068-7")
    book.change_isbn(new_isbn)
    
    assert book.isbn == new_isbn

# Test for attempting to change a book's title to an empty string. Should raise a ValueError.
def test_change_book_to_invalid_title():
    isbn = ISBN("978-1-86197-271-2")
    book = Book(book_id=1, title="Domain-Driven Design", isbn=isbn)

    with pytest.raises(ValueError):
        book.change_title("")

# Test for creating a book with an empty title. Should raise a ValueError.
def test_create_book_with_empty_title():
    isbn = ISBN("978-1-86197-271-2")

    with pytest.raises(ValueError):
        Book(book_id=1, title="", isbn=isbn)

# Test for domain event BookBorrowed, assuming such an event exists in your domain model.
def test_book_borrowed_event():
    isbn = ISBN("978-1-86197-271-2")
    book = Book(book_id=1, title="Domain-Driven Design", isbn=isbn)
    
    book.borrow()
    
    assert book.status == "borrowed"

# Test that a book's status transitions correctly when borrowed and returned.
def test_book_status_transitions():
    isbn = ISBN("978-1-86197-271-2")
    book = Book(book_id=1, title="Domain-Driven Design", isbn=isbn)
    
    book.borrow()
    assert book.status == "borrowed"
    
    book.return_book()
    assert book.status == "available"

# Test that a due date is set/updated correctly when a book is borrowed.
def test_due_date_calculation():
    isbn = ISBN("978-1-86197-271-2")
    book = Book(book_id=1, title="Domain-Driven Design", isbn=isbn)
    
    book.borrow()
    assert book.due_date == datetime.now() + timedelta(days=14)

# Test to check if a book is marked as overdue after the due date.
def test_overdue_book():
    isbn = ISBN("978-1-86197-271-2")
    book = Book(book_id=1, title="Domain-Driven Design", isbn=isbn)
    
    book.borrow()
    book.due_date = datetime.now() - timedelta(days=1)  # Manually setting the due date to the past
    
    assert book.is_overdue()