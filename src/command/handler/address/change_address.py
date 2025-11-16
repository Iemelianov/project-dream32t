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
                "Changes an existing address of a contact to a new one.",
                mandatory_arg("name", "Name of the contact."),
                mandatory_arg("old_address", "The current address to replace."),
                mandatory_arg("new_address", "The new address to set."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Changes an existing address of the specified contact."""
        name = args[0]
        old_address = args[1]
        new_address= " ".join(args[2:])

        contact = self.__address_book.find_contact_by_name(name)
        if contact is None:
            print("Contact not found.")
            return
        try:
            contact.update_address(old_address, new_address)
            print("Changed a address.")
        except ValueError:
            print(f"Address not found for contact '{name}'.")
