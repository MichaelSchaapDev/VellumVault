import pytest
from VellumVault.apps.users.domain.aggregates.user import User
from VellumVault.apps.users.domain.value_objects.address import Address

# Test for successfully creating an address with valid attributes
def test_create_address_with_valid_attributes():
    address = Address(street="123 Main St", city="Cityville", state="State", zip_code="12345")
    assert address.street == "123 Main St"
    assert address.city == "Cityville"
    assert address.state == "State"
    assert address.zip_code == "12345"

# Test for attempting to create an address with an empty street. Should raise a ValueError.
def test_create_address_with_empty_street():
    with pytest.raises(ValueError):
        Address(street="", city="Cityville", state="State", zip_code="12345")

# Test for attempting to create an address with an empty city. Should raise a ValueError.
def test_create_address_with_empty_city():
    with pytest.raises(ValueError):
        Address(street="123 Main St", city="", state="State", zip_code="12345")

# Test for attempting to create an address with an empty state. Should raise a ValueError.
def test_create_address_with_empty_state():
    with pytest.raises(ValueError):
        Address(street="123 Main St", city="Cityville", state="", zip_code="12345")

# Test for attempting to create an address with an empty zip code. Should raise a ValueError.
def test_create_address_with_empty_zip_code():
    with pytest.raises(ValueError):
        Address(street="123 Main St", city="Cityville", state="State", zip_code="")

# Test for attempting to create an address with an empty street, and check if it fails as expected
def test_address_creation_with_empty_street_fails():
    with pytest.raises(ValueError):
        Address(street="", city="Cityville", state="State", zip_code="12345")

# Test for Address Zip code to be numeric
def test_address_zip_code_numeric():
    with pytest.raises(ValueError):
        Address(street="123 Main St", city="Cityville", state="State", zip_code="12A45")

# Test for invalid Zip Code length
def test_address_invalid_zip_code_length():
    with pytest.raises(ValueError):
        Address(street="123 Main St", city="Cityville", state="State", zip_code="123456")

# Test for Equality
def test_address_equality():
    address1 = Address(street="123 Main St", city="Cityville", state="State", zip_code="12345")
    address2 = Address(street="123 Main St", city="Cityville", state="State", zip_code="12345")
    assert address1 == address2

# Test for Inequality
def test_address_inequality():
    address1 = Address(street="123 Main St", city="Cityville", state="State", zip_code="12345")
    address2 = Address(street="124 Main St", city="Cityville", state="State", zip_code="12345")
    assert address1 != address2
