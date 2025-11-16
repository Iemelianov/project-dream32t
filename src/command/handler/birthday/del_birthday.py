"""Handler for the del-birthday command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook


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
        name = args[0]
        contact = self.__address_book.find_contact(name)
        if contact is None:
            print("Contact not found.")
            return
        if contact.birthday is None:
            print(f"Contact '{name}' has no birthday to delete.")
        else:
            contact.clear_birthday()
            print(f"Birthday deleted for contact '{name}'.")
