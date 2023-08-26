from  apps.users.domain.value_objects import Address

class User:
    def __init__(self, user_id: int, name: str, address: Address):
        self.user_id = user_id
        self.name = name
        self.address = address
