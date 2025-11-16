from src.model.field import Field
from src.model.field import Field


# Represents a phone number with validation: must be exactly 10 digits
class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)  # ← cleaner and consistente