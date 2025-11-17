from src.model.field import Field


# Represents a contact's name; inherits from Field
class Name(Field):
    def __init__(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string.")
        super().__init__(value)
        self.value = value.strip()
