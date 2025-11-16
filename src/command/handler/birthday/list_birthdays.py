"""Handler for the birthdays command."""
from src.command.command_argument import mandatory_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook


class BirthdaysCommandHandler(CommandHandler):
    """Displays contacts with upcoming birthdays within the specified number of days."""

    def __init__(self, address_book: ContactBook):
        self.__address_book = address_book
        super().__init__(
            CommandDefinition(
                "list-birthdays",
                "Shows contacts with birthdays in the next N days (default: 7).",
                mandatory_arg("days", "Number of days to look ahead (default: 7)."),
            )
        )

    def _handle(self, args: list[str]) -> None:
        """Display upcoming birthdays."""
        # Parse days argument (default to 7)
        days = 7
        if args:
            try:
                days = int(args[0])
                if days < 0:
                    print("Number of days must be non-negative.")
                    return
            except ValueError:
                print("Invalid number of days. Please provide a valid integer.")
                return

        # Get upcoming birthdays
        try:
            upcoming = self.__address_book.get_upcoming_birthdays(days)
        except (ValueError, AttributeError) as e:
            print(f"Error retrieving birthdays: {e}")
            return

        # Display results
        if not upcoming:
            print(f"No birthdays in the next {days} days.")
        else:
            print(f"Upcoming birthdays in the next {days} days:")
            print("-" * 50)
            for entry in upcoming:
                print(f"• {entry['name']}: {entry['congratulation_date']}")
