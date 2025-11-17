"""Handler for the del-tags command."""
from rich import print as rprint

from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.command.handler.confirm_delete import confirm_delete
from src.model.note import Notes
from src.util.messages import TAG_DELETED


class DelTagsCommandHandler(CommandHandler):
    """Handles the functionality to delete tags from note."""

    def __init__(self, notes: Notes):
        self.__notes = notes
        super().__init__(
            CommandDefinition(
                "del-tags",
                "Deletes tags from note.",
                mandatory_arg("topic", "Topic of a note."),
                mandatory_arg(
                    "tags",
                    "The list tags for deleting from a note. Example: 'tag1,tag2,tag3'."
                ),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        topic = args[0]
        tags = args[1]
        is_confirmed = confirm_delete(
            f"the tags '{tags}' from a note on topic '{topic}'"
        )
        if not is_confirmed:
            return

        is_done = self.__notes.delete_tags(topic, tags)
        if is_done == "Tags deleted.":
            rprint(TAG_DELETED.format(topic=topic))
        else:
            print("No such tags in the note.")
