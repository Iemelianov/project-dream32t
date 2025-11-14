"""Base class for command handlers."""
import rich

from src.command.command_description import CommandDefinition
from src.util.colorize import error_color


class CommandHandler:
    """Base class for command handlers."""

    def __init__(self, definition: CommandDefinition):
        self.__definition = definition

    def handle(self, args: list[str]) -> None:
        """Handles the command."""
        try:
            self.__check_args(args)
        except ValueError as e:
            rich.print(f"{error_color('[ERROR]')}: " + str(e))
            self.show_usage()
            return

        self._handle(args)

    @property
    def name(self) -> str:
        """Returns the name of the command."""
        return self.__definition.name

    @property
    def description(self) -> str:
        """Returns the description of the command."""
        return self.__definition.description

    def show_usage(self) -> None:
        """Returns the help message for the command."""
        return self.__definition.show_usage()

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""

    def __check_args(self, args: list[str]) -> None:
        """Checks if the number of command arguments matches the expected number."""
        if (len(args) < self.__definition.count_mandatory_args or
                len(args) > self.__definition.count_all_args):
            raise ValueError("Invalid command arguments.")
