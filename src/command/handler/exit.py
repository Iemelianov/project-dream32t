"""Exit command handler."""
import sys

from colorama import Fore, Style


def exit_command_handler():
    """Handles the command."""
    print(f"{Fore.BLUE}Good bye!{Style.RESET_ALL}")
    sys.exit(0)
