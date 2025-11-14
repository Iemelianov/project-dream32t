"""Handler for the del-note command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.note import Notes


class DelNoteCommandHandler(CommandHandler):
    """Handles the functionality to delete a note from notes."""

    def __init__(self, notes: Notes):
        self.__notes = notes
        super().__init__(
            CommandDefinition(
                "del-note",
                "Deletes a note from notes.",
                mandatory_arg("name", "Name of a note."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        topic = args[0]
        is_done = self.__notes.delete_note(topic)
        if is_done:
            print("Deleted a note.")
        else:
            print("The note has not been delete")
