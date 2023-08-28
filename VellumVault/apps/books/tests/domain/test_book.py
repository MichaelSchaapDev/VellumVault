import pytest
from VellumVault.apps.books.domain.aggregates.book import Book
from VellumVault.apps.books.domain.value_objects.isbn import ISBN
from datetime import datetime, timedelta

def test_book_creation():
    """Test that a Book object can be successfully created with valid attributes."""
    isbn = ISBN("978-3-16-148410-0")
    book = Book(book_id=1, title="Domain-Driven Design", isbn=isbn)

    assert book.book_id == 1
    assert book.title == "Domain-Driven Design"
    assert book.isbn == isbn

def test_invalid_isbn_creation():
    """Test that creating an ISBN with an invalid string raises a ValueError."""
    with pytest.raises(ValueError):
        ISBN("invalid-isbn")

def test_change_book_attributes():
    """Test that a Book's ISBN can be successfully updated."""
    isbn = ISBN("978-1-86197-271-2")
    book = Book(book_id=1, title="Domain-Driven Design", isbn=isbn)
    
    new_isbn = ISBN("978-0-596-52068-7")
    book.change_isbn(new_isbn)
    
    assert book.isbn == new_isbn

def test_change_book_to_invalid_title():
    """Test that attempting to set a Book's title to an empty string raises a ValueError."""
    isbn = ISBN("978-1-86197-271-2")
    book = Book(book_id=1, title="Domain-Driven Design", isbn=isbn)

    with pytest.raises(ValueError):
        book.change_title("")

def test_create_book_with_empty_title():
    """Test that attempting to create a Book with an empty title raises a ValueError."""
    isbn = ISBN("978-1-86197-271-2")

    with pytest.raises(ValueError):
        Book(book_id=1, title="", isbn=isbn)

def test_create_book_with_empty_isbn():
    """Test that attempting to create a Book with an empty ISBN raises a ValueError."""
    with pytest.raises(ValueError):
        Book(book_id=1, title="Some Title", isbn=ISBN(""))

def test_book_borrowed_event():
    """Test that the 'borrow' method changes the Book's status to 'borrowed'."""
    isbn = ISBN("978-1-86197-271-2")
    book = Book(book_id=1, title="Domain-Driven Design", isbn=isbn)
    
    book.borrow()
    
    assert book.status == "borrowed"

def test_book_status_transitions():
    """Test that the Book's status transitions correctly between 'borrowed' and 'available'."""
    isbn = ISBN("978-1-86197-271-2")
    book = Book(book_id=1, title="Domain-Driven Design", isbn=isbn)
    
    book.borrow()
    assert book.status == "borrowed"
    
    book.return_book()
    assert book.status == "available"

def test_due_date_calculation():
    """Test that the due date is set correctly when a book is borrowed."""
    isbn = ISBN("978-1-86197-271-2")
    book = Book(book_id=1, title="Domain-Driven Design", isbn=isbn)
    
    book.borrow()
    assert book.due_date == datetime.now() + timedelta(days=14)

def test_overdue_book():
    """Test that a book is marked as overdue if its due date has passed."""
    isbn = ISBN("978-1-86197-271-2")
    book = Book(book_id=1, title="Domain-Driven Design", isbn=isbn)
    
    book.borrow()
    book.due_date = datetime.now() - timedelta(days=1)  # Manually setting the due date to the past
    
    assert book.is_overdue()