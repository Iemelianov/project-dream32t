"""Module for showing contacts in the table format."""

from rich.table import Table
from rich.box import ROUNDED
from rich import print 
from src.util.messages import CONTACT_BOOK_EMPTY
from src.model.contact import Contact

def show_contacts(contacts: list[Contact]) -> None:
    """Shows all contacts in a clean Rich table."""
    if not contacts:
        print(CONTACT_BOOK_EMPTY)
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
        phones = contact.show_phones() or "[dim]-[/dim]"
        emails = contact.show_emails() or "[dim]-[/dim]"
        addresses = contact.show_addresses() or "[dim]-[/dim]"
        birthday = contact.birthday.value.strftime('%d.%m.%Y') if contact.birthday else "[dim]-[/dim]"
        
        table.add_row(contact.name.value, phones, emails, addresses, birthday)
    
    print(table)