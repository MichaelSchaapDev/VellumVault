import pytest
from VellumVault.apps.loans.domain.aggregate.loan import Loan
from VellumVault.apps.users.domain.aggregates.user import User
from VellumVault.apps.users.domain.value_objects.address import Address
from VellumVault.apps.books.domain.aggregates.book import Book
from VellumVault.apps.books.domain.value_objects.isbn import ISBN

def test_loan_creation():
    # Create a User
    address = Address("123 Main St", "Springfield", "IL", "62704")
    user = User(user_id=1, name="John Doe", address=address)

    # Create a Book
    isbn = ISBN("978-3-16-148410-0")
    book = Book(book_id=1, title="Domain-Driven Design", isbn=isbn)

    # Create a Loan
    loan = Loan(loan_id=1, user=user, book=book, due_date="2023-09-01")

    # Assertions
    assert loan.loan_id == 1
    assert loan.user == user
    assert loan.book == book
    assert loan.due_date == "2023-09-01"
