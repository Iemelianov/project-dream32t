# tests/test_del_birthday.py
import sys
import os

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.model.contact_book import ContactBook
from src.command.handler.birthday.del_birthday import DelBirthdayCommandHandler  # adjust path if needed


# ───────────────────────────────────────
# Test: Delete Birthday (success)
# ───────────────────────────────────────
def test_del_birthday_success():
    # Arrange
    book = ContactBook()
    book.create_contact("Alice", "1234567890")
    
    # Add a birthday first
    from src.command.handler.birthday.add_birthday import AddBirthdayCommandHandler
    add_handler = AddBirthdayCommandHandler(book)
    add_handler._handle(["Alice", "15.05.1990"])

    # Act
    del_handler = DelBirthdayCommandHandler(book)
    del_handler._handle(["Alice"])

    # Assert
    contact = book.find_contact("Alice")
    assert contact.birthday is None, "Birthday should be deleted"
    print("✅ Delete birthday (success) test passed!")


# ───────────────────────────────────────
# Test: Delete Birthday (no birthday exists)
# ───────────────────────────────────────
def test_del_birthday_no_birthday():
    book = ContactBook()
    book.create_contact("Bob", "0000000000")

    from io import StringIO
    import sys as sys_mod
    old_stdout = sys_mod.stdout
    sys_mod.stdout = captured = StringIO()

    del_handler = DelBirthdayCommandHandler(book)
    del_handler._handle(["Bob"])

    sys_mod.stdout = old_stdout
    output = captured.getvalue()

    assert "has no birthday to delete" in output
    contact = book.find_contact("Bob")
    assert contact.birthday is None
    print("✅ Delete birthday (no birthday) test passed!")


# ───────────────────────────────────────
# Test: Delete Birthday (contact not found)
# ───────────────────────────────────────
def test_del_birthday_contact_not_found():
    book = ContactBook()

    from io import StringIO
    import sys as sys_mod
    old_stdout = sys_mod.stdout
    sys_mod.stdout = captured = StringIO()

    del_handler = DelBirthdayCommandHandler(book)
    del_handler._handle(["Unknown"])

    sys_mod.stdout = old_stdout
    output = captured.getvalue()

    assert "Contact not found" in output
    print("✅ Delete birthday (contact not found) test passed!")


# ───────────────────────────────────────
# Run All Tests
# ───────────────────────────────────────
def run_all_tests():
    print("🧪 Starting del-birthday handler tests...\n")
    try:
        test_del_birthday_success()
        test_del_birthday_no_birthday()
        test_del_birthday_contact_not_found()
        print("\n🎉 All del-birthday tests passed!")
    except Exception as e:
        print(f"\n💥 Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    run_all_tests()