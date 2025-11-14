"""Help command handler."""

from src.command.command_argument import optional_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.command.handler.command_handlers import CommandHandlers
from src.util.colorize import cmd_color


class HelpCommandHandler(CommandHandler):
    """Handles the "help" command functionality."""

    def __init__(self, handlers: CommandHandlers):
        self.__handlers = handlers
        super().__init__(
            CommandDefinition(
                "help",
                "Displays a list of available commands or help for a specific command.",
                optional_arg("command", "Name of the command for which help should be displayed.")
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""
        if len(args) == 0:
            self.__handlers.show_list_available_commands()
        else:
            self.__show_help_for_command(args[0])

    def __show_help_for_command(self, command_name: str):
        """Shows help for a specific command."""
        handler = self.__handlers.get(command_name, None)
        if handler is None:
            raise ValueError(f"Help for command: '{cmd_color(command_name)}' is not available.")
        handler.show_usage()
