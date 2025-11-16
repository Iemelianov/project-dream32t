# tests/test.py
import sys
import os

# Add project root to Python path so 'src' is importable
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# Import handlers and models
from src.model.contact_book import ContactBook
from src.command.handler.address.add_address import AddAddressCommandHandler
from src.command.handler.address.change_address import ChangeAddressCommandHandler
from src.command.handler.address.del_address import DelAddressCommandHandler


# ───────────────────────────────────────
# Test: Add Address
# ───────────────────────────────────────
def test_add_address():
    book = ContactBook()
    book.create_contact("Alice", "1234567890")
    handler = AddAddressCommandHandler(book)
    handler._handle(["Alice", "123 Main St"])

    contact = book.find_contact("Alice")
    assert hasattr(contact, 'addresses'), "Contact missing 'addresses' attribute"
    assert len(contact.addresses) == 1, "Expected 1 address"
    assert contact.addresses[0].value == "123 Main St", "Address value mismatch"
    print("✅ Add address test passed!")


# ───────────────────────────────────────
# Test: Change Address (Success)
# ───────────────────────────────────────
def test_change_address_success():
    book = ContactBook()
    book.create_contact("Bob", "0000000000")
    
    add_handler = AddAddressCommandHandler(book)
    add_handler._handle(["Bob", "Old Street"])

    change_handler = ChangeAddressCommandHandler(book)
    change_handler._handle(["Bob", "Old Street", "New Avenue"])

    contact = book.find_contact("Bob")
    assert len(contact.addresses) == 1
    assert contact.addresses[0].value == "New Avenue"
    print("✅ Change address (success) test passed!")


# ───────────────────────────────────────
# Test: Change Address (Old Address Not Found)
# ───────────────────────────────────────
def test_change_address_not_found():
    book = ContactBook()
    book.create_contact("Charlie", "1111111111")
    
    add_handler = AddAddressCommandHandler(book)
    add_handler._handle(["Charlie", "Valid Address"])

    # Capture printed output
    from io import StringIO
    import sys as sys_mod
    old_stdout = sys_mod.stdout
    sys_mod.stdout = captured = StringIO()

    change_handler = ChangeAddressCommandHandler(book)
    change_handler._handle(["Charlie", "Wrong Address", "New Addr"])

    sys_mod.stdout = old_stdout
    output = captured.getvalue()

    # Should NOT succeed
    assert "Changed a address." not in output
    # Should show error
    assert "Address not found for contact 'Charlie'." in output

    # Original address must remain
    contact = book.find_contact("Charlie")
    assert len(contact.addresses) == 1
    assert contact.addresses[0].value == "Valid Address"
    print("✅ Change address (not found) test passed!")


# ───────────────────────────────────────
# Test: Delete Address (Success)
# ───────────────────────────────────────
def test_del_address_success():
    book = ContactBook()
    book.create_contact("Diana", "2222222222")
    
    add_handler = AddAddressCommandHandler(book)
    add_handler._handle(["Diana", "To Be Deleted"])

    # Capture output
    from io import StringIO
    import sys as sys_mod
    old_stdout = sys_mod.stdout
    sys_mod.stdout = captured = StringIO()

    del_handler = DelAddressCommandHandler(book)
    del_handler._handle(["Diana", "To Be Deleted"])

    sys_mod.stdout = old_stdout
    output = captured.getvalue()

    assert "Address deleted for contact 'Diana'." in output

    contact = book.find_contact("Diana")
    assert len(contact.addresses) == 0
    print("✅ Delete address (success) test passed!")


# ───────────────────────────────────────
# Test: Delete Address (Not Found)
# ───────────────────────────────────────
def test_del_address_not_found():
    book = ContactBook()
    book.create_contact("Eve", "3333333333")
    
    add_handler = AddAddressCommandHandler(book)
    add_handler._handle(["Eve", "Kept Address"])

    # Capture output
    from io import StringIO
    import sys as sys_mod
    old_stdout = sys_mod.stdout
    sys_mod.stdout = captured = StringIO()

    del_handler = DelAddressCommandHandler(book)
    del_handler._handle(["Eve", "Missing Address"])

    sys_mod.stdout = old_stdout
    output = captured.getvalue()

    assert "Address not found for contact 'Eve'." in output

    contact = book.find_contact("Eve")
    assert len(contact.addresses) == 1
    assert contact.addresses[0].value == "Kept Address"
    print("✅ Delete address (not found) test passed!")


# ───────────────────────────────────────
# Run All Tests
# ───────────────────────────────────────
def run_all_tests():
    print("🧪 Starting address handler tests...\n")
    try:
        test_add_address()
        test_change_address_success()
        test_change_address_not_found()
        test_del_address_success()
        test_del_address_not_found()
        print("\n🎉 All tests passed!")
    except Exception as e:
        print(f"\n💥 Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


# ───────────────────────────────────────
# Entry Point
# ───────────────────────────────────────
if __name__ == "__main__":
    run_all_tests()