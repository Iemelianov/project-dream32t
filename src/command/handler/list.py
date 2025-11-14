"""Help command handler."""

from src.command.command_description import CommandDescriptor
from src.command.handler.command_handler import CommandHandler
from src.command.handler.command_handlers import CommandHandlers
from src.util.colorize import cmd_color, description_color


class ListCommandHandler(CommandHandler):
    """Handles the "list" command functionality."""

    def __init__(self, handlers: CommandHandlers):
        self.__handlers = handlers
        super().__init__(
            CommandDescriptor("list", "Displays the list of available commands.", )
        )

    def handle(self, args: list[str]) -> None:
        """Handles the command."""
        self._check_args(args)
        if len(self.__handlers) > 0:
            result = "The command list:\n"
            command_names = self.__handlers.names
            indent = ListCommandHandler.__indent(command_names)
            for command_name in command_names:
                command_handler = self.__handlers[command_name]
                result = result + self.__format_command(indent, command_handler)
            print(result)
        else:
            print("No commands available.")

    @staticmethod
    def __indent(command_names: list[str]) -> int:
        """Returns the indent for the command list."""
        indent = 0
        for command_name in command_names:
            indent = max(indent, len(command_name))
        return indent

    @staticmethod
    def __format_command(indent: int, command_handler: CommandHandler) -> str:
        """Formats a command for display."""
        result = f"  {cmd_color(command_handler.name)}"
        command_description = command_handler.description
        if command_description:
            indent = " " * (indent - len(command_handler.name) + 5)
            result = result + f"{indent}{description_color(command_description)}\n"
        else:
            result = result + "\n"

        return result
