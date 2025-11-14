"""Handler for the change-note command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDescriptor
from src.command.handler.command_handler import CommandHandler


class ChangeNoteCommandHandler(CommandHandler):
    """Handles the functionality to change a note in notes."""

    def __init__(self, address_book: dict[str, str]):
        self.__address_book = address_book
        super().__init__(
            CommandDescriptor(
                "change-note",
                "This command changes the note of notes.",
                mandatory_arg("name", "Name of a note."),
                mandatory_arg("content", "The content of a note."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        print("Changed a note.")
