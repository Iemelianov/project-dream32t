"""Handler for the add-contact command."""
from rich import print

from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook
from src.util.messages import ADD_CONTACT_SUCCESS


class AddContactCommandHandler(CommandHandler):
    """Handles the functionality to add a contact into an address book."""

    def __init__(self, contact_book: ContactBook):
        self.__contact_book = contact_book
        super().__init__(
            CommandDefinition(
                "add-contact",
                "Adds a contact to the address book.",
                mandatory_arg("name", "Name of a contact."),
                mandatory_arg("phone", "Phone number of a contact.")
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Adds an address to the specified contact."""
        name = args[0]
        phone = args[1]
        try:
            ret, _ = self.__contact_book.create_contact(name, phone)
            if ret:
                print(ADD_CONTACT_SUCCESS.format(name=name))
            else:
                print(f"Contact '{name}' already exist in the contact book")
        except ValueError as e:
            print(f"Failed to add contact: {e}")
