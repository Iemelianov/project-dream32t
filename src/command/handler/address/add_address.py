"""Handler for the add-address command."""
from rich import print as rprint

from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook
from src.model.name import Name
from src.model.address import Address
from src.util.messages import INVALID_ADDRESS, ADDRESS_ADDED, CONTACT_NOT_FOUND



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
        name = Name(args[0])
        address = Address(args[1])
        contact = self.__address_book.find_contact_by_name(name)
        if contact is None:
            rprint(CONTACT_NOT_FOUND.format(name=name))
            return

        try:
            contact.add_address(address)
            rprint(ADDRESS_ADDED.format(name=name))
        except ValueError:
            rprint(INVALID_ADDRESS)
