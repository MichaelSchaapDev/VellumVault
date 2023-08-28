import pytest
from VellumVault.apps.users.domain.aggregates.user import User
from VellumVault.apps.users.domain.value_objects.address import Address

# Test for successfully creating a user with valid attributes
def test_user_creation():
    address = Address(street="123 Main St", city="Cityville", state="State", zip_code="12345")
    user = User(user_id=1, name="John Doe", address=address)

    assert user.user_id == 1
    assert user.name == "John Doe"
    assert user.address == address

# Test for attempting to create a user with an empty name. Should raise a ValueError.
def test_create_user_with_empty_name():
    address = Address(street="123 Main St", city="Cityville", state="State", zip_code="12345")

    with pytest.raises(ValueError):
        User(user_id=1, name="", address=address)

# Test for attempting to create a user with an invalid address. Should raise a ValueError.
def test_create_user_with_invalid_address():
    with pytest.raises(ValueError):
        Address(street="", city="Cityville", state="State", zip_code="12345")

# Test for domain event OverdueNotificationSent, assuming such an event exists in your domain model.
def test_overdue_notification_sent_event():
    address = Address(street="123 Main St", city="Cityville", state="State", zip_code="12345")
    user = User(user_id=1, name="John Doe", address=address)
    
    # Simulate sending overdue notification
    user.send_overdue_notification()
    
    assert user.overdue_notification_sent

# Test that a user's overdue notification status is set/reset correctly.
def test_user_overdue_notification_status():
    address = Address(street="123 Main St", city="Cityville", state="State", zip_code="12345")
    user = User(user_id=1, name="John Doe", address=address)
    
    user.send_overdue_notification()
    assert user.overdue_notification_sent
    
    user.reset_overdue_notification()
    assert not user.overdue_notification_sent

# Test that a user's borrowed book count is initially zero.
def test_initial_borrowed_book_count():
    address = Address(street="123 Main St", city="Cityville", state="State", zip_code="12345")
    user = User(user_id=1, name="John Doe", address=address)
    
    assert user.borrowed_book_count() == 0