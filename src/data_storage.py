import json
import os
import shutil
import tempfile
from typing import Any, Dict
from src.util.messages import DATA_SAVED
from rich import print as rprint

# --- Data storage settings ---
# Files are persisted in the user's home directory under APP_FOLDER.
APP_FOLDER = ".cli_assistant"
CONTACTS_FILE = "contacts.json"
NOTES_FILE = "notes.json"
STORAGE_VERSION = 1
# -----------------------------------


class DataStorage:
    """
    Manages atomic saving, backup, and restoration of JSON data.
    Persists files inside the user's home directory (APP_FOLDER) using UTF-8.
    """

    def __init__(self, filename: str):
        home_dir = os.path.expanduser("~")
        self.storage_dir = os.path.join(home_dir, APP_FOLDER)

        try:
            os.makedirs(self.storage_dir, exist_ok=True)
        except Exception as e:
            # Fallback to current directory if we cannot create the folder.
            print(
                f"FATAL ERROR: Could not create storage directory {self.storage_dir}: {e}. "
                "Falling back to current directory."
            )
            self.storage_dir = "."

        self.filename = os.path.join(self.storage_dir, filename)
        self.backup_filename = self.filename + ".bak"

        # Use the storage version constant
        self.initial_data: Dict[str, Any] = {"version": STORAGE_VERSION, "data": []}

    def _load_file(self, file_path: str) -> Dict[str, Any] | None:
        """Reads data from a file with UTF-8 encoding set."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return None
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            return None

    def load_data(self) -> Dict[str, Any]:
        """
        Load data, attempting recovery from .bak if the main file is missing or corrupted.
        """
        data = self._load_file(self.filename)

        if data is None:
            backup_data = self._load_file(self.backup_filename)

            if backup_data is not None:
                print(f"⚠️ Main file '{self.filename}' is damaged. Restore from backup.")

                if backup_data.get("version") != STORAGE_VERSION:
                    print(
                        f"❌ Backup file version mismatch. Expected {STORAGE_VERSION}, "
                        f"found {backup_data.get('version')}. Returning initial data."
                    )
                    return self.initial_data

                try:
                    self.save_data(backup_data)
                    return backup_data
                except Exception as e:
                    print(f"❌ Unable to restore the main file from the backup: {e}")
                    return self.initial_data

            print(f"ℹ️ File '{self.filename}' not found or cannot be loaded. New data created.")
            return self.initial_data

        if data.get("version") != STORAGE_VERSION:
            print(
                f"❌ Main file version mismatch. Expected {STORAGE_VERSION}, "
                f"found {data.get('version')}. Using initial data."
            )
            return self.initial_data

        return data

    def save_data(self, data: Dict[str, Any], silent: bool = False) -> None:
        """
        Atomically save data:
        1. Create a backup copy of the existing main file.
        2. Write new data to a temporary file.
        3. Replace the main file with the temp file.
        """

        if not isinstance(data, dict) or "version" not in data or data.get("version") != STORAGE_VERSION:
            if isinstance(data, dict) and data.get("version") != STORAGE_VERSION:
                print(
                    f"❌ Error: Invalid data version for saving. Expected {STORAGE_VERSION}. Saving canceled."
                )
            else:
                print("❌ Error: Invalid data format for saving. Saving canceled.")
            return

        if os.path.exists(self.filename):
            try:
                shutil.copy2(self.filename, self.backup_filename)
            except Exception as e:
                print(f"❌ Error creating backup '{self.backup_filename}': {e}")

        temp_fd, temp_path = tempfile.mkstemp(suffix=".tmp", dir=self.storage_dir)

        try:
            with os.fdopen(temp_fd, "w", encoding="utf-8") as tmp_file:
                json.dump(data, tmp_file, indent=4, ensure_ascii=False)

            os.replace(temp_path, self.filename)
            if not silent:
                rprint(DATA_SAVED.format(filename=self.filename))

            if os.path.exists(self.backup_filename):
                os.remove(self.backup_filename)

        except Exception as e:
            print(f"❌ Error during data write: {e}. Existing data preserved.")
            if os.path.exists(temp_path):
                os.remove(temp_path)
