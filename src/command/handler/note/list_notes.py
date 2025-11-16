"""Handler for the list-notes command."""

from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.command.handler.note.show_notes import show_notes
from src.model.note import Notes


class ListNoteTextCommandHandler(CommandHandler):
    """Handles the functionality to find a note in notes."""

    def __init__(self, notes: Notes):
        self.__notes = notes
        super().__init__(
            CommandDefinition(
                "list-notes",
                "Show all notes.",
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        show_notes(self.__notes.data)
