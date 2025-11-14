"""
A module for colorizing strings using the colorama library.

This module provides utility functions to apply distinct colors to text
based on its intended meaning, such as errors, commands, arguments, and
descriptions.
"""
from colorama import Fore, Style


def error_color(text: str) -> str:
    """Colorize the given text as an error."""
    return f"{Fore.RED}{text}{Style.RESET_ALL}"


def cmd_color(text: str) -> str:
    """Colorize the given text as a command."""
    return f"{Fore.GREEN}{text}{Style.RESET_ALL}"


def arg_color(text: str) -> str:
    """Colorize the given text as an argument."""
    return f"{Fore.BLUE}{text}{Style.RESET_ALL}"


def description_color(text: str) -> str:
    """Colorize the given text as a description."""
    return f"{Fore.YELLOW}{text}{Style.RESET_ALL}"
