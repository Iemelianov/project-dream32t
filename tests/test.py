# tests/test_birthday_handler.py
import sys
import os

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.model.contact_book import ContactBook
from src.command.handler.birthday.add_birthday import AddBirthdayCommandHandler


def test_add_birthday_success():
    """Test adding a birthday to a contact that has no birthday."""
    # Arrange
    book = ContactBook()
    book.create_contact("Alice", "1234567890")
    
    handler = AddBirthdayCommandHandler(book)
    
    # Act
    handler._handle(["Alice", "15.05.1990"])
    
    # Assert
    contact = book.find_contact("Alice")
    assert contact.birthday is not None
    assert contact.birthday.value.strftime("%d.%m.%Y") == "15.05.1990"
    print("✅ Add birthday (success) test passed!")


def test_update_birthday_success():
    """Test updating a birthday for a contact that already has one."""
    # Arrange
    book = ContactBook()
    book.create_contact("Bob", "0000000000")
    
    # Add initial birthday
    handler = AddBirthdayCommandHandler(book)
    handler._handle(["Bob", "10.03.1985"])
    
    # Act - update the birthday
    handler._handle(["Bob", "24.07.1992"])
    
    # Assert
    contact = book.find_contact("Bob")
    assert contact.birthday.value.strftime("%d.%m.%Y") == "24.07.1992"
    print("✅ Update birthday (success) test passed!")


def test_invalid_birthday_format():
    """Test handling of invalid birthday format."""
    # Arrange
    book = ContactBook()
    book.create_contact("Charlie", "1111111111")
    
    handler = AddBirthdayCommandHandler(book)
    
    # Capture output
    from io import StringIO
    import sys as sys_mod
    old_stdout = sys_mod.stdout
    sys_mod.stdout = captured = StringIO()
    
    # Act
    handler._handle(["Charlie", "1990-05-15"])  # Wrong format
    
    # Restore stdout
    sys_mod.stdout = old_stdout
    output = captured.getvalue()
    
    # Assert
    assert "Failed to set birthday" in output
    contact = book.find_contact("Charlie")
    assert contact.birthday is None
    print("✅ Invalid birthday format test passed!")


def test_contact_not_found():
    """Test handling when contact doesn't exist."""
    # Arrange
    book = ContactBook()
    handler = AddBirthdayCommandHandler(book)
    
    # Capture output
    from io import StringIO
    import sys as sys_mod
    old_stdout = sys_mod.stdout
    sys_mod.stdout = captured = StringIO()
    
    # Act
    handler._handle(["NonExistent", "15.05.1990"])
    
    # Restore stdout
    sys_mod.stdout = old_stdout
    output = captured.getvalue()
    
    # Assert
    assert "Contact 'NonExistent' not found." in output
    print("✅ Contact not found test passed!")


def test_multi_word_birthday_input():
    """Test that multi-word input is handled correctly (should treat as single birthday string)."""
    # Arrange
    book = ContactBook()
    book.create_contact("Diana", "2222222222")
    
    handler = AddBirthdayCommandHandler(book)
    
    # Act - this should fail because "15.05.1990 extra" is not a valid date
    from io import StringIO
    import sys as sys_mod
    old_stdout = sys_mod.stdout
    sys_mod.stdout = captured = StringIO()
    
    handler._handle(["Diana", "15.05.1990", "extra"])
    
    sys_mod.stdout = old_stdout
    output = captured.getvalue()
    
    # Assert - should fail validation
    assert "Failed to set birthday" in output
    contact = book.find_contact("Diana")
    assert contact.birthday is None
    print("✅ Multi-word birthday input test passed!")


def test_exact_date_format():
    """Test that the exact DD.MM.YYYY format works correctly."""
    # Arrange
    book = ContactBook()
    book.create_contact("Eve", "3333333333")
    
    handler = AddBirthdayCommandHandler(book)
    
    # Act
    handler._handle(["Eve", "01.01.2000"])
    
    # Assert
    contact = book.find_contact("Eve")
    assert contact.birthday.value.strftime("%d.%m.%Y") == "01.01.2000"
    print("✅ Exact date format test passed!")


def run_all_tests():
    """Run all birthday handler tests."""
    print("🧪 Starting AddBirthdayCommandHandler tests...\n")
    try:
        test_add_birthday_success()
        test_update_birthday_success()
        test_invalid_birthday_format()
        test_contact_not_found()
        test_multi_word_birthday_input()
        test_exact_date_format()
        print("\n🎉 All AddBirthdayCommandHandler tests passed!")
    except Exception as e:
        print(f"\n💥 Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    run_all_tests()