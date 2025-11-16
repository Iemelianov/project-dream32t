"""Handler for the all-contacts command."""

from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.command.handler.contact.show_contacts import show_contacts
from src.model.contact_book import ContactBook


class AllContactsCommandHandler(CommandHandler):
    """Handles the functionality to list all contacts in the address book."""

    def __init__(self, contact_book: ContactBook):
        self.__contact_book = contact_book
        super().__init__(
            CommandDefinition(
                "all-contacts",
                "Shows all contacts in the address book."
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the all-contacts command."""
        contacts = list(self.__contact_book.values())
        show_contacts(contacts)
