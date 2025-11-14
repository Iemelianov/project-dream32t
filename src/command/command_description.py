"""
This module defines a class for managing and interacting with a command definition,
including its name, associated arguments, and a help string.

The `CommandDefinition` class provides properties to retrieve the name of the
command and the number of arguments. It also contains a method to retrieve
a descriptive help string for the command.
"""

import rich
from rich.table import Table

from src.command.command_argument import CommandArgument
from src.util.colorize import cmd_color, arg_color


class CommandDefinition:
    """Represents a command definition with a name and associated arguments."""

    def __init__(self, name: str, description: str | None, *args: CommandArgument):
        self.__name = name
        self.__description = description
        self.__args = args

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

    def show_usage(self):
        """Returns a formatted string representation of the command definition."""
        rich.print(
            f"usage: {cmd_color(self.__name)} "
            f"{" ".join(map(lambda a: CommandDefinition.__arg_name_format(a), self.__args))}"
        )
        if len(self.__args) > 0:
            table = Table(box=None, show_header=False)
            table.add_column("Arguments", justify="left", style="blue", no_wrap=True)
            table.add_column("Description", justify="left", style="yellow")
            for arg in self.__args:
                table.add_row(" - " + arg.name, arg.description)
            rich.print(table)

    @staticmethod
    def __arg_name_format(arg: CommandArgument) -> str:
        """Formats the name of a command argument."""
        return f"<{arg_color(arg.name)}>" if arg.is_required else f"[{arg_color(arg.name)}]"
