"""Handler for the add-phone command."""
from src.command.command_description import CommandDescription
from src.command.handler.command_handler import CommandHandler


class AddPhoneCommandHandler(CommandHandler):
    """Handles the functionality to add a phone number into an address book."""

    def __init__(self, address_book: dict[str, str]):
        self.address_book = address_book
        super().__init__(CommandDescription("add-phone", "name", "phone"))

    def handle(self, args: list[str]) -> None:
        """Handles the command."""
        self._check_args(args)
        print(f"Adding phone {args[0]} {self.address_book}")
