"""Handler for the del-contact command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler


class DelContactCommandHandler(CommandHandler):
    """Handles the functionality to delete a contact from a contact book."""

    def __init__(self, address_book: dict[str, str]):
        self.__address_book = address_book
        super().__init__(
            CommandDefinition(
                "del-contact",
                "Deletes a contact from a contact book.",
                mandatory_arg("name", "Name of a contact."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        print("Deleted a contact.")
