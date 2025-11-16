import re

from src.model.field import Field
from src.util.messages import INVALID_EMAIL


# Represents an email field with basic validation
class Email(Field):
    def __init__(self, value):
        # Basic email validation pattern
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not isinstance(value, str) or not re.fullmatch(email_pattern, value.strip()):
            raise ValueError(INVALID_EMAIL)
        super().__init__(value.strip())

    def __str__(self):
        return str(self.value)
