"""Handler for the change-phone command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler


class ChangePhoneCommandHandler(CommandHandler):
    """Handles the functionality to change a phone number in a contact."""

    def __init__(self, address_book: dict[str, str]):
        self.__address_book = address_book
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
        print("Changed a phone number.")
