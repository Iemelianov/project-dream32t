"""Handler for the change-address command."""
from src.command.command_description import CommandDescriptor, arg_def
from src.command.handler.command_handler import CommandHandler


class ChangeAddressCommandHandler(CommandHandler):
    """Handles the functionality to change an address in a contact."""

    def __init__(self, address_book: dict[str, str]):
        self.__address_book = address_book
        super().__init__(
            CommandDescriptor(
                "change-address",
                "This command changes the address of a contact.",
                arg_def("name", "Name of a contact."),
                arg_def("old_email", "The old address that needs to be changed."),
                arg_def("new_email", "The new address to change to."),
            )
        )

    def handle(self, args: list[str]) -> None:
        """Handles the command."""
        self._check_args(args)
        print("Change an address.")
