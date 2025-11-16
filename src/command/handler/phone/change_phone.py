"""Handler for the change-phone command."""
from rich import print

from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook
from src.model.name import Name
from src.model.phone import Phone
from src.util.messages import CONTACT_NOT_FOUND, PHONE_UPDATED


class ChangePhoneCommandHandler(CommandHandler):
    """Handles the functionality to change a phone number in a contact."""

    def __init__(self, contact_book: ContactBook):
        self.__contact_book = contact_book
        super().__init__(
            CommandDefinition(
                "change-phone",
                "This command changes the phone number of a contact.",
                mandatory_arg("name", "Name of a contact."),
                mandatory_arg("old_phone", "The old phone number that needs to be changed."),
                mandatory_arg("new_phone", "The new phone number to change to."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        name = Name(args[0])
        old_phone = Phone(args[1])
        new_phone = Phone(args[2])
        contact = self.__contact_book.find_contact_by_name(name)
        if contact is None:
            print(CONTACT_NOT_FOUND.format(name=name))
            return
        contact.update_phone(old_phone, new_phone)
        print(PHONE_UPDATED.format(name=name, phone=new_phone))
