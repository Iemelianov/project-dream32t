"""
This module defines a class for managing and interacting with a command definition,
including its name, associated arguments, and a help string.

The `CommandDefinition` class provides properties to retrieve the name of the
command and the number of arguments. It also contains a method to retrieve
a descriptive help string for the command.
"""
from colorama import Fore, Style


def arg_def(name: str, description: str = "") -> tuple[str, str]:
    """Returns a tuple containing the name and description of an argument."""
    return name, description


class CommandDescriptor:
    """Represents a command descriptor with a name and associated arguments."""

    def __init__(self, name: str, description: str | None, *args: tuple[str, str]):
        self.__name = name.casefold()
        self.__description = description
        self.__args = args
        self.__help = CommandDescriptor.__help_format(name, *args)

    @property
    def name(self) -> str:
        """Returns the name of the command."""
        return self.__name

    @property
    def description(self) -> str | None:
        """Returns the description of the command."""
        return self.__description

    @property
    def args_count(self) -> int:
        """Returns the number of the command arguments."""
        return len(self.__args)

    def help(self) -> str:
        """Returns a formatted string representation of the command definition."""
        return self.__help

    @staticmethod
    def __help_format(name: str, *args: tuple[str, str]) -> str:
        result = (f"usage: {Fore.GREEN}{name} "
                  f"{Fore.BLUE}{" ".join(map(lambda a: a[0], args))}{Style.RESET_ALL}")
        if len(args) > 0:
            result = result + "\narguments:\n"
            indent = CommandDescriptor.__indent(*args)
            for arg in args:
                result = result + CommandDescriptor.__format_arg(indent, arg)
        return result

    @staticmethod
    def __indent(*args: tuple[str, str]) -> int:
        """Returns the indent for the argument list."""
        indent = 0
        for arg in args:
            indent = max(indent, len(arg[0]))
        return indent

    @staticmethod
    def __format_arg(indent: int, arg: tuple[str, str]) -> str:
        """Formats a command argument for display."""
        arg_name = arg[0]
        if arg_name.startswith("[") and arg_name.endswith("]"):
            arg_name = arg_name[1:-1]

        result = f" - {Fore.BLUE}{arg_name}{Style.RESET_ALL}"
        description = arg[1]
        if len(description) != 0:
            indent = " " * (indent - len(arg_name) + 5)
            result = result + f"{indent}{Fore.YELLOW}{description}{Style.RESET_ALL}\n"
        else:
            result = result + "\n"
        return result
