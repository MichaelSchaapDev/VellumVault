from VellumVault.apps.users.domain.aggregates.user import User
from VellumVault.apps.books.domain.aggregates.book import Book

class Loan:
    def __init__(self, loan_id: int, user: User, book: Book, due_date: str):
        self.loan_id = loan_id
        self.user = user
        self.book = book
        self.due_date = due_date
