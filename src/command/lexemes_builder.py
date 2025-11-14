"""Module for the LexemesBuilder class."""
from enum import Enum


class LexemesBuilder:
    """
    Handles the processing and splitting of input text into lexemes based on
    whitespace and quotation marks. Supports both single and double quotation
    marks for grouping portions of input as single lexemes. Ensures no
    unclosed quotations persist before outputting the resulting lexeme list.
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
