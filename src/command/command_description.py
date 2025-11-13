"""
This module defines a class for managing and interacting with a command definition,
including its name, associated arguments, and a help string.

The `CommandDefinition` class provides properties to retrieve the name of the
command and the number of arguments. It also contains a method to retrieve
a descriptive help string for the command.
"""
from colorama import Fore, Style


class CommandDescription:
    """Represents a command description with a name and associated arguments."""

    def __init__(self, name: str, *args: str):
        self.__name = name.casefold()
        self.__args = args
        self.__help = CommandDescription.__format(name, *args)

    @property
    def name(self) -> str:
        """Returns the name of the command."""
        return self.__name

    @property
    def args_count(self) -> int:
        """Returns the number of the command arguments."""
        return len(self.__args)

    def help(self) -> str:
        """Returns a formatted string representation of the command definition."""
        return self.__help

    @staticmethod
    def __format(name: str, *args: str) -> str:
        result = f"Command format: {Fore.GREEN}{name} {Fore.BLUE}{" ".join(args)}{Style.RESET_ALL}"
        if len(args) > 0:
            result = result + "\narguments:\n"
            for arg in args:
                result = result + CommandDescription.__format_arg(arg)
        return result

    @staticmethod
    def __format_arg(arg: str) -> str:
        """Formats a command argument for display."""
        return f" - {Fore.BLUE}{arg}{Style.RESET_ALL}\n"
