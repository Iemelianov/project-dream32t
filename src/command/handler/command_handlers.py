"""
A module implementing a collection of command handlers.

This module defines the `CommandHandlers` class, a specialized dictionary
class for managing command handlers. It provides functionality to register
and retrieve command handlers and to view all registered command names.
"""
from collections import UserDict

import rich
from rich.table import Table

from src.command.handler.command_handler import CommandHandler


class CommandHandlers(UserDict[str, CommandHandler]):
    """A collection of command handlers."""

    def __init__(self):
        self.__handler_names = []
        super().__init__()

    def register(self, handler: CommandHandler) -> None:
        """Registers a new command handler."""
        command_name = handler.name.casefold()
        if command_name in self.data:
            raise ValueError(f"Command handler already registered for command: '{command_name}'.")
        self.data[command_name] = handler
        self.__handler_names.append(command_name)

    def __getitem__(self, command_name: str) -> CommandHandler | None:
        return self.data.get(command_name, None)

    def show_list_available_commands(self) -> None:
        """Shows a list of available commands."""
        if len(self.data) > 0:
            print("The command list:")
            table = Table(box=None)
            table.add_column("Command", justify="left", style="green", no_wrap=True)
            table.add_column("Description", justify="left", style="yellow")
            for command_name in self.__handler_names:
                command_handler = self.data[command_name]
                table.add_row(command_handler.name, command_handler.description)
            rich.print(table)
        else:
            print("No commands available.")
