"""Handler for the add-note command."""
from src.command.command_argument import mandatory_arg, optional_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.note import Notes


class AddNoteCommandHandler(CommandHandler):
    """Handles the functionality to add a note to notes."""

    def __init__(self, notes: Notes):
        self.__notes = notes
        super().__init__(
            CommandDefinition(
                "add-note",
                "Adds a note to notes.",
                mandatory_arg("topic", "Topic of a note."),
                mandatory_arg("content", "The content of a note."),
                optional_arg("tags", "The list tags of a note. Example: 'tag1,tag2,tag3'."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        topic = args[0]
        content = args[1]
        if len(args) > 2:
            tags = args[2]
        else:
            tags = None
        self.__notes.add_note(topic, content, tags)
        print("Added a note.")
