"""Handler for the del-phone command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler


class DelPhoneCommandHandler(CommandHandler):
    """Handles the functionality to delete a phone number from a contact."""

    def __init__(self, address_book: dict[str, str]):
        self.__address_book = address_book
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
        print("Deleted a phone number.")
