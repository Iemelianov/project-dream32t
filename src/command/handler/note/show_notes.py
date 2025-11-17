"""Module for showing notes."""

from rich import print as rprint
from rich.table import Table, box

from src.model.note import NoteEntity
from src.util.messages import NO_NOTES_FOUND


def show_notes(notes: list[NoteEntity]) -> None:
    """Shows the notes in a clean Rich table."""
    if not notes:
        rprint(NO_NOTES_FOUND)
        return

    table = Table(
        title="[bold blue]📝 Notes[/bold blue]",
        header_style="bold blue",
        border_style="blue",
        box=box.ROUNDED,
        expand=True
    )

    table.add_column("Topic", style="cyan", no_wrap=False)
    table.add_column("Content", style="white", overflow="fold")

    for note in notes:
        topic_display = note.topic
        if note.tags:
            tags_str = ", ".join(note.tags)
            topic_display += f"\n[dim]🏷️ {tags_str}[/dim]"

        table.add_row(topic_display, note.content)

    rprint(table)
