"""Handler for the del-phone command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook
from src.model.name import Name
from src.model.phone import Phone


class DelPhoneCommandHandler(CommandHandler):
    """Handles the functionality to delete a phone number from a contact."""

    def __init__(self, contact_book: ContactBook):
        self.__contact_book = contact_book
        super().__init__(
            CommandDefinition(
                "del-phone",
                "Deletes a phone number from a a contact.",
                mandatory_arg("name", "Name of a contact."),
                mandatory_arg("phone", "The phone number to delete."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        name = Name(args[0])
        phone = Phone(args[1])
        contact = self.__contact_book.find_contact_by_name(name)
        if contact is None:
            print("Contact not found.")
            return
        contact.remove_phone(phone)
        print("Deleted a phone number.")
