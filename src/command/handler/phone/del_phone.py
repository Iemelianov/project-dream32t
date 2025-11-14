"""Handler for the del-phone command."""
from src.command.command_description import CommandDescriptor, arg_def
from src.command.handler.command_handler import CommandHandler


class DelPhoneCommandHandler(CommandHandler):
    """Handles the functionality to delete a phone number from a contact."""

    def __init__(self, address_book: dict[str, str]):
        self.__address_book = address_book
        super().__init__(
            CommandDescriptor(
                "del-phone",
                "Deletes a phone number from a a contact.",
                arg_def("name", "Name of a contact."),
                arg_def("phone", "The phone number to delete."),
            )
        )

    def handle(self, args: list[str]) -> None:
        """Handles the command."""
        self._check_args(args)
        print("Deleted a phone number.")
