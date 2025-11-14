"""
This module provides the implementation for a personal assistant system that
interprets user commands and performs a set of pre-defined actions. It includes
a command parsing mechanism and dynamically assigns handlers to manage specific
commands.

The `PersonalAssistant` class acts as the main interface for the system, allowing
users to interact with a series of commands such as adding contacts, adding notes,
or exiting the application.
"""
from src.command.command import Command
from src.command.handler.address.add_address import AddAddressCommandHandler
from src.command.handler.address.change_address import ChangeAddressCommandHandler
from src.command.handler.address.del_address import DelAddressCommandHandler
from src.command.handler.birthday.add_birthday import AddBirthdayCommandHandler
from src.command.handler.birthday.del_birthday import DelBirthdayCommandHandler
from src.command.handler.command_handler import CommandHandler
from src.command.handler.command_handlers import CommandHandlers
from src.command.handler.contact.add_contact import AddContactCommandHandler
from src.command.handler.contact.del_contact import DelContactCommandHandler
from src.command.handler.email.add_email import AddEmailCommandHandler
from src.command.handler.email.change_email import ChangeEmailCommandHandler
from src.command.handler.email.del_email import DelEmailCommandHandler
from src.command.handler.exit import ExitCommandHandler
from src.command.handler.help import HelpCommandHandler
from src.command.handler.note.add_note import AddNoteCommandHandler
from src.command.handler.note.change_note import ChangeNoteCommandHandler
from src.command.handler.note.del_note import DelNoteCommandHandler
from src.command.handler.note.find_note_by_tags import FindNoteByTagCommandHandler
from src.command.handler.note.find_note_by_text import FindNoteByTextCommandHandler
from src.command.handler.phone.add_phone import AddPhoneCommandHandler
from src.command.handler.phone.change_phone import ChangePhoneCommandHandler
from src.command.handler.phone.del_phone import DelPhoneCommandHandler
from src.model.note import Notes
from src.parser.parser import parse
from src.util.colorize import error_color


class PersonalAssistant:
    """Main class for the personal assistant system."""

    def __init__(self):
        self.__address_book = {}
        self.__notes = Notes()
        self.__handlers = CommandHandlers()
        self.__register_command_handlers()

    def run(self) -> None:
        """
        Executes a loop that continuously waits for user input, parses commands,
        and takes action based on those commands.

        :return: None
        """
        while True:
            try:
                input_line = input("Enter a command: ")
                command = parse(input_line)
                if command is None:
                    continue
                self.__handle(command)
            except ValueError as e:
                print(f"{error_color('[ERROR]')}: " + str(e))

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
        handler.handle(command.args)

    def __get_handler(self, command: Command) -> CommandHandler:
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
            raise ValueError(f"Invalid command: '{command.name}'.")
        return handler

    def __register_command_handlers(self) -> None:
        """
        Sets up handlers for various commands in the application.

        This method registers command handlers for operations. Each command is
        associated with a lambda function that acts as an intermediary to the
        actual command handler function, passing the necessary arguments to it.

        :return: None
        """
        # Registering handlers for contact management commands
        self.__handlers.register(AddContactCommandHandler(self.__address_book))
        self.__handlers.register(DelContactCommandHandler(self.__address_book))

        # Registering handlers for phone number management commands
        self.__handlers.register(AddPhoneCommandHandler(self.__address_book))
        self.__handlers.register(ChangePhoneCommandHandler(self.__address_book))
        self.__handlers.register(DelPhoneCommandHandler(self.__address_book))

        # Registering handlers for email address management commands
        self.__handlers.register(AddEmailCommandHandler(self.__address_book))
        self.__handlers.register(ChangeEmailCommandHandler(self.__address_book))
        self.__handlers.register(DelEmailCommandHandler(self.__address_book))

        # Registering handlers for address management commands
        self.__handlers.register(AddAddressCommandHandler(self.__address_book))
        self.__handlers.register(ChangeAddressCommandHandler(self.__address_book))
        self.__handlers.register(DelAddressCommandHandler(self.__address_book))

        # Registering handlers for birthday management commands
        self.__handlers.register(AddBirthdayCommandHandler(self.__address_book))
        self.__handlers.register(DelBirthdayCommandHandler(self.__address_book))

        # Registering handlers for notes management commands
        self.__handlers.register(AddNoteCommandHandler(self.__notes))
        self.__handlers.register(ChangeNoteCommandHandler(self.__notes))
        self.__handlers.register(DelNoteCommandHandler(self.__notes))
        self.__handlers.register(FindNoteByTextCommandHandler(self.__notes))
        self.__handlers.register(FindNoteByTagCommandHandler(self.__notes))

        self.__handlers.register(ExitCommandHandler())
        self.__handlers.register(HelpCommandHandler(self.__handlers))
