"""Handler for the add-contact command."""

from src.command.command_description import CommandDescriptor, arg_def
from src.command.handler.command_handler import CommandHandler


class AddContactCommandHandler(CommandHandler):
    """Handles the functionality to add a contact into an address book."""

    def __init__(self, address_book: dict[str, str]):
        self.__address_book = address_book
        super().__init__(
            CommandDescriptor(
                "add-contact",
                "Adds a contact to the address book.",
                arg_def("name", "Name of a contact.")
            )
        )

    def handle(self, args: list[str]) -> None:
        """Handles the command."""
        self._check_args(args)

        print(f"Adding contact {args[0]} {self.__address_book}")
