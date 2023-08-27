import pytest
from VellumVault.apps.users.domain.aggregates.user import User
from VellumVault.apps.users.domain.value_objects.address import Address

def test_user_creation():
    address = Address("123 Main St", "Springfield", "IL", "62704")
    user = User(user_id=1, name="John Doe", address=address)

    assert user.user_id == 1
    assert user.name == "John Doe"
    assert user.address == address
