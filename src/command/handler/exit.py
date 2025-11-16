"""Exit command handler."""
import sys
from rich import print


from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.util.messages import get_goodbye_message


class ExitCommandHandler(CommandHandler):
    """Handles the "exit" command functionality."""

    def __init__(self):
        super().__init__(CommandDefinition("exit", "Exits the program.", ))

    def _handle(self, _: list[str]) -> None:
        """Handles the command."""
        print(get_goodbye_message())
        sys.exit(0)
