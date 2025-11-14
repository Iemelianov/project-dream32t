"""Handler for the del-email command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler


class DelEmailCommandHandler(CommandHandler):
    """Handles the functionality to delete an email address from a contact."""

    def __init__(self, address_book: dict[str, str]):
        self.__address_book = address_book
        super().__init__(
            CommandDefinition(
                "del-email",
                "Deletes an email address from a contact.",
                mandatory_arg("name", "Name of a contact."),
                mandatory_arg("phone", "The email address to delete."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        print("Deleted an email address.")
