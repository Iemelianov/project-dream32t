"""Collection object used to store and search contact records."""

from __future__ import annotations

from collections import UserDict
from typing import Optional

from model.contact import Contact


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

    def find_contact(self, query: str) -> Optional[Contact]:
        """
        Find a contact either by name (case-insensitive) or one of its phones.

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

    def delete_contact(self, name: str) -> tuple[bool, Optional[Contact]]:
        """
        Delete an existing contact by name.

        :returns: (True, removed Contact) if deletion succeeded; otherwise
            (False, None) when no such contact was stored.
        """

        normalized = self._normalize_name(name)
        contact = self.data.pop(normalized, None)
        return (contact is not None, contact)

    # ------------------------------------------------------------------ #
    # Internal helpers
    # ------------------------------------------------------------------ #
    def _find_by_phone(self, phone: str) -> Optional[Contact]:
        for contact in self.data.values():
            for number in getattr(contact, "phones", []):
                if number.value == phone:
                    return contact
        return None

    def _normalize_name(self, name: str) -> str:
        stripped = name.strip()
        if not stripped:
            raise ValueError("Name cannot be empty.")
        return stripped.casefold()
