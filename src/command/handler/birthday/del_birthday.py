"""Handler for the del-birthday command."""
from rich import print as rprint

from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.command.handler.confirm_delete import confirm_delete
from src.model.contact_book import ContactBook
from src.model.name import Name
from src.util.messages import CONTACT_NOT_FOUND, BIRTHDAY_DELETED, BIRTHDAY_NOT_FOUND


class DelBirthdayCommandHandler(CommandHandler):
    """Handles the functionality to delete a birthday from a contact."""

    def __init__(self, address_book: ContactBook):
        self.__address_book = address_book
        super().__init__(
            CommandDefinition(
                "del-birthday",
                "Deletes a birthday from a contact.",
                mandatory_arg("name", "Name of a contact."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Deletes the birthday from the specified contact if it matches."""
        name = Name(args[0])
        contact = self.__address_book.find_contact_by_name(name)
        if contact is None:
            rprint(CONTACT_NOT_FOUND.format(name=name))
            return

        if contact.birthday is None:
            rprint(BIRTHDAY_NOT_FOUND.format(name=name))
            return

        is_confirmed = confirm_delete(f"the birthday from contact '{name.value}'")
        if not is_confirmed:
            return
        contact.clear_birthday()
        rprint(BIRTHDAY_DELETED.format(name=name))
