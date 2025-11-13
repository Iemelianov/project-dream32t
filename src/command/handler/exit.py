"""Exit command handler."""
import sys

from colorama import Fore, Style

from src.command.command_description import CommandDescription
from src.command.handler.command_handler import CommandHandler


class ExitCommandHandler(CommandHandler):
    """Handles the "exit" command functionality."""

    def __init__(self):
        super().__init__(CommandDescription("exit"))

    def handle(self, args: list[str]) -> None:
        """Handles the command."""
        self._check_args(args)
        print(f"{Fore.BLUE}Good bye!{Style.RESET_ALL}")
        sys.exit(0)
