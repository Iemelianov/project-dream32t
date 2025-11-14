"""
A module for colorizing strings using the colorama library.

This module provides utility functions to apply distinct colors to text
based on its intended meaning, such as errors, commands, arguments, and
descriptions.
"""


def error_color(text: str) -> str:
    """Colorize the given text as an error."""
    return f"[red]{text}[/red]"


def cmd_color(text: str) -> str:
    """Colorize the given text as a command."""
    return f"[bold green]{text}[/bold green]"


def arg_color(text: str) -> str:
    """Colorize the given text as an argument."""
    return f"[blue]{text}[/blue]"


def description_color(text: str) -> str:
    """Colorize the given text as a description."""
    return f"[yellow]{text}[/yellow]"
