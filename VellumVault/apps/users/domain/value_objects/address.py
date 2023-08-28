class Address:
    def __init__(self, street: str, city: str, state: str, zip_code: str):
        if not street:
            raise ValueError("Street cannot be empty")
        
        if not city:
            raise ValueError("City cannot be empty")
        
        if not state:
            raise ValueError("State cannot be empty")

        # Check if the zip code is numeric
        if not zip_code.isnumeric():
            raise ValueError("Zip code must be numeric")

        # Check the length of the zip code
        if len(zip_code) != 5:
            raise ValueError("Zip code must be 5 digits long")
        
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __eq__(self, other):
        return (
            self.street == other.street and
            self.city == other.city and
            self.state == other.state and
            self.zip_code == other.zip_code
        )

    def __ne__(self, other):
        return not self.__eq__(other)
