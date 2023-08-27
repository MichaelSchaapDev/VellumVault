class ISBN:
    def __init__(self, isbn: str):
        if not self.is_valid_isbn(isbn):
            raise ValueError("Invalid ISBN")
        self.value = isbn

    @staticmethod
    def is_valid_isbn(isbn: str) -> bool:
        # Removing any hyphens
        isbn = isbn.replace('-', '')
        
        # ISBN-13 should be 13 digits
        if len(isbn) != 13:
            return False

        total = 0
        for i, digit in enumerate(isbn):
            n = int(digit)
            if i % 2 == 0:
                total += n
            else:
                total += 3 * n

        return total % 10 == 0
