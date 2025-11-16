"""Handler for the del-note command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.command.handler.confirm_delete import confirm_delete
from src.model.note import Notes


class DelNoteCommandHandler(CommandHandler):
    """Handles the functionality to delete a note from notes."""

    def __init__(self, notes: Notes):
        self.__notes = notes
        super().__init__(
            CommandDefinition(
                "del-note",
                "Deletes a note from notes.",
                mandatory_arg("topic", "Topic of a note."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        topic = args[0]

        is_confirmed = confirm_delete(f"a note on topic '{topic}'")
        if not is_confirmed:
            return

        print(self.__notes.delete_note(topic))
