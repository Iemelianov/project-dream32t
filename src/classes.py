from datetime import datetime
import re


# Base class for all fields in a contact record
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


# Represents a contact's name; inherits from Field
class Name(Field):
    def __init__(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string.")
        self.value = value.strip()


# Represents a phone number with validation: must be exactly 10 digits
class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)  # ← cleaner and consistente


# Represents a birthday field with date validation
class Birthday(Field):
    def __init__(self, value):
        try:
            date_obj = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(date_obj)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


# Represents an address field
class Address(Field):
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Address must be a string.")
        super().__init__(value.strip())


# Represents an email field with basic validation
class Email(Field):
    def __init__(self, value):
        # Basic email validation pattern
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not isinstance(value, str) or not re.fullmatch(email_pattern, value.strip()):
            raise ValueError("Please provide a valid email address.")
        super().__init__(value.strip())
