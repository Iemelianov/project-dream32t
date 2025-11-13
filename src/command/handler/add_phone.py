"""Handler for the add-phone command."""
from src.command.command_description import CommandDescriptor, arg_def
from src.command.handler.command_handler import CommandHandler


class AddPhoneCommandHandler(CommandHandler):
    """Handles the functionality to add a phone number into an address book."""

    def __init__(self, address_book: dict[str, str]):
        self.__address_book = address_book
        super().__init__(
            CommandDescriptor(
                "add-phone",
                None,
                arg_def("name", "Name of a contact."),
                arg_def("phone", "The phone number to add."),
            )
        )

    def handle(self, args: list[str]) -> None:
        """Handles the command."""
        self._check_args(args)
        print(f"Adding phone {args[0]} {self.__address_book}")
