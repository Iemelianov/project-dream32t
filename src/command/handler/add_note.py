"""Handler for the add-note command."""


def add_note_command_handler(args: list[str], notes: dict[str, str] = None):
    """Handles the command."""
    if len(args) != 3:
        raise ValueError("add-note topic content [tags]")

    print(f"Adding note {args[0]} {notes}")
