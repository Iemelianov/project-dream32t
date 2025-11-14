"""Help command handler."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDescriptor
from src.command.handler.command_handler import CommandHandler
from src.command.handler.command_handlers import CommandHandlers
from src.util.colorize import cmd_color


class HelpCommandHandler(CommandHandler):
    """Handles the "help" command functionality."""

    def __init__(self, handlers: CommandHandlers):
        self.__handlers = handlers
        super().__init__(
            CommandDescriptor(
                "help",
                "Displays help for a specific command.",
                mandatory_arg("command", "Name of the command for which help should be displayed.")
            )
        )

    def handle(self, args: list[str]) -> None:
        """Handles the command."""
        self._check_args(args)
        command_name = args[0]
        handler = self.__handlers.get(command_name, None)
        if handler is None:
            raise ValueError(f"Help for command: '{cmd_color(command_name)}' is not available.")
        print(handler.help())
