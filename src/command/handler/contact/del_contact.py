"""Handler for the del-contact command."""
from rich import print

from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.command.handler.confirm_delete import confirm_delete
from src.model.contact_book import ContactBook
from src.model.name import Name

from src.util.messages import CONTACT_DELETED, CONTACT_NOT_FOUND

class DelContactCommandHandler(CommandHandler):
    """Handles the functionality to delete a contact from a contact book."""

    def __init__(self, contact_book: ContactBook):
        self.__contact_book = contact_book
        super().__init__(
            CommandDefinition(
                "del-contact",
                "Deletes a contact from a contact book.",
                mandatory_arg("name", "Name of a contact."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the del-contact command."""
        name = Name(args[0])

        is_confirmed = confirm_delete(f"the contact '{name.value}'")
        if not is_confirmed:
            return

        ret, _ = self.__contact_book.delete_contact(name.value)
        if ret:
            print(CONTACT_DELETED.format(name=args[0]))
        else:
            print(CONTACT_NOT_FOUND.format(name=args[0]))
