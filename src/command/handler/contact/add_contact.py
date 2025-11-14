"""Handler for the add-contact command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler


class AddContactCommandHandler(CommandHandler):
    """Handles the functionality to add a contact into an address book."""

    def __init__(self, address_book: dict[str, str]):
        self.__address_book = address_book
        super().__init__(
            CommandDefinition(
                "add-contact",
                "Adds a contact to the address book.",
                mandatory_arg("name", "Name of a contact.")
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        print("Adding a contact.")
