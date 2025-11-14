"""Handler for the change-email command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler


class ChangeEmailCommandHandler(CommandHandler):
    """Handles the functionality to change an email address in a contact."""

    def __init__(self, address_book: dict[str, str]):
        self.__address_book = address_book
        super().__init__(
            CommandDefinition(
                "change-email",
                "This command changes the email address of a contact.",
                mandatory_arg("name", "Name of a contact."),
                mandatory_arg("old_email", "The old email address that needs to be changed."),
                mandatory_arg("new_email", "The new email address to change to."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        print("Change an email address.")
