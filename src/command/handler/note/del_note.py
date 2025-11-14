"""Handler for the del-note command."""
from src.command.command_description import CommandDescriptor, arg_def
from src.command.handler.command_handler import CommandHandler


class DelNoteCommandHandler(CommandHandler):
    """Handles the functionality to delete a note from notes."""

    def __init__(self, address_book: dict[str, str]):
        self.__address_book = address_book
        super().__init__(
            CommandDescriptor(
                "del-note",
                "Deletes a note from notes.",
                arg_def("name", "Name of a note."),
            )
        )

    def handle(self, args: list[str]) -> None:
        """Handles the command."""
        self._check_args(args)
        print("Deleted a note.")
