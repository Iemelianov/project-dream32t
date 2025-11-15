"""Handler for the del-address command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook


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
        address_to_delete = " ".join(args[1:])

        contact = self.__address_book.find_contact(name)
        if contact is None:
            print(f"Contact '{name}' not found.")
            return

        # Check if contact has an address
        current_address = getattr(contact, 'address', None)
        if current_address is None or not hasattr(current_address, 'value'):
            print(f"Contact '{name}' has no address to delete.")
            return

        # Verify the provided address matches the current one
        if current_address.value != address_to_delete:
            print(f"The provided address does not match the current address for '{name}'.")
            return

        # Delete the address
        contact.address = None
        print(f"Address deleted for contact '{name}'.")
