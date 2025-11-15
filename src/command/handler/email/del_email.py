"""Handler for the del-email command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook
from src.model.email import Email
from src.model.name import Name


class DelEmailCommandHandler(CommandHandler):
    """Handles the functionality to delete an email address from a contact."""

    def __init__(self, address_book: ContactBook):
        self.__address_book = address_book
        super().__init__(
            CommandDefinition(
                "del-email",
                "Deletes an email address from a contact.",
                mandatory_arg("name", "Name of a contact."),
                mandatory_arg("email", "The email address to delete."),
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
        contact.remove_email(email)
        print("Deleted an email address.")
