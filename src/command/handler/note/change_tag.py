"""Handler for the change-tag command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.note import Notes


class ChangeTagCommandHandler(CommandHandler):
    """Handles the functionality to change a tag in note."""

    def __init__(self, notes: Notes):
        self.__notes = notes
        super().__init__(
            CommandDefinition(
                "change-tag",
                "This command changes the tag of note.",
                mandatory_arg("topic", "Topic of a note."),
                mandatory_arg("old_tag", "The old tag that needs to be changed."),
                mandatory_arg("new_tag", "The new tag to change to."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        topic = args[0]
        old_tag = args[1]
        naw_tag = args[2]
        is_done = self.__notes.edit_tag(topic, old_tag, naw_tag)
        if is_done:
            print("Changed the tag.")
        else:
            print("The tag has not been changed.")
