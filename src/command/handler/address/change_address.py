"""Handler for the change-address command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook


class ChangeAddressCommandHandler(CommandHandler):
    """Handles the functionality to change an address of a contact."""

    def __init__(self, address_book: ContactBook):
        self.__address_book = address_book
        super().__init__(
            CommandDefinition(
                "change-address",
                "Changes the address of a contact.",
                mandatory_arg("name", "Name of the contact."),
                mandatory_arg("new_address", "The new address to set."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Changes the contact's address to the new value."""
        name = args[0]
        new_address = " ".join(args[1:])

        contact = self.__address_book.find_contact(name)
        if contact is None:
            print(f"Contact '{name}' not found.")
            return

        try:
            contact.add_address(new_address)
            print(f"Address for '{name}' has been updated.")
        except ValueError as e:
            print(f"Failed to update address: {e}")
