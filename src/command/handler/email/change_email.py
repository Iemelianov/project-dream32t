"""Handler for the change-email command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook
from src.model.email import Email
from src.model.name import Name


class ChangeEmailCommandHandler(CommandHandler):
    """Handles the functionality to change an email address in a contact."""

    def __init__(self, contact_book: ContactBook):
        self.__contact_book = contact_book
        super().__init__(
            CommandDefinition(
                "change-email",
                "This command changes the email address of a contact.",
                mandatory_arg("name", "Name of a contact."),
                mandatory_arg("old_email", "The old email address that needs to be changed."),
                mandatory_arg("new_email", "The new email address to change to."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        name = Name(args[0])
        old_email = Email(args[1])
        new_email = Email(args[1])
        contact = self.__contact_book.find_contact_by_name(name)
        if contact is None:
            print("Contact not found.")
            return
        contact.update_email(old_email, new_email)
        print("Change an email address.")
