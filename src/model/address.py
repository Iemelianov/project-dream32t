from src.model.field import Field


# Represents an address field
class Address(Field):
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Address must be a string.")
        super().__init__(value.strip())
