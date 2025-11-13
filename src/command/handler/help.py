"""Help command handler."""

# from colorama import Fore, Style

from src.command.command_description import CommandDescriptor, arg_def
from src.command.handler.command_handler import CommandHandler
from src.util.format import cmd_color, error_color


class HelpCommandHandler(CommandHandler):
    """Handles the "help" command functionality."""

    def __init__(self, handlers: dict[str, CommandHandler]):
        self.__handlers = handlers
        super().__init__(
            CommandDescriptor(
                "help",
                "Displays help for a specific command.",
                arg_def("command", "Name of the command for which help should be displayed.")
            )
        )

    def handle(self, args: list[str]) -> None:
        """Handles the command."""
        self._check_args(args)
        command_name = args[0]
        handler = self.__handlers.get(command_name, None)
        if handler is None:
            raise ValueError(f"{error_color('[ERROR]')} "
                             f"Help for command: '{cmd_color(command_name)}' is not available.")
        print(handler.help())
