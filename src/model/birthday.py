from datetime import datetime

from src.model.field import Field
from src.util.messages import INVALID_BIRTHDAY


# Represents a birthday field with date validation
class Birthday(Field):
    def __init__(self, value):
        try:
            date_obj = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(date_obj)
        except ValueError as exc:
            raise ValueError(INVALID_BIRTHDAY) from exc
