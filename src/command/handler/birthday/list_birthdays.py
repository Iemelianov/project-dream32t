"""Handler for the birthdays command."""
from rich import print, box
from rich.table import Table

from src.command.command_argument import optional_arg
from src.command.command_description import CommandDefinition
from src.command.handler.command_handler import CommandHandler
from src.model.contact_book import ContactBook
from src.util.messages import NO_UPCOMING_BIRTHDAYS

class BirthdaysCommandHandler(CommandHandler):
    """Displays contacts with upcoming birthdays within the specified number of days."""

    def __init__(self, address_book: ContactBook):
        self.__address_book = address_book
        super().__init__(
            CommandDefinition(
                "list-birthdays",
                "Shows contacts with birthdays in the next N days (default: 7).",
                optional_arg("days", "Number of days to look ahead (default: 7)."),
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
        if not upcoming:
            print(NO_UPCOMING_BIRTHDAYS)
            return

  # Create table to display birthdays
        table = Table(
            title=f"[bold bright_magenta] Birthdays Party Coming Up (in {days} Days)[/bold bright_magenta]",
            title_style="bold bright_magenta",
            show_header=True,
            header_style="bold yellow",
            border_style="bright_magenta",
            box=box.HEAVY  # Bold borders
        )
        table.add_column("Contact Name", style="cyan", justify="left")
        table.add_column("Birthday Date", style="red bold", justify="center")
        for entry in upcoming:
            table.add_row(
            f"[cyan]{entry['name']}[/cyan]",
            f"[red]{entry['congratulation_date']}[/red]"
        )
        print(table)
