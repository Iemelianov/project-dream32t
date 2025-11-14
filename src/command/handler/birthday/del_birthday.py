"""Handler for the del-birthday command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler


class DelBirthdayCommandHandler(CommandHandler):
    """Handles the functionality to delete a birthday from a contact."""

    def __init__(self, address_book: dict[str, str]):
        self.__address_book = address_book
        super().__init__(
            CommandDefinition(
                "del-birthday",
                "Deletes a birthday from a contact.",
                mandatory_arg("name", "Name of a contact."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        print("Deleted  a birthday.")
