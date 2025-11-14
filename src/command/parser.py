"""
Parses input lines into command objects.

This module processes input strings, extracting command names and their
associated arguments, and converts them into `Command` objects for further
use in the application flow.
"""
from enum import Enum

from src.command.command import Command


class Parser:
    class Quite(Enum):
        """Enum for the quoting style."""
        SINGLE = "'"
        DOUBLE = '"'

    @staticmethod
    def parse(input_line: str) -> Command | None:
        """
        Parses a user input string into a command and its arguments.

        This function processes a given input string, splits it into separate parts,
        and extracts the first element as the command name while the remaining elements are
        treated as arguments. If the input is empty, it returns None.

        :param input_line: The raw input string to be parsed.
        :return: An object containing the extracted command name and a list of its arguments.
        """
        parts = Parser.__parse(input_line)
        if len(parts) == 0:
            return None

        cmd_name = parts[0].strip()
        args: list[str] = parts[1:]
        return Command(name=cmd_name, args=args)

    @staticmethod
    def __parse(input_line: str) -> list[str]:
        quote = None
        parts: list[str] = []
        current_part: str = ""
        for char in input_line:

            if char == Parser.Quite.SINGLE.value:
                if quote is None:
                    quote = Parser.Quite.SINGLE
                elif quote == Parser.Quite.SINGLE:
                    quote = None
                else:
                    current_part += char
                continue

            if char == Parser.Quite.DOUBLE.value:
                if quote is None:
                    quote = Parser.Quite.DOUBLE
                elif quote == Parser.Quite.DOUBLE:
                    quote = None
                else:
                    current_part += char
                continue

            if char == " ":
                if quote is None:
                    if len(current_part) != 0:
                        parts.append(current_part)
                        current_part = ""
                else:
                    current_part += char
            else:
                current_part += char

        if quote is not None:
            raise ValueError("Invalid input - missing closing quotation marks.")

        if len(current_part) != 0:
            parts.append(current_part)

        return parts
