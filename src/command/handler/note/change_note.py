"""Handler for the change-note command."""
from model.note import Notes
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDescriptor
from src.command.handler.command_handler import CommandHandler


class ChangeNoteCommandHandler(CommandHandler):
    """Handles the functionality to change a note in notes."""

    def __init__(self, notes: Notes):
        self.__notes = notes
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
        topic = args[0]
        content = args[1]
        is_done = self.__notes.edit_note(topic, content)
        if is_done:
            print("Changed the note.")
        else:
            print("The note has not been changed")
