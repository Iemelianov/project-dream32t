"""Collection object used to store and search contact records."""

from __future__ import annotations

from collections import UserDict
from datetime import datetime, timedelta
from typing import Optional

from src.data_storage import DataStorage, CONTACTS_FILE, STORAGE_VERSION
from src.model.contact import Contact
from src.model.name import Name
from src.model.birthday import Birthday



class ContactBook(UserDict[str, Contact]):
    """
    Store ``Contact`` records indexed by the contact name.

    The book provides helpers to create, fetch, and delete contacts. Names are
    matched irrespective of case, while phone lookups expect an exact match.
    """

    def create_contact(self, name: str, phone: str) -> tuple[bool, Optional[Contact]]:
        """
        Create a new contact with the provided name and phone number.

        :returns: (True, Contact) if the contact was created; otherwise
            (False, existing Contact) when the name is already taken.
        """

        normalized = self._normalize_name(name)
        if normalized in self.data:
            return False, self.data[normalized]

        contact = Contact(name, phone)
        self.data[normalized] = contact
        return True, contact

    def find_contact_by_name(self, name: Name) -> Contact | None:
        """
        Find a contact by its name.

        :param name: The name of the contact to search for.
        :type name: Name
        :return: The contact if found, otherwise None.
        :rtype: Contact | None
        """
        normalized = self._normalize_name(name.value)
        return self.data.get(normalized, None)

    def find_contact(self, query: str) -> Optional[Contact]:
        """
        Find a contact by name (case-insensitive) or by one of its phones.

        :returns: Contact if found, None otherwise.
        """

        cleaned = query.strip()
        if not cleaned:
            return None

        normalized = cleaned.casefold()
        contact = self.data.get(normalized)
        if contact:
            return contact

        return self._find_by_phone(cleaned)

    def find_contact_by_param(self, param: str, val: str) -> Contact | None:
        """
        Find a contact by parameter.

        :param: Search parameter, must be one of the following:
                name, phones, emails, addresses, birthday
        :type param: string
        :val: Value to search
        :type val: string
        :return: The contact if found, otherwise None.
        :rtype: Contact | None | []
        """
        param = param.casefold().strip()

        if param == "name":
            return [self.find_contact_by_name(Name(val.casefold().strip()))]
        if param in ("phones", "emails"):
            return self._find_by_attr(param, val.casefold().strip())
        if param == "addresses":
            return self._find_by_attr(param, val)
        if param == "birthday":
            return self._find_by_birthday(val.casefold().strip())
        return  None

    def delete_contact(self, name: str) -> tuple[bool, Optional[Contact]]:
        """
        Delete an existing contact by name.

        :returns: (True, removed Contact) if deletion succeeded; otherwise
            (False, None) when no such contact was stored.
        """

        normalized = self._normalize_name(name)
        contact = self.data.pop(normalized, None)
        return (contact is not None, contact)

    def get_upcoming_birthdays(self, days: int = 7) -> list[dict[str, str]]:
        """ Get a list of contacts with birthdays within the next 'days' days. """
        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday is None:
                continue

            birthday = record.birthday.value

            # Adjust to this year (handle Feb 29)
            try:
                birthday_this_year = birthday.replace(year=today.year)
            except ValueError:
                # Handle leap year (Feb 29)
                birthday_this_year = birthday.replace(year=today.year, day=28)

            # If birthday already passed this year, use next year
            if birthday_this_year < today:
                try:
                    birthday_this_year = birthday.replace(year=today.year + 1)
                except ValueError:
                    birthday_this_year = birthday.replace(year=today.year + 1, day=28)

            days_until = (birthday_this_year - today).days

            # Only include if within the specified range
            if 0 <= days_until <= days:
                congratulation_date = birthday_this_year

                # Adjust for weekends
                weekday = congratulation_date.weekday()
                if weekday == 5:  # Saturday
                    congratulation_date += timedelta(days=2)
                elif weekday == 6:  # Sunday
                    congratulation_date += timedelta(days=1)

                upcoming_birthdays.append({
                    "name": record.name.value,
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
                })

        return upcoming_birthdays

    # ------------------------------------------------------------------ #
    # Internal helpers
    # ------------------------------------------------------------------ #
    def _find_by_phone(self, phone: str) -> Optional[Contact]:
        for contact in self.data.values():
            for number in getattr(contact, "phones", []):
                if number.value == phone:
                    return contact
        return None

    def _find_by_attr(self, attr: str, val: str) -> Optional[Contact]:
        ret = []
        for contact in self.data.values():
            for items in getattr(contact, attr, []):
                if items.value == val:
                    ret.append(contact)
        return ret

    def _find_by_birthday(self, birthday: str) -> Optional[Contact]:
        ret = []
        birthday_obj = Birthday(birthday)
        for contact in self.data.values():
            if contact.birthday and contact.birthday.value == birthday_obj.value:
                ret.append(contact)
        return ret

    def _normalize_name(self, name: str) -> str:
        stripped = name.strip()
        if not stripped:
            raise ValueError("Name cannot be empty.")
        return stripped.casefold()

    # ------------------------------------------------------------------ #
    # Save, load, storage
    # ------------------------------------------------------------------ #
    def __init__(self, contacts: dict[str, Contact] | None = None):
        super().__init__()
        if contacts:
            for contact in contacts.values():
                # Key is the contact name in lowercase (for case-insensitive search)
                self.data[contact.name.value.lower()] = contact

    def to_dict(self) -> dict[str, any]:
        """Converts ContactBook into a serializable dictionary of contact data."""
        # Store contact data (represented as Name: Contact.to_dict()),
        # ignoring the lowercase keys used internally by UserDict.
        return {contact.name.value: contact.to_dict() for contact in self.data.values()}

    @classmethod
    def from_data_payload(cls, data_payload: dict[str, any]) -> 'ContactBook':
        """Creates an ContactBook from the loaded dictionary data payload."""
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
    def load_from_storage() -> 'ContactBook':
        """Loads contacts from file, handling errors and file absence."""
        storage = DataStorage(CONTACTS_FILE)
        raw_data = storage.load_data()

        # 'data' key contains the contacts dictionary
        if raw_data.get("data"):
            return ContactBook.from_data_payload(raw_data["data"])

        print("Contacts not found. Created a new contact book.")
        return ContactBook()

    def save_to_storage(self, silent: bool = False):
        """Saves the current ContactBook state to file."""
        data_payload = self.to_dict()
        data_to_save = {"version": STORAGE_VERSION, "data": data_payload}
        storage = DataStorage(CONTACTS_FILE)
        storage.save_data(data_to_save, silent=silent)
