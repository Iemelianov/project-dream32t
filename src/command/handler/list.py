"""Help command handler."""
from colorama import Fore, Style

from src.command.command_description import CommandDescriptor
from src.command.handler.command_handler import CommandHandler


class ListCommandHandler(CommandHandler):
    """Handles the "list" command functionality."""

    def __init__(self, handlers: dict[str, CommandHandler]):
        self.__handlers = handlers
        super().__init__(
            CommandDescriptor("list", "Displays the list of available commands.", )
        )

    def handle(self, args: list[str]) -> None:
        """Handles the command."""
        self._check_args(args)
        if len(self.__handlers) > 0:
            result = "The command list:\n"
            command_handlers = self.__handlers.values()
            indent = ListCommandHandler.__indent(command_handlers)
            for command_handler in command_handlers:
                result = result + self.__format_command(indent, command_handler)
            print(result)
        else:
            print("No commands available.")

    @staticmethod
    def __indent(command_handlers) -> int:
        """Returns the indent for the command list."""
        indent = 0
        for command_handler in command_handlers:
            indent = max(indent, len(command_handler.name))
        return indent

    @staticmethod
    def __format_command(indent: int, command_handler: CommandHandler) -> str:
        """Formats a command for display."""
        result = f"  {Fore.GREEN}{command_handler.name}{Style.RESET_ALL}"
        command_description = command_handler.description
        if command_description:
            indent = " " * (indent - len(command_handler.name) + 5)
            result = result + f"{indent}{Fore.YELLOW}{command_description}{Style.RESET_ALL}\n"
        else:
            result = result + "\n"

        return result
