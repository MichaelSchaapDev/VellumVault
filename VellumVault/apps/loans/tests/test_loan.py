import pytest
from apps.loans.domain.entities import Loan
from apps.users.domain.aggregates import User
from apps.users.domain.value_objects import Address
from apps.books.domain.aggregates import Book
from apps.books.domain.value_objects import ISBN

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
