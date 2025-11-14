import re

from field import Field


# Represents an email field with basic validation
class Email(Field):
    def __init__(self, value):
        # Basic email validation pattern
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not isinstance(value, str) or not re.fullmatch(email_pattern, value.strip()):
            raise ValueError("Please provide a valid email address.")
        super().__init__(value.strip())