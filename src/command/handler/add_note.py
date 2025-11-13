"""Handler for the add-note command."""
from src.command.command_description import CommandDescription
from src.command.handler.command_handler import CommandHandler


class AddNoteCommandHandler(CommandHandler):
    """Handles the functionality to add a note into a notes."""

    def __init__(self, notes: dict[str, str]):
        self.__notes = notes
        super().__init__(CommandDescription("add-note", "topic", "content", "[tags]"))

    def handle(self, args: list[str]) -> None:
        """Handles the command."""
        self._check_args(args)
        print(f"Adding note {args[0]} {self.__notes}")
