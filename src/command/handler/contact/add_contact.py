"""Handler for the add-contact command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook
from src.model.phone import Phone


class AddContactCommandHandler(CommandHandler):
    """Handles the functionality to add a contact into an address book."""

    def __init__(self, address_book: ContactBook):
        self.__address_book = address_book
        super().__init__(
            CommandDefinition(
                "add-contact",
                "Adds a contact to the address book.",
                mandatory_arg("name", "Name of a contact."),
                mandatory_arg("phone", "Phone number of a contact.")
            )
        )


    def _handle(self, args: list[str]) -> None:
        """Adds an address to the specified contact."""
        name = args[0]
        phone = Phone(args[1])
        try:
            contact.create_contact(name,phone)
            print(f"Address added to contact '{name}'.")
        except ValueError as e:
            print(f"Failed to add address: {e}")
