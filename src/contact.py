"""Contact record implementation."""

from __future__ import annotations

from typing import Type, TypeVar

from address import Address
from birthday import Birthday
from email import Email
from name import Name
from phone import Phone

FieldType = TypeVar("FieldType", Name, Phone, Email, Address, Birthday)


class Contact:
    """
    Represent a single contact record with validated fields.

    Creation mirrors the CLI workflow: a new contact requires only Name and the
    first Phone number. All other fields are added, updated, or removed via the
    dedicated helper methods so that commands can focus on a single value at a time.
    """

    def __init__(self, name: Name | str, phone: Phone | str) -> None:
        self.name: Name = self._coerce(name, Name)
        self.phones: list[Phone] = [self._coerce(phone, Phone)]
        self.emails: list[Email] = []
        self.addresses: list[Address] = []
        self.birthday: Birthday | None = None

    @staticmethod
    def _coerce(value: FieldType | str, field_cls: Type[FieldType]) -> FieldType:
        """Ensure the provided value is an instance of ``field_cls``."""

        if isinstance(value, field_cls):
            return value
        return field_cls(value)

    # ----- Phone handling -------------------------------------------------
    def add_phone(self, phone: Phone | str) -> Phone:
        phone_obj = self._coerce(phone, Phone)
        if any(existing.value == phone_obj.value for existing in self.phones):
            raise ValueError("Phone number already exists for this contact.")
        self.phones.append(phone_obj)
        return phone_obj

    def remove_phone(self, phone: Phone | str) -> Phone:
        phone_value = self._coerce(phone, Phone).value
        for idx, existing in enumerate(self.phones):
            if existing.value == phone_value:
                if len(self.phones) == 1:
                    raise ValueError("Contact must keep at least one phone number.")
                return self.phones.pop(idx)
        raise ValueError("Phone number not found for this contact.")

    def update_phone(self, old_phone: Phone | str, new_phone: Phone | str) -> Phone:
        old_value = self._coerce(old_phone, Phone).value
        new_obj = self._coerce(new_phone, Phone)

        if any(p.value == new_obj.value for p in self.phones if p.value != old_value):
            raise ValueError("The new phone number already exists for this contact.")

        for idx, existing in enumerate(self.phones):
            if existing.value == old_value:
                self.phones[idx] = new_obj
                return new_obj
        raise ValueError("Phone number not found for this contact.")

    # ----- Email handling -------------------------------------------------
    def add_email(self, email: Email | str) -> Email:
        email_obj = self._coerce(email, Email)
        if any(e.value.lower() == email_obj.value.lower() for e in self.emails):
            raise ValueError("Email already exists for this contact.")
        self.emails.append(email_obj)
        return email_obj

    def remove_email(self, email: Email | str) -> Email:
        email_value = self._coerce(email, Email).value.lower()
        for idx, existing in enumerate(self.emails):
            if existing.value.lower() == email_value:
                return self.emails.pop(idx)
        raise ValueError("Email not found for this contact.")

    def update_email(self, old_email: Email | str, new_email: Email | str) -> Email:
        old_value = self._coerce(old_email, Email).value.lower()
        new_obj = self._coerce(new_email, Email)
        if any(e.value.lower() == new_obj.value.lower() for e in self.emails if e.value.lower() != old_value):
            raise ValueError("The new email already exists for this contact.")
        for idx, existing in enumerate(self.emails):
            if existing.value.lower() == old_value:
                self.emails[idx] = new_obj
                return new_obj
        raise ValueError("Email not found for this contact.")

    # ----- Address handling -----------------------------------------------
    def add_address(self, address: Address | str) -> Address:
        address_obj = self._coerce(address, Address)
        if any(a.value == address_obj.value for a in self.addresses):
            raise ValueError("Address already exists for this contact.")
        self.addresses.append(address_obj)
        return address_obj

    def remove_address(self, address: Address | str) -> Address:
        address_value = self._coerce(address, Address).value
        for idx, existing in enumerate(self.addresses):
            if existing.value == address_value:
                return self.addresses.pop(idx)
        raise ValueError("Address not found for this contact.")

    def update_address(self, old_address: Address | str, new_address: Address | str) -> Address:
        old_value = self._coerce(old_address, Address).value
        new_obj = self._coerce(new_address, Address)
        if any(a.value == new_obj.value for a in self.addresses if a.value != old_value):
            raise ValueError("The new address already exists for this contact.")
        for idx, existing in enumerate(self.addresses):
            if existing.value == old_value:
                self.addresses[idx] = new_obj
                return new_obj
        raise ValueError("Address not found for this contact.")

    # ----- Birthday handling ----------------------------------------------
    def set_birthday(self, birthday: Birthday | str) -> Birthday:
        if self.birthday is not None:
            raise ValueError("Birthday is already set for this contact.")
        self.birthday = self._coerce(birthday, Birthday)
        return self.birthday

    def update_birthday(self, old_birthday: Birthday | str, new_birthday: Birthday | str) -> Birthday:
        if self.birthday is None:
            raise ValueError("Birthday is not set for this contact.")
        old_value = self._coerce(old_birthday, Birthday).value
        if self.birthday.value != old_value:
            raise ValueError("Provided birthday does not match the existing value.")
        self.birthday = self._coerce(new_birthday, Birthday)
        return self.birthday

    def clear_birthday(self, birthday: Birthday | str | None = None) -> None:
        if self.birthday is None:
            raise ValueError("Birthday is not set for this contact.")
        if birthday is not None:
            existing_value = self._coerce(birthday, Birthday).value
            if self.birthday.value != existing_value:
                raise ValueError("Provided birthday does not match the existing value.")
        self.birthday = None

    # ----- Utility helpers ------------------------------------------------
    def to_dict(self) -> dict[str, object]:
        """Return a serialisable representation of the contact."""

        return {
            "name": self.name.value,
            "phones": [phone.value for phone in self.phones],
            "emails": [email.value for email in self.emails],
            "addresses": [address.value for address in self.addresses],
            "birthday": self.birthday.value.strftime("%d.%m.%Y") if self.birthday else None,
        }

    def __repr__(self) -> str:  # pragma: no cover - helper for debugging
        return (
            f"Contact(name={self.name!r}, phones={self.phones!r}, emails={self.emails!r}, "
            f"addresses={self.addresses!r}, birthday={self.birthday!r})"
        )
