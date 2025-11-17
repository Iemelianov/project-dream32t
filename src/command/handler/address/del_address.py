"""Handler for the del-address command."""
from rich import print
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.command.handler.confirm_delete import confirm_delete
from src.model.address import Address
from src.model.contact_book import ContactBook
from src.model.name import Name
from src.util.messages import CONTACT_NOT_FOUND, ADDRESS_DELETED, ADDRESS_NOT_FOUND


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
        name = Name(args[0])
        address_to_delete = Address(args[1])

        contact = self.__address_book.find_contact_by_name(name)
        if contact is None:
            print(CONTACT_NOT_FOUND.format(name=name))
            return

        is_confirmed = confirm_delete(
            f"the address '{address_to_delete.value}' from contact '{name.value}'"
        )
        if not is_confirmed:
            return

        try:
            contact.remove_address(address_to_delete)
            print(ADDRESS_DELETED.format(name=name))
        except ValueError:
            print(ADDRESS_NOT_FOUND.format(name=name))
