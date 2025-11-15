"""Handler for the add-email command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook
from src.model.email import Email
from src.model.name import Name


class AddEmailCommandHandler(CommandHandler):
    """Handles the functionality to add an email address to a contact."""

    def __init__(self, address_book: ContactBook):
        self.__address_book = address_book
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
        contact = self.__address_book.find_contact_by_name(name)
        if contact is None:
            print("Contact not found.")
            return
        contact.add_email(email)
        print("Added an email address.")
