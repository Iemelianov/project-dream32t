"""Handler for the add-birthday command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook


class AddBirthdayCommandHandler(CommandHandler):
    """Handles the functionality to add a birthday to a contact."""

    def __init__(self, address_book: ContactBook):
        self.__address_book = address_book
        super().__init__(
            CommandDefinition(
                "set-birthday",
                "Adds an contact birthday to an address book.",
                mandatory_arg("name", "Name of a contact."),
                mandatory_arg("birthday", "The birthday to add (format: YYYY-MM-DD)."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Sets or changes the birthday of the specified contact."""
        name = args[0]
        birthday = " ".join(args[1:])

        contact = self.__address_book.find_contact(name)
        if contact is None:
            print(f"Contact '{name}' not found.")
            return

        try:
            if contact.birthday is None:
                contact.set_birthday(birthday)
                print(f"Birthday added to contact '{name}'.")
            else:
                contact.update_birthday(birthday)
                print(f"Birthday updated for contact '{name}'.")
        except ValueError as e:
            print(f"Failed to set birthday: {e}")
