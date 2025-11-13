"""
The entry point module of the application.

This module contains the main entry point of the program, designed to initialize
and execute the core functionality of the application. It ensures that the primary
logic is invoked only when the module is run as the main script.
"""

from src.personal_assistant import PersonalAssistant


def main() -> None:
    """
    The main entry point of the application that initializes and executes the program.
    """
    PersonalAssistant().run()


if __name__ == '__main__':
    main()
