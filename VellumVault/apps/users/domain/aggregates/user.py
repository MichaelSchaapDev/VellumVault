from ..value_objects.address import Address

class User:
    def __init__(self, user_id: int, name: str, address: Address):
        # Check if the name is empty or contains only whitespace
        if not name or name.isspace():
            raise ValueError("Name cannot be empty or whitespace")

        # Check if the user_id is an integer
        if not isinstance(user_id, int):
            raise TypeError("User ID must be an integer")

        # Check if the user_id is non-negative
        if user_id < 0:
            raise ValueError("User ID must be non-negative")

        self.user_id = user_id
        self.name = name
        self.address = address

    def __eq__(self, other):
        return (
            self.user_id == other.user_id and
            self.name == other.name and
            self.address == other.address
        )

    def __ne__(self, other):
        return not self.__eq__(other)
