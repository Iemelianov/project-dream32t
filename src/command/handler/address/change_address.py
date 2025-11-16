"""Handler for the change-address command."""
from rich import print
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook
from src.model.name import Name
from src.model.address import Address
from src.util.messages import CONTACT_NOT_FOUND, ADDRESS_UPDATED, ADDRESS_NOT_FOUND
 


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
        name = Name(args[0])
        old_address = Address(args[1])
        new_address= Address(" ".join(args[1:]))

        contact = self.__address_book.find_contact_by_name(name)
        if contact is None:
            print(CONTACT_NOT_FOUND.format(name=name))
            return
        try:
            contact.update_address(old_address, new_address)
            print(ADDRESS_UPDATED.format(name=name) )
        except ValueError:
            print(ADDRESS_NOT_FOUND.format(name=name))
