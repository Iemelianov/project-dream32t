"""Handler for the add-contact command."""


def add_contact_command_handler(args: list[str], address_book: dict[str, str] = None):
    """Handles the command."""
    if len(args) != 1:
        raise ValueError("add-contact [name]")

    print(f"Adding contact {args[0]} {address_book}")
