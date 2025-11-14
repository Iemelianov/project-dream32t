"""Handler for the note-by-tag command."""

from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.command.handler.note.show_notes import show_notes
from src.model.note import Notes, NoteEntity


class FindNoteByTagCommandHandler(CommandHandler):
    """Handles the functionality to find a note in notes."""

    def __init__(self, notes: Notes):
        self.__notes = notes
        super().__init__(
            CommandDefinition(
                "note-by-tag",
                "Finds a note in notes by tag.",
                mandatory_arg("tags", "The tag to search for."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        tag = args[0]
        notes: list[NoteEntity] = self.__notes.search_by_tag(tag)
        if notes:
            show_notes(notes)
        else:
            print("No notes found.")
