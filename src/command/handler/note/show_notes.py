"""Module for showing notes."""

import rich
from rich.table import Table, box

from src.model.note import NoteEntity


def show_notes(notes: list[NoteEntity]) -> None:
    """Shows the notes."""
    table = Table(box=box.SIMPLE_HEAD)
    table.add_column("Topic", justify="left", style="blue", no_wrap=True)
    table.add_column("Content", justify="left", style="yellow")
    table.add_column("Tags", justify="left", style="red")
    for note in notes:
        table.add_row(note.topic, note.content, ", ".join(note.tags))
    rich.print(table)
