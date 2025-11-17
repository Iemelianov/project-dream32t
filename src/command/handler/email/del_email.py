"""Handler for the del-email command."""
from rich import print as rprint

from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.command.handler.confirm_delete import confirm_delete
from src.model.contact_book import ContactBook
from src.model.email import Email
from src.model.name import Name
from src.util.messages import CONTACT_NOT_FOUND, EMAIL_DELETED


class DelEmailCommandHandler(CommandHandler):
    """Handles the functionality to delete an email address from a contact."""

    def __init__(self, contact_book: ContactBook):
        self.__contact_book = contact_book
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
        contact = self.__contact_book.find_contact_by_name(name)
        if contact is None:
            rprint(CONTACT_NOT_FOUND.format(name=name))
            return

        is_confirmed = confirm_delete(
            f"the email '{email.value}' from contact '{name.value}'"
        )
        if not is_confirmed:
            return

        contact.remove_email(email)
        rprint(EMAIL_DELETED.format(name=name))
