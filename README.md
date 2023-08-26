# VellumVault: A Library Management System

## Overview

VellumVault is a Library Management System built with Python and Django. It follows best practices like Domain-Driven Design (DDD) and Test-Driven Design (TDD) to ensure that the system is not only efficient but also maintainable and scalable.

## Features

- User authentication and authorization
- Inventory management for books
- Loan management for book borrowings and returns
- Overdue fine calculations
- Domain events like `BookBorrowed` and `BookReturned`
- RESTful API interface

## Table of Contents

- [Setup](#setup)
- [Running Tests](#running-tests)
- [API Endpoints](#api-endpoints)
- [Domain Model](#domain-model)
- [Contributing](#contributing)
- [License](#license)

## Setup

### Prerequisites

- Python 3.8+
- PostgreSQL
- Virtual environment (`venv` or `conda`)

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/MichaelSchaapDev/VellumVault.git
    ```

2. Navigate to the project directory:
    ```bash
    cd VellumVault
    ```

3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run database migrations:
    ```bash
    python manage.py migrate
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Running Tests

To run the tests, use the following command:

```bash
pytest
```

## API Endpoints

Documentation for the API is available at `http://localhost:8000/api/docs/`.

## Domain Model

- **Entities**: User, Book, Loan
- **Value Objects**: Address, ISBN
- **Aggregates**: User, Book
- **Domain Events**: BookBorrowed, BookReturned
- **Domain Services & Policies**: LoanApproval, OverdueFineCalculation

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## License

This project is licensed under the MIT License. See [LICENSE.md](LICENSE.md) for details.
