"""Handler for the del-address command."""
from src.command.command_description import CommandDescriptor, arg_def
from src.command.handler.command_handler import CommandHandler


class DelAddressCommandHandler(CommandHandler):
    """Handles the functionality to delete an email address from a contact."""

    def __init__(self, address_book: dict[str, str]):
        self.__address_book = address_book
        super().__init__(
            CommandDescriptor(
                "del-address",
                "Deletes an address from a contact.",
                arg_def("name", "Name of a contact."),
                arg_def("phone", "The address to delete."),
            )
        )

    def handle(self, args: list[str]) -> None:
        """Handles the command."""
        self._check_args(args)
        print("Deleted an address.")
