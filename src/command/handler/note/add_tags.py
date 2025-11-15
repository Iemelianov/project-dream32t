"""Handler for the add-tags command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.note import Notes


class AddTagsCommandHandler(CommandHandler):
    """Handles the functionality to add tags to note."""

    def __init__(self, notes: Notes):
        self.__notes = notes
        super().__init__(
            CommandDefinition(
                "add-tags",
                "Adds tags to note.",
                mandatory_arg("topic", "Topic of a note."),
                mandatory_arg(
                    "tags",
                    "The list tags for adding to a note. Example: 'tag1,tag2,tag3'."
                ),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        topic = args[0]
        tags = args[1]
        self.__notes.add_tag(topic, tags)
        print("Added tags.")
