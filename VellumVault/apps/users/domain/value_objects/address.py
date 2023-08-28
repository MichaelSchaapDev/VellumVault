class Address:
    def __init__(self, street: str, city: str, state: str, zip_code: str):
        if not street:
            raise ValueError("Street cannot be empty")
        
        if not city:
            raise ValueError("City cannot be empty")
        
        if not state:
            raise ValueError("State cannot be empty")
        
        if not zip_code:
            raise ValueError("Zip code cannot be empty")
        
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
