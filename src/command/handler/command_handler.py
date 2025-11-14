"""Base class for command handlers."""

from src.command.command_description import CommandDescriptor


class CommandHandler:
    """Base class for command handlers."""

    def __init__(self, definition: CommandDescriptor):
        self.__definition = definition

    def handle(self, args: list[str]) -> None:
        """Handles the command."""
        self.__check_args(args)
        self._handle(args)

    @property
    def name(self) -> str:
        """Returns the name of the command."""
        return self.__definition.name

    @property
    def description(self) -> str:
        """Returns the description of the command."""
        return self.__definition.description

    def help(self) -> str:
        """Returns the help message for the command."""
        return self.__definition.help()

    def _handle(self, args: list[str]) -> None:
        """Handles the command."""

    def __check_args(self, args: list[str]) -> None:
        """Checks if the number of command arguments matches the expected number."""
        if (len(args) < self.__definition.count_mandatory_args or
                len(args) > self.__definition.count_all_args):
            raise ValueError(f"Invalid command arguments.\n{self.help()}")
