"""Handler for the sort-notes-tags command."""
from rich import print as rprint

from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.command.handler.note.show_notes import show_notes
from src.model.note import Notes
from src.util.messages import NO_NOTES_TO_SORT



class SortNotesByTagCommandHandler(CommandHandler):
    """Handles the functionality to find a note in notes."""

    def __init__(self, notes: Notes):
        self.__notes = notes
        super().__init__(
            CommandDefinition(
                "sort-notes-tags",
                "Sort all notes by their tags in alphabetical order.",
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        ret = self.__notes.sort_by_tag()
        if ret is None:
            rprint(NO_NOTES_TO_SORT)
        else:
            show_notes(ret)
