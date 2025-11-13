"""
Unit tests for validating the functionality of the `parse` function
in the command parsing module.
"""
from src.command.parser import parse


def test_parse_valid_command_with_args() -> None:
    """
    Parses and validates a command string with arguments, then performs assertions
    to ensure correct parsing behavior. This function tests the ability of the
    `parse` function to correctly parse a command name and its associated arguments.
    """
    input_line = "change-phone 1234567890 1111122222"

    command = parse(input_line)

    assert command.name == "change-phone"
    assert command.args == ["1234567890", "1111122222"]


def test_parse_valid_command_without_args() -> None:
    """
    Parses a command without arguments and verifies its parsed output.

    This test function ensures that a command string without any arguments is
    correctly parsed into its respective components: the command name and an
    empty argument list.
    """
    input_line = "exit"

    command = parse(input_line)

    assert command.name == "exit"
    assert command.args == []


def test_parse_empty_input() -> None:
    """
    Parses an empty input string and validates that the returned command is None.

    This function ensures that when the input string is empty, the `parse`
    function correctly processes it by returning `None`.
    """
    input_line = ""

    command = parse(input_line)

    assert command is None


def test_parse_command_with_extra_whitespace() -> None:
    """
    Tests the functionality of the `parse` function with input containing
    extra whitespace.

    This test ensures that the `parse` function correctly strips
    whitespace and accurately parses the command name and arguments from
    the given input.
    """
    input_line = "   change-phone   1234567890   1111122222   "

    command = parse(input_line)

    assert command.name == "change-phone"
    assert command.args == ["1234567890", "1111122222"]


def test_parse_command_with_case_insensitivity() -> None:
    """
    Tests the parsing of a command string to ensure case insensitivity. It validates
    that the `parse` function correctly interprets the command name and arguments
    regardless of the casing in the input.
    """
    input_line = "CHANGE-EMAIL A2B.CO C@B.CO"

    command = parse(input_line)

    assert command.name == "CHANGE-EMAIL"
    assert command.args == ["A2B.CO", "C@B.CO"]
