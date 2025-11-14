"""Exit command handler."""
import sys

import rich

from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler


class ExitCommandHandler(CommandHandler):
    """Handles the "exit" command functionality."""

    def __init__(self):
        super().__init__(CommandDefinition("exit", "Exits the program.", ))

    def _handle(self, _: list[str]) -> None:
        """Handles the command."""
        rich.print("[blue]Good bye![/blue]")
        sys.exit(0)
