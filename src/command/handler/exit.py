"""Exit command handler."""
import sys

from colorama import Fore, Style

from src.command.command_description import CommandDescriptor
from src.command.handler.command_handler import CommandHandler


class ExitCommandHandler(CommandHandler):
    """Handles the "exit" command functionality."""

    def __init__(self):
        super().__init__(CommandDescriptor("exit", "Exits the program.", ))

    def _handle(self, _: list[str]) -> None:
        """Handles the command."""
        print(f"{Fore.BLUE}Good bye!{Style.RESET_ALL}")
        sys.exit(0)
