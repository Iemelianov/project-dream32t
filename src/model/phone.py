from src.model.field import Field
from src.util.messages import INVALID_PHONE


# Represents a phone number with validation: must be exactly 10 digits
class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError(INVALID_PHONE)
        super().__init__(value)

    def __str__(self):
        return str(self.value)
