"""Handler for the all-contacts command."""

from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.command.handler.contact.show_contacts import show_contacts


class AllContactsCommandHandler(CommandHandler):
    """Handles the functionality to list all contacts in the address book."""

    def __init__(self, address_book: dict[str, str]):
        self.__address_book = address_book
        super().__init__(
            CommandDefinition(
                "all-contacts",
                "Shows all contacts in the address book."
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the all-contacts command."""
        contacts = list(self.__address_book.values())
        show_contacts(contacts)
