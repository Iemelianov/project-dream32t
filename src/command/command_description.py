"""
This module defines a class for managing and interacting with a command definition,
including its name, associated arguments, and a help string.

The `CommandDefinition` class provides properties to retrieve the name of the
command and the number of arguments. It also contains a method to retrieve
a descriptive help string for the command.
"""

from src.command.command_argument import CommandArgument
from src.util.colorize import description_color, arg_color, cmd_color


class CommandDescriptor:
    """Represents a command descriptor with a name and associated arguments."""

    def __init__(self, name: str, description: str | None, *args: CommandArgument):
        arguments = list(args)
        self.__name = name.casefold()
        self.__description = description
        self.__args = arguments
        self.__help = CommandDescriptor.__help_format(name, arguments)

    @property
    def name(self) -> str:
        """Returns the name of the command."""
        return self.__name

    @property
    def description(self) -> str | None:
        """Returns the description of the command."""
        return self.__description

    @property
    def count_mandatory_args(self) -> int:
        """Returns the number of the command arguments."""
        count = 0
        for arg in self.__args:
            if arg.is_required:
                count += 1
        return count

    @property
    def count_all_args(self) -> int:
        """Returns the number of the command arguments."""
        return len(self.__args)

    def help(self) -> str:
        """Returns a formatted string representation of the command definition."""
        return self.__help

    @staticmethod
    def __help_format(name: str, args: list[CommandArgument]) -> str:
        result = CommandDescriptor.__format_command_description(name, args)
        if len(args) > 0:
            result = result + "\narguments:\n"
            indent = CommandDescriptor.__indent(args)
            for arg in args:
                result = result + CommandDescriptor.__format_arg(indent, arg)
        return result

    @staticmethod
    def __format_command_description(name: str, args: list[CommandArgument]) -> str:
        return (
            f"usage: {cmd_color(name)} "
            f"{arg_color(" ".join(map(lambda a: CommandDescriptor.__arg_name_format(a), args)))}"
        )

    @staticmethod
    def __indent(args: list[CommandArgument]) -> int:
        """Returns the indent for the argument list."""
        indent = 0
        for arg in args:
            indent = max(indent, len(arg.name))
        return indent

    @staticmethod
    def __format_arg(indent: int, arg: CommandArgument) -> str:
        """Formats a command argument for display."""
        arg_name = arg.name
        result = f" - {arg_color(arg_name)}"
        description = arg.description
        if len(description) != 0:
            indent = " " * (indent - len(arg_name) + 5)
            result = result + f"{indent}{description_color(description)}\n"
        else:
            result = result + "\n"
        return result

    @staticmethod
    def __arg_name_format(arg: CommandArgument) -> str:
        """Formats the name of a command argument."""
        if arg.is_required:
            return f"<{arg_color(arg.name)}>"
        return f"[{arg_color(arg.name)}]"
