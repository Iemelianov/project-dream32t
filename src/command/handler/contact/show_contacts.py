"""Module for showing contacts in the table format."""

import rich
from rich.table import Table, box

from src.model.contact import Contact


def show_contacts(contacts: list[Contact]) -> None:
    """Shows all contacts from the address book."""
    if not contacts:
        print("Contact book is empty")
        return
    table = Table(box=box.SIMPLE_HEAD)
    table.add_column("Name", justify="left", style="red", no_wrap=False)
    table.add_column("Phone", justify="left", style="green")
    table.add_column("Email", justify="left", style="green")
    table.add_column("Address", justify="left", style="green")
    table.add_column("Birthday", justify="left", style="green")
    for contact in contacts:
        phones = contact.show_phones()
        emails = contact.show_emails()
        addresses = contact.show_addresses()
        birthday = ""
        if contact.birthday:
            birthday = contact.birthday.value.strftime('%d.%m.%Y')
        table.add_row(contact.name.value, phones, emails, addresses, birthday)
    rich.print(table)
