"""Handler for the change-note command."""
from src.command.command_description import CommandDescriptor, arg_def
from src.command.handler.command_handler import CommandHandler


class ChangeNoteCommandHandler(CommandHandler):
    """Handles the functionality to change a note in notes."""

    def __init__(self, address_book: dict[str, str]):
        self.__address_book = address_book
        super().__init__(
            CommandDescriptor(
                "change-note",
                "This command changes the note of notes.",
                arg_def("name", "Name of a note."),
                arg_def("content", "The content of a note."),
            )
        )

    def handle(self, args: list[str]) -> None:
        """Handles the command."""
        self._check_args(args)
        print("Changed a note.")
