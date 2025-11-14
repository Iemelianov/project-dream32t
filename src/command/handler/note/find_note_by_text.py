"""Handler for thenote-by-text command."""
from model.note import Notes, NoteEntity
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDescriptor
from src.command.handler.command_handler import CommandHandler


class FindNoteByTextCommandHandler(CommandHandler):
    """Handles the functionality to find a note in notes."""

    def __init__(self, notes: Notes):
        self.__notes = notes
        super().__init__(
            CommandDescriptor(
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
            self.show_notes(notes)
        else:
            print("No notes found.")

    def show_notes(self, notes: list[NoteEntity]) -> None:
        """Shows the notes."""
        for note in notes:
            print(note.content)
