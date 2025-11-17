"""Handler for the note-by-text command."""
from rich import print as rprint

from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.command.handler.note.show_notes import show_notes
from src.model.note import Notes, NoteEntity
from src.util.messages import NOTE_NOT_FOUND


class FindNoteByTextCommandHandler(CommandHandler):
    """Handles the functionality to find a note in notes."""

    def __init__(self, notes: Notes):
        self.__notes = notes
        super().__init__(
            CommandDefinition(
                "note-by-text",
                "Finds a note in notes by text.",
                mandatory_arg("text", "The text to search for."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        text = args[0]
        notes: list[NoteEntity] = self.__notes.find_text_in_notes(text)
        if notes:
            show_notes(notes)
        else:
            rprint(NOTE_NOT_FOUND)
