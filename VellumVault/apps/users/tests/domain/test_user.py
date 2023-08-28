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

# Test for User ID data type
def test_user_id_data_type():
    address = Address(street="123 Main St", city="Cityville", state="State", zip_code="12345")
    with pytest.raises(TypeError):
        User(user_id="1", name="John Doe", address=address)

# Test for User ID non-negative
def test_user_id_non_negative():
    address = Address(street="123 Main St", city="Cityville", state="State", zip_code="12345")
    with pytest.raises(ValueError):
        User(user_id=-1, name="John Doe", address=address)

# Test for whitespace name
def test_create_user_with_whitespace_name():
    address = Address(street="123 Main St", city="Cityville", state="State", zip_code="12345")
    with pytest.raises(ValueError):
        User(user_id=1, name="   ", address=address)

# Test for setting a new name
def test_setting_new_name():
    address = Address(street="123 Main St", city="Cityville", state="State", zip_code="12345")
    user = User(user_id=1, name="John Doe", address=address)
    user.name = "Jane Doe"
    assert user.name == "Jane Doe"

# Test for setting a new address
def test_setting_new_address():
    address = Address(street="123 Main St", city="Cityville", state="State", zip_code="12345")
    new_address = Address(street="124 Main St", city="Cityville", state="State", zip_code="12345")
    user = User(user_id=1, name="John Doe", address=address)
    user.address = new_address
    assert user.address == new_address

# Test for Equality
def test_user_equality():
    address1 = Address(street="123 Main St", city="Cityville", state="State", zip_code="12345")
    address2 = Address(street="123 Main St", city="Cityville", state="State", zip_code="12345")
    user1 = User(user_id=1, name="John Doe", address=address1)
    user2 = User(user_id=1, name="John Doe", address=address2)
    assert user1 == user2

# Test for Inequality
def test_user_inequality():
    address = Address(street="123 Main St", city="Cityville", state="State", zip_code="12345")
    user1 = User(user_id=1, name="John Doe", address=address)
    user2 = User(user_id=2, name="Jane Doe", address=address)
    assert user1 != user2
