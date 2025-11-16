"""Handler for the del-address command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook
from src.model.address import Address


class DelAddressCommandHandler(CommandHandler):
    """Handles the functionality to delete an address from a contact."""

    def __init__(self, address_book: ContactBook):
        self.__address_book = address_book
        super().__init__(
            CommandDefinition(
                "del-address",
                "Deletes an address from a contact.",
                mandatory_arg("name", "Name of the contact."),
                mandatory_arg("address", "The address to delete (must match exactly)."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Deletes the address from the specified contact if it matches."""
        name = args[0]
        address_to_delete = Address(" ".join(args[1:]))

        contact = self.__address_book.find_contact_by_name(name)
        if contact is None:
            print("Contact not found.")
            return
        try:
            contact.remove_address(address_to_delete)
            print(f"Address deleted for contact '{name}'.")
        except ValueError:
            print(f"Address not found for contact '{name}'.")
