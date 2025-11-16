from src.model.field import Field
from src.util.messages import INVALID_ADDRESS

# Represents an address field
class Address(Field):
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError(INVALID_ADDRESS)
        
        clean_value = value.strip()
        if not clean_value:
            raise ValueError(INVALID_ADDRESS)
            
        super().__init__(clean_value)

    def __str__(self):
        return str(self.value)
