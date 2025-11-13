"""Help command handler."""

from colorama import Fore, Style

from src.command.command_description import CommandDescription, arg_def
from src.command.handler.command_handler import CommandHandler


class HelpCommandHandler(CommandHandler):
    """Handles the "help" command functionality."""

    def __init__(self, handlers: dict[str, CommandHandler]):
        self.__handlers = handlers
        super().__init__(
            CommandDescription(
                "help",
                arg_def("command", "Name of the command for which help should be displayed.")
            )
        )

    def handle(self, args: list[str]) -> None:
        """Handles the command."""
        self._check_args(args)
        command_name = args[0]
        handler = self.__handlers.get(command_name, None)
        if handler is None:
            raise ValueError(f"{Fore.RED}[ERROR]{Style.RESET_ALL} "
                             f"Help for command: '{command_name}' is not available.")
        print(handler.help())
