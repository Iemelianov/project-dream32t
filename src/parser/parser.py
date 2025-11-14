"""
Parses input lines into command objects.

This module processes input strings, extracting command names and their
associated arguments, and converts them into `Command` objects for further
use in the application flow.
"""
from src.command.command import Command
from src.parser.lexemes_builder import LexemesBuilder


def parse(input_line: str) -> Command | None:
    """
    Parses a user input string into a command and its arguments.

    This function processes a given input string, splits it into separate parts,
    and extracts the first element as the command name while the remaining elements are
    treated as arguments. If the input is empty, it returns None.

    :param input_line: The raw input string to be parsed.
    :return: An object containing the extracted command name and a list of its arguments.
    """
    builder = LexemesBuilder()
    for char in input_line:
        builder.append_char(char)
    lexemes = builder.build()
    if len(lexemes) == 0:
        return None

    cmd_name = lexemes[0]
    args: list[str] = lexemes[1:]
    return Command(name=cmd_name, args=args)
