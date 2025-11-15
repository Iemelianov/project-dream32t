# tests/test.py

import sys
import os

# Add PROJECT ROOT (parent of 'src') to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

print("Project root added to sys.path:", project_root)
print("Checking if 'src' is importable...")

# Now import
try:
    import src
    print("✅ 'src' imported successfully. Location:", src.__file__)
except ImportError as e:
    print("❌ Failed to import 'src':", e)
    sys.exit(1)

from src.model.contact_book import ContactBook
from src.command.handler.address.add_address import AddAddressCommandHandler

# Rest of your test...
def test_add_address():
    book = ContactBook()
    book.create_contact("Alice", "1234567890")
    handler = AddAddressCommandHandler(book)
    handler._handle(["Alice", "123 Main St"])

    contact = book.find_contact("Alice")
    assert contact.address is not None
    assert contact.address.value == "123 Main St"
    print("✅ Test passed!")

if __name__ == "__main__":
    test_add_address()