# src/data_storage.py
import json
import os
import shutil
import tempfile
from typing import Any, Dict

# Storage configuration according to requirements
CONTACTS_FILE = "contacts.json"
NOTES_FILE = "notes.json"
STORAGE_VERSION = 1

class DataStorage:
    """
    Manages atomic saving, backup, and restoration of JSON data.
    Provides portability and UTF-8.
    """
    def __init__(self, filename: str):
        self.filename = filename
        self.backup_filename = filename + ".bak"
        # Use the storage version constant
        self.initial_data: Dict[str, Any] = {"version": STORAGE_VERSION, "data": []} 

    def _load_file(self, file_path: str) -> Dict[str, Any] | None:
        """Reads data from a file with UTF-8 encoding set."""
        try:
            # Using UTF-8 encoding as required
            with open(file_path, 'r', encoding='utf-8') as f: 
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return None
        except Exception as e:
            # Simple print as we may not have rich available here
            print(f"Error reading file {file_path}: {e}")
            return None

    def load_data(self) -> Dict[str, Any]:
        """
        Loading data. Attempting to recover from .bak if the main file is corrupted.
        """
        data = self._load_file(self.filename)
        
        if data is None:
            # Attempting to download a backup if the primary file is corrupted
            backup_data = self._load_file(self.backup_filename)
            
            if backup_data is not None:
                print(f"⚠️ Main file '{self.filename}' is damaged. Restore from backup.")
                
                # Check backup version
                if backup_data.get("version") != STORAGE_VERSION:
                    print(f"❌ Backup file version mismatch. Expected {STORAGE_VERSION}, found {backup_data.get('version')}. Returning initial data.")
                    return self.initial_data
                
                # Attempt to save recovered data to the main file
                try:
                    # Recursive call to save_data to update the main file and remove .bak
                    self.save_data(backup_data) 
                    return backup_data
                except Exception as e:
                    print(f"❌ Unable to restore the main file from the backup: {e}")
                    return self.initial_data
            print(f"ℹ️ File '{self.filename}' not found or cannot be loaded. New data created.")
            return self.initial_data

        # Check main file version
        if data.get("version") != STORAGE_VERSION:
            print(f"❌ Main file version mismatch. Expected {STORAGE_VERSION}, found {data.get('version')}. Using initial data.")
            return self.initial_data

        return data

    def save_data(self, data: Dict[str, Any]) -> None:
        """
        Atomically saves data:
        1. Creates a backup copy of the existing main file.
        2. Writes new data to a temporary file.
        3. Renames the temporary file, replacing the main one.
        """
        
        # Check data version before saving
        if not isinstance(data, dict) or "version" not in data or data.get("version") != STORAGE_VERSION:
            if data.get("version") != STORAGE_VERSION:
                 print(f"❌ Error: Invalid data version for saving. Expected {STORAGE_VERSION}. Saving canceled.")
            else:
                print("❌ Error: Invalid data format for saving. Saving canceled.")
            return

        # 1. Backup
        if os.path.exists(self.filename):
            try:
                # Using shutil.copy2 to preserve metadata
                shutil.copy2(self.filename, self.backup_filename)
            except Exception as e:
                print(f"❌ Error creating backup '{self.backup_filename}': {e}")
                pass 

        # 2. Write to temporary file
        # Use named_temporary_file, to ensure uniqueness
        temp_file_descriptor, temp_path = tempfile.mkstemp(suffix='.tmp', dir='.')

        try:
            with os.fdopen(temp_file_descriptor, 'w', encoding='utf-8') as tmp_file:
                # ensure_ascii=False for correct UTF-8 saving
                json.dump(data, tmp_file, indent=4, ensure_ascii=False) 
            
            # 3. Replacing the main file
            # os.replace performs an atomic rename (swap) operation
            os.replace(temp_path, self.filename)
            print(f"✅ Data successfully saved to '{self.filename}'.")

            # 4. Remove backup file after successful save
            if os.path.exists(self.backup_filename):
                os.remove(self.backup_filename)

        except Exception as e:
            print(f"❌ Error during data write: {e}. Existing data preserved.")
            # Delete temporary file if an error occurs
            if os.path.exists(temp_path):
                os.remove(temp_path)