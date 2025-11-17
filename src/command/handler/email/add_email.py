"""Handler for the add-email command."""
from rich import print

from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook
from src.model.email import Email
from src.model.name import Name
from src.util.messages import CONTACT_NOT_FOUND, EMAIL_ADDED


class AddEmailCommandHandler(CommandHandler):
    """Handles the functionality to add an email address to a contact."""

    def __init__(self, contact_book: ContactBook):
        self.__contact_book = contact_book
        super().__init__(
            CommandDefinition(
                "add-email",
                "Adds an email address to a contact.",
                mandatory_arg("name", "Name of a contact."),
                mandatory_arg("email", "The email to add."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        name = Name(args[0])
        email = Email(args[1])
        contact = self.__contact_book.find_contact_by_name(name)
        if contact is None:
            print(CONTACT_NOT_FOUND.format(name=name))
            return
        contact.add_email(email)
        print(EMAIL_ADDED.format(name=name))
