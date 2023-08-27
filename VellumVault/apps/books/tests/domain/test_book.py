import pytest
from VellumVault.apps.books.domain.aggregates.book import Book
from VellumVault.apps.books.domain.value_objects.isbn import ISBN

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