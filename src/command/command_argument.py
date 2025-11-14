"""
Defines a `CommandArgument` class to represent a command-line argument
with its associated properties such as name, description, and whether
it is required.
"""


class CommandArgument:
    """Represents a command argument with a name and a description."""

    def __init__(self, name: str, description: str, is_required: bool = True):
        self.__name = name
        self.__description = description
        self.__is_required = is_required

    @property
    def name(self) -> str:
        """Returns the name of the command argument."""
        return self.__name

    @property
    def description(self) -> str:
        """Returns the description of the command argument."""
        return self.__description

    @property
    def is_required(self) -> bool:
        """Returns whether the command argument is required."""
        return self.__is_required


def mandatory_arg(name: str, description: str) -> CommandArgument:
    """Defines a mandatory argument with a name and description."""
    return CommandArgument(name, description)


def optional_arg(name: str, description: str = "") -> CommandArgument:
    """Defines an optional argument with a name and description."""
    return CommandArgument(name, description, is_required=False)
