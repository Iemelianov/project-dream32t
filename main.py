import note


"""
The entry point module of the application.

This module contains the main entry point of the program, designed to initialize
and execute the core functionality of the application. It ensures that the primary
logic is invoked only when the module is run as the main script.
"""

def notes_test() -> None:
    """
    A test function to demonstrate the functionality of the note management system.
    """
    notes = note.Notes()
    notes.add_note("Shopping", "Buy milk and eggs", "groceries, Fruits   ")
    notes.add_note("Workout", "Go for a run fruits", "fitness")
    notes.add_note("Fruits", "I love pizza eating", "apple, banana")
    notes.add_note("No tag", "Note without tags")
    print("Initial Notes:")
    print(notes)

    find = notes.find_text_in_notes("fruits")
    print("\nSearch results for 'fruits' in notes content:")
    for item in find:
        print(item)

    find = notes.search_by_tag("fruits")
    print("\nSearch results for 'fruits' in notes tags:")
    for item in find:
        print(item)

    print("\nInitial Notes sorted by tags:")
    sorted_notes = notes.sort_by_tag()
    for item in sorted_notes:
        print(item)

    notes.edit_note("Shopping", "Buy milk, eggs, and bread")
    notes.add_tag("Workout", "fitness, evening")
    print("\nAfter Editing Shopping Note and Adding Tag to Workout Note:")
    print(notes)

    notes.delete_tags("Workout", "fitness,  evening ")
    notes.delete_note("Shopping")
    print("\nAfter Deleting Fitness, evening Tag from Workout Note and Deleting Shopping Note:")
    print(notes)


def main() -> None:
    """
    The main entry point of the application that initializes and executes the program.
    """
    # Uncomment the following line to run the note test function.
    #notes_test()


if __name__ == '__main__':
    main()
