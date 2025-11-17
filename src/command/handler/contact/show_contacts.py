"""Module for showing contacts in the table format."""

from rich.table import Table
from rich.box import ROUNDED
from rich import print as rprint
from src.util.messages import CONTACT_BOOK_EMPTY
from src.model.contact import Contact

def show_contacts(contacts: list[Contact]) -> None:
    """Shows all contacts in a clean Rich table."""
    if not contacts:
        rprint(CONTACT_BOOK_EMPTY)
        return

    table = Table(
        title="[bold blue]📇 Contact Book[/bold blue]",
        header_style="bold blue",
        border_style="blue",
        box=ROUNDED,
        expand=True
    )

    table.add_column("Name", style="cyan", no_wrap=False)
    table.add_column("Phone", style="white", overflow="fold")
    table.add_column("Email", style="white", overflow="fold")
    table.add_column("Address", style="white", overflow="fold")
    table.add_column("Birthday", style="white")

    for contact in contacts:
        cont_dict =  contact.to_dict()
        table.add_row(contact.name.value,
                    ", ".join(cont_dict["phones"]),
                    ", ".join(cont_dict["emails"]) or "[dim]-[/dim]",
                    ", ".join(cont_dict["addresses"]) or "[dim]-[/dim]",
                    cont_dict["birthday"] if contact.birthday else "[dim]-[/dim]")
    rprint(table)
