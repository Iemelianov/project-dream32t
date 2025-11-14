"""Handler for the add-note command."""
from src.command.command_description import CommandDescriptor, arg_def
from src.command.handler.command_handler import CommandHandler


class AddNoteCommandHandler(CommandHandler):
    """Handles the functionality to add a note to notes."""

    def __init__(self, notes: dict[str, str]):
        self.__notes = notes
        super().__init__(
            CommandDescriptor(
                "add-note",
                "Adds a note to notes.",
                arg_def("name", "Name of a note."),
                arg_def("content", "The content of a note."),
                arg_def("[tags]", "The list tags of a note. Example: 'tag1,tag2,tag3'."),
            )
        )

    def handle(self, args: list[str]) -> None:
        """Handles the command."""
        self._check_args(args)
        print("Added a note.")
