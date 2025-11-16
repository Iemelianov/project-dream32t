"""Handler for the find-contact command."""

from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.command.handler.contact.show_contacts import show_contacts
from src.model.contact_book import ContactBook
from src.model.name import Name


class FindContactCommandHandler(CommandHandler):
    """Handles the functionality to find contact in the address book."""

    def __init__(self, address_book: ContactBook):
        self.__address_book = address_book
        super().__init__(
            CommandDefinition(
                "find-contact",
                "Find contact in the address book.",
                mandatory_arg("name", "Name of a contact."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Find contact in the address book"""
        name = Name(args[0])
        contact = self.__address_book.find_contact_by_name(name)
        if contact is None:
            print(f"Contact '{args[0]}' not found.")
            return
        show_contacts([contact])
