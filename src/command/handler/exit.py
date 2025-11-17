"""Exit command handler."""
import sys
from rich import print as rprint


from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook
from src.model.note import Notes
from src.util.messages import get_goodbye_message


class ExitCommandHandler(CommandHandler):
    """Handles the "exit" command functionality."""

    def __init__(self,  address_book: ContactBook, notes: Notes):
        super().__init__(CommandDefinition("exit", "Exits the program.", ))
        self.address_book = address_book
        self.notes = notes

    def _handle(self, _: list[str]) -> None:
        """Handles the command."""
        # Save with message on exit
        self.address_book.save_to_storage(silent=False)
        self.notes.save_to_storage(silent=False)
        rprint(get_goodbye_message())
        sys.exit(0)
