"""
A module implementing a collection of command handlers.

This module defines the `CommandHandlers` class, a specialized dictionary
class for managing command handlers. It provides functionality to register
and retrieve command handlers and to view all registered command names.
"""
from collections import UserDict

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
        self.__handler_names.append(handler.name)

    def __getitem__(self, command_name: str) -> CommandHandler | None:
        return self.data.get(command_name, None)

    @property
    def names(self) -> list[str]:
        """Returns the names of all registered commands."""
        return self.__handler_names
