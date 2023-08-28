from ..value_objects.address import Address

class User:
    def __init__(self, user_id: int, name: str, address: Address):
        if not name:
            raise ValueError("Name cannot be empty")
         
        self.user_id = user_id
        self.name = name
        self.address = address
