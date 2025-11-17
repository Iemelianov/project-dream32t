"""
A module implementing a collection of command handlers.

This module defines the `CommandHandlers` class, a specialized dictionary
class for managing command handlers. It provides functionality to register
and retrieve command handlers and to view all registered command names.
"""
from collections import UserDict

from rich import box
from rich import print as rprint
from rich.table import Table

from src.command.handler.command_handler import CommandHandler
from src.util.messages import NO_COMMANDS_AVAILABLE, HELP_HEADER



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
        """Shows commands with maximum sass."""
        if not self.data:
            print(NO_COMMANDS_AVAILABLE)
            return

        table = Table(
            title=HELP_HEADER,
            header_style="bold yellow",
            border_style="red",
            box=box.ROUNDED,
            expand=True
        )

        table.add_column("Don't Break This", style="green bold", no_wrap=True)
        table.add_column("What It Pretends to Do", style="white", overflow="fold")

        for command_name in sorted(self.__handler_names):
            command_handler = self.data[command_name]
            table.add_row(
                f"[green]{command_handler.name}[/green]",
                f"[dim]{command_handler.description}[/dim]"
            )

        rprint(table)
        rprint("[dim]💡 Pro tip: Most of these actually work. Sometimes.[/dim]")
