"""
Module for Note entity and Notes container.
Note has topic (string) and content (string), tag is optional parameter (list of strings)
"""
from __future__ import annotations
from collections import UserList
from typing import Optional, List, Dict, Any, Tuple
from colorama import Fore, Style

from src.data_storage import DataStorage, CONTACTS_FILE, STORAGE_VERSION

class NoteEntity:
    """Class for Note entity.
    Note has topic (string) and content (string). 
    Tag is optional parameter (list of strings)"""

    def __init__(self, topic: str, content: str, tag: str = None):
        self.tags = []
        self.topic = topic
        self.content = content
        if tag:
            lst_tags = tag.lower().strip().split(',')
            # Remove extra spaces around tags
            self.tags = list(map(str.strip, lst_tags))

    def __str__(self):
        if self.tags:
            tag_str = ", ".join(self.tags)
            return (f"Note topic {Fore.RED}{self.topic}{Style.RESET_ALL}, "
                    f"tags [{Fore.GREEN}{tag_str}{Style.RESET_ALL}]: {self.content}")

        return f"Note topic {Fore.RED}{self.topic}{Style.RESET_ALL}: {self.content}"
    
    # Methods for serialization (for saving/loading)
    def to_dict(self) -> Dict[str, Any]:
        """Convert NoteEntity to a serializable dictionary."""
        return {
            "topic": self.topic,
            "content": self.content,
            "tags": self.tags
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'NoteEntity':
        """Create a NoteEntity from a dictionary."""
        return cls(
            topic=data["topic"],
            content=data["content"],
            tags=data.get("tags", [])
        )


class Notes(UserList[NoteEntity]):
    """Class container for Notes entities.
    Inherits from UserList to manage a list of NoteEntity objects."""

    def __init__(self, notes: Dict[str, NoteEntity] | None = None):
        super().__init__()
        if notes:
            for note in notes.values():
                # The key is a normalized header
                self.data[self._normalize_topic(note.topic)] = note

    def __str__(self) -> str:
        if not self.data:
            return "No notes stored."
        return "\n".join(str(item) for item in self.data.values())
    
    # --- Internal Helper ---
    def _normalize_topic(self, topic: str) -> str:
        """Helper to normalize note topic for internal dictionary key."""
        stripped = topic.strip()
        if not stripped:
            raise ValueError("Topic cannot be empty.")
        return stripped.casefold()

    def add_note(self, topic: str, note: str, tag: str = None):
        """Add a new note to the list"""
        if self.find_note_by_topic(topic):
            return f"Note with topic {topic} already exists"

        self.data.append(NoteEntity(topic, note, tag))
        return "New note is added"

    def find_note_by_topic(self, topic: str):
        """Return note for the given topic or None if not found"""
        for item in self.data:
            if item.topic == topic:
                return item
        return None

    def edit_note(self, topic: str, new_note: str):
        """Edit the content of an existing note."""
        item = self.find_note_by_topic(topic)
        if item:
            item.content = new_note
            return "The note is changed."
        return "Note not found."

    def delete_note(self, topic: str):
        """Delete a note by its topic."""
        if not self.data:
            return "There are no notes to delete."
        item = self.find_note_by_topic(topic)
        if item:
            self.data.remove(item)
            return "The note is deleted."
        return f"Note with topic '{topic}' not found."

    def find_text_in_notes(self, text: str):
        """Find notes containing the given text in their content or topic."""
        results = []
        for item in self.data:
            if (text.lower().strip() in item.content.lower() or
                    text.lower().strip() in item.topic.lower()):
                results.append(item)
        return results

    def add_tag(self, topic: str, tag: str):
        """Add a tag to an existing note.
        May add multiple tags separated by commas."""
        tag_is_new = False
        item = self.find_note_by_topic(topic)
        if item:
            tag_lst = tag.lower().strip().split(",")
            tag_lst = list(map(str.strip, tag_lst))
            for tag_item in tag_lst:
                if tag_item not in item.tags:
                    tag_is_new = True
                    item.tags.append(tag_item)
            if tag_is_new:
                return "New tag(s) added."
            return "Such tag(s) already exist."
        return f"Note with topic '{topic}' not found."

    def edit_tag(self, topic: str, old_tag: str, new_tag: str):
        """Edit a tag of an existing note."""
        item = self.find_note_by_topic(topic)
        if item:
            if old_tag in item.tags:
                item.tags.remove(old_tag)
                item.tags.append(new_tag)
                return "The tag is changed."
            return f"Tag {old_tag} not found in the note."
        return f"Note with topic '{topic}' not found."

    def delete_tags(self, topic: str, tag: str):
        """Delete tags from an existing note.
        May delete multiple tags separated by commas."""
        tag_in_note_tags = False
        item = self.find_note_by_topic(topic)
        if item:
            tag_lst = tag.strip().split(",")
            tag_lst = list(map(str.strip, tag_lst))
            for tag_item in tag_lst:
                if tag_item in item.tags:
                    item.tags.remove(tag_item)
                    tag_in_note_tags = True
            if tag_in_note_tags:
                return "Tags deleted."
            return "No such tags in the note."
        return f"Note with topic '{topic}' not found."

    def search_by_tag(self, tag: str):
        """Find notes containing the given tag.
        Multiple tags separated by commas are not supported."""
        results = []
        for item in self.data:
            if tag.lower().strip() in item.tags:
                results.append(item)
        return results

    def sort_by_tag(self):
        """Return notes sorted by their first tag alphabetically."""
        if not self.data:
            return None
        return sorted(self.data, key=lambda x: x.tags[0] if x.tags else "")
