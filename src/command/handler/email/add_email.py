"""Handler for the add-email command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler


class AddEmailCommandHandler(CommandHandler):
    """Handles the functionality to add an email address to a contact."""

    def __init__(self, address_book: dict[str, str]):
        self.__address_book = address_book
        super().__init__(
            CommandDefinition(
                "add-email",
                "Adds an email address to a contact.",
                mandatory_arg("name", "Name of a contact."),
                mandatory_arg("email", "The email to add."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        print("Added an email address.")
