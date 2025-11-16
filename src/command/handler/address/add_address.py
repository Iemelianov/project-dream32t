"""Handler for the add-address command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook
from src.model.address import Address



class AddAddressCommandHandler(CommandHandler):
    """Handles the functionality to add an address to a contact."""

    def __init__(self, address_book: ContactBook ):
        self.__address_book = address_book
        super().__init__(
            CommandDefinition(
                "add-address",
                "Adds an address to a contact.",
                mandatory_arg("name", "Name of the contact."),
                mandatory_arg("address", "The address to add."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Adds an address to the specified contact."""
        name = args[0]
        address = Address( " ".join(args[1:]))

        contact = self.__address_book.find_contact(name)
        if contact is None:
            print(f"Contact '{name}' not found.")
            return

        try:
            contact.add_address(address)
            print(f"Address added to contact '{name}'.")
        except ValueError as e:
            print(f"Failed to add address: {e}")

