from collections import UserDict
from typing import Any, Dict
from src.model.contact import Contact 
from src.data_storage import DataStorage, CONTACTS_FILE, STORAGE_VERSION 

class AddressBook(UserDict[str, Contact]):
    """Collection of contacts, keyed by the contact's name in lowercase for case-insensitive lookup."""

    def __init__(self, contacts: Dict[str, Contact] | None = None):
        super().__init__()
        if contacts:
            for contact in contacts.values():
                # Key is the contact name in lowercase (for case-insensitive search)
                self.data[contact.name.value.lower()] = contact

    def to_dict(self) -> Dict[str, Any]:
        """Converts AddressBook into a serializable dictionary of contact data."""
        # Store contact data (represented as Name: Contact.to_dict()), 
        # ignoring the lowercase keys used internally by UserDict.
        return {contact.name.value: contact.to_dict() for contact in self.data.values()}

    @classmethod
    def from_data_payload(cls, data_payload: Dict[str, Any]) -> 'AddressBook':
        """Creates an AddressBook from the loaded dictionary data payload."""
        contacts = {}
        for contact_data in data_payload.values():
            try:
                contact = Contact.from_dict(contact_data)
                # Store with case-insensitive key
                contacts[contact.name.value.lower()] = contact
            except Exception as e:
                print(f"[WARNING]: Failed to load contact: {contact_data.get('name', 'N/A')}. Details: {e}")
        return cls(contacts)

    @staticmethod
    def load_from_storage() -> 'AddressBook':
        """Loads contacts from file, handling errors and file absence."""
        storage = DataStorage(CONTACTS_FILE)
        raw_data = storage.load_data()
        
        # 'data' key contains the contacts dictionary
        if raw_data.get("data"):
            return AddressBook.from_data_payload(raw_data["data"])
        
        print("Contacts not found. Created a new address book.")
        return AddressBook()

    def save_to_storage(self):
        """Saves the current AddressBook state to file."""
        data_payload = self.to_dict()
        data_to_save = {"version": STORAGE_VERSION, "data": data_payload}
        storage = DataStorage(CONTACTS_FILE)
        storage.save_data(data_to_save)