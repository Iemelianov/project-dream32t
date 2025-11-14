"""
Parses input lines into command objects.

This module processes input strings, extracting command names and their
associated arguments, and converts them into `Command` objects for further
use in the application flow.
"""
from enum import Enum

from src.command.command import Command


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


class LexemesBuilder:
    """
    A buffer class to parse and separate input strings into parts based on
    specific quotation styles and whitespace. It handles input processing,
    distinguishing between quoted parts, and correctly splitting and handling
    whitespace, single quotes, and double quotes.
    """

    class QuotationMark(Enum):
        """Enumeration for different types of quotation marks."""
        SINGLE = "'"
        DOUBLE = '"'

    def __init__(self):
        self.__quote = None
        self.__list_lexeme: list[str] = []
        self.__lexeme: str = ""

    def append_char(self, char) -> None:
        """Appends a character to the current part."""
        if char == LexemesBuilder.QuotationMark.SINGLE.value:
            self.__handle_single_quote()
        elif char == LexemesBuilder.QuotationMark.DOUBLE.value:
            self.__handle_double_quote()
        elif char == " ":
            self.__handle_whitespace()
        else:
            self.__append_char_to_lexeme(char)

    def build(self) -> list[str]:
        """Closes the current part and returns the list of parts."""
        if self.__lexeme_is_not_empty():
            self.__append_new_lexeme()

        if self.__has_open_quote():
            raise ValueError("Invalid input - missing closing quotation marks.")

        return self.__list_lexeme

    def __has_open_quote(self) -> bool:
        return self.__quote is not None

    def __handle_whitespace(self) -> None:
        if self.__has_open_quote():
            self.__append_whitespace_to_lexeme()
        else:
            if self.__lexeme_is_not_empty():
                self.__append_new_lexeme()
                self.__clear_buffer()

    def __append_new_lexeme(self) -> None:
        self.__list_lexeme.append(self.__lexeme)

    def __lexeme_is_not_empty(self) -> bool:
        return len(self.__lexeme) != 0

    def __handle_single_quote(self) -> None:
        if self.__quote is None:
            self.__quote = LexemesBuilder.QuotationMark.SINGLE
        elif self.__quote == LexemesBuilder.QuotationMark.SINGLE:
            self.__quote = None
        else:
            self.__append_single_quote_to_lexeme()

    def __handle_double_quote(self) -> None:
        if self.__quote is None:
            self.__quote = LexemesBuilder.QuotationMark.DOUBLE
        elif self.__quote == LexemesBuilder.QuotationMark.DOUBLE:
            self.__quote = None
        else:
            self.__append_double_quote_to_lexeme()

    def __append_whitespace_to_lexeme(self) -> None:
        self.__append_char_to_lexeme(" ")

    def __append_single_quote_to_lexeme(self) -> None:
        self.__append_char_to_lexeme("'")

    def __append_double_quote_to_lexeme(self) -> None:
        self.__append_char_to_lexeme('"')

    def __append_char_to_lexeme(self, char) -> None:
        self.__lexeme += char

    def __clear_buffer(self) -> None:
        self.__lexeme = ""
