"""
This module provides the implementation for a personal assistant system that
interprets user commands and performs a set of pre-defined actions. It includes
a command parsing mechanism and dynamically assigns handlers to manage specific
commands.

The `PersonalAssistant` class acts as the main interface for the system, allowing
users to interact with a series of commands such as adding contacts, adding notes,
or exiting the application.
"""
from typing import Callable

from colorama import Fore, Style

from src.command.command import Command
from src.command.handler.add_contact import add_contact_command_handler
from src.command.handler.add_note import add_note_command_handler
from src.command.handler.exit import exit_command_handler
from src.command.parser import parse


class PersonalAssistant:
    """Main class for the personal assistant system."""

    def __init__(self):
        self.__address_book = {}
        self.__notes = {}
        self.__handlers = {}
        self.__register_command_handlers()

    def run(self) -> None:
        """
        Executes a loop that continuously waits for user input, parses commands,
        and takes action based on those commands.

        :return: None
        """
        while True:
            input_line = input("Enter a command: ")
            command = parse(input_line)
            if command is None:
                continue

            try:
                self.__handle(command)
            except ValueError as e:
                print(str(e))

    def __handle(self, command: Command) -> None:
        """
        Handles the processing of a command using a handler execution system. The method
        retrieves the appropriate handler for the provided command and executes it with
        the command's arguments.

        :param command: The command object containing the action to be performed and its
            associated arguments.
        :type command: Command
        """
        handler = self.__get_handler(command)
        handler(command.args)

    def __get_handler(self, command: Command) -> Callable[[list[str]], None]:
        """
        Retrieves the handler function associated with a given command.

        This method looks up the provided command name, ignoring case, in the internal
        registry of handlers. If a corresponding handler is found, it is returned;
        otherwise, an error is raised indicating an invalid command.

        :param command: The command for which the associated handler function is to
            be retrieved.
        :type command: Command
        :return: The handler function associated with the given command.
        :rtype: Callable[[list[str]], None]
        :raises ValueError: If the command name does not have an associated handler.
        """
        command_name = command.name.casefold()
        handler = self.__handlers.get(command_name, None)
        if handler is None:
            raise ValueError(f"{Fore.RED}[ERROR]{Style.RESET_ALL} "
                             f"Invalid command: '{command.name}'.")
        return handler

    def __register_command_handlers(self) -> None:
        """
        Sets up handlers for various commands in the application.

        This method registers command handlers for operations. Each command is
        associated with a lambda function that acts as an intermediary to the
        actual command handler function, passing the necessary arguments to it.

        :return: None
        """
        self.__handlers["add-contact"] = \
            lambda args: add_contact_command_handler(args, self.__address_book)

        self.__handlers["add-note"] = \
            lambda args: add_note_command_handler(args, self.__notes)

        self.__handlers["exit"] = lambda args: exit_command_handler()
