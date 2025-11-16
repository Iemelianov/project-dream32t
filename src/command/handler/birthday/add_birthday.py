"""Handler for the set-birthday command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook
from src.model.name import Name

class AddBirthdayCommandHandler(CommandHandler):
    """Handles setting or updating a birthday for a contact."""

    def __init__(self, address_book: ContactBook):
        self.__address_book = address_book
        super().__init__(
            CommandDefinition(
                "set-birthday",
                "Sets or updates the birthday of a contact.",
                mandatory_arg("name", "Name of the contact."),
                mandatory_arg("birthday", "The birthday to set (format: DD.MM.YYYY)."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Sets or updates the birthday of the specified contact."""
        name = Name(args[0])
        birthday = " ".join(args[1:])

        contact = self.__address_book.find_contact_by_name(name)
        if contact is None:
            print(f"Contact '{name}' not found.")
            return

        try:
            # Check if birthday already exists (for user feedback only)
            had_birthday = contact.birthday is not None
            
            # Use unified set_birthday method (handles both add and update)
            contact.set_birthday(birthday)
            
            # Provide appropriate feedback
            if had_birthday:
                print(f"Birthday updated for contact '{name}'.")
            else:
                print(f"Birthday added to contact '{name}'.")
        except ValueError as e:
            print(f"Failed to set birthday: {e}")
