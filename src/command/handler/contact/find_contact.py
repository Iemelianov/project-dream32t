"""Handler for the find-contact command."""

from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.command.handler.contact.show_contacts import show_contacts
from src.model.contact_book import ContactBook


class FindContactCommandHandler(CommandHandler):
    """Handles the functionality to find contact in the address book."""

    def __init__(self, contact_book: ContactBook):
        self.__contact_book = contact_book
        super().__init__(
            CommandDefinition(
                "find-contact",
                "Find contact(s) in the address book for defined search parameter.",
                mandatory_arg("parameter", "Search parameter, must be one of the " \
                              "following: name, phones, emails, addresses, birthday"),
                mandatory_arg("value", "Value to find"),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Find contact in the address book"""
        if args[0] not in ("name", "phones", "emails", "addresses", "birthday"):
            print(("Wrong parameter value, must be on of the following:"
                   "name, phones, emails, addresses, birthday"))
            return
        contact = self.__contact_book.find_contact_by_param(args[0], args[1])
        if not contact or not contact[0]:
            print(f"Contact with {args[0]}: '{args[1]}' not found.")
            return
        show_contacts(contact)
