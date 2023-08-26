# VellumVault Domain Modeling

This document outlines the domain model for the VellumVault Library Management System. The primary goal is to provide a high-level understanding of the main entities, value objects, domain events, and services that constitute the domain.

## Table of Contents

- [Entities](#entities)
- [Value Objects](#value-objects)
- [Aggregates](#aggregates)
- [Domain Events](#domain-events)
- [Domain Services & Policies](#domain-services--policies)

---

## Entities

### User

Represents a library user who can borrow and return books.

- **Attributes**:
  - `user_id`: Unique identifier for each user.
  - `name`: Full name of the user.
  - `address`: Address of the user (Value Object).

### Book

Represents a book in the library.

- **Attributes**:
  - `book_id`: Unique identifier for each book.
  - `title`: Title of the book.
  - `isbn`: ISBN number of the book (Value Object).

### Loan

Represents the action of borrowing a book by a user.

- **Attributes**:
  - `loan_id`: Unique identifier for each loan.
  - `user`: The user who borrowed the book (Entity).
  - `book`: The book that was borrowed (Entity).
  - `due_date`: The date by which the book should be returned.

---

## Value Objects

### ISBN

A unique identifier for each book.

- **Attributes**:
  - `isbn_number`: The ISBN number.

### Address

The physical address of a user.

- **Attributes**:
  - `street`: Street name.
  - `city`: City name.
  - `state`: State name.
  - `zip_code`: Zip code.

---

## Aggregates

### User

The User entity serves as an aggregate root containing the `Address` value object and is responsible for multiple `Loan` entities.

### Book

The Book entity serves as an aggregate root containing the `ISBN` value object and related `Loan` entities.

---

## Domain Events

### BookBorrowed

Triggered when a book is borrowed by a user.

### BookReturned

Triggered when a book is returned to the library.

### OverdueNotificationSent

Triggered when a user is notified of an overdue book.

---

## Domain Services & Policies

### LoanApprovalService

A domain service that involves both the User and Book to approve a loan.

### OverdueFineCalculation

A policy that calculates the overdue fines for a User based on their Loans.
