def confirm_delete(message: str) -> bool:
    input_line = input(f"Are you sure you want to delete {message}? (y/n) [N] ")
    cleared_line = input_line.strip()
    if len(cleared_line) == 0 or cleared_line.lower() != "y":
        print("Deletion cancelled.")
        return False
    return True
