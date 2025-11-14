"""
Defines the `Command` class representing a command with a name and associated arguments.
"""


class Command:
    """Represents a command with a name and associated arguments."""

    def __init__(self, name: str, args: list[str]):
        self.__name = name
        self.__args = args

    @property
    def name(self) -> str:
        """Returns the name of the command."""
        return self.__name

    @property
    def args(self) -> list[str]:
        """Returns the arguments of the command."""
        return self.__args
