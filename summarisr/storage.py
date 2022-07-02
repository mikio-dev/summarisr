# pylint: disable=E0611
from .document import Document


class Storage:
    """The class Storage is a singleton class that stores documents."""

    def __new__(cls):
        """Create an instance only if no instance has been created yet.
        If there is one, return the instance already created.
        https://python-patterns.guide/gang-of-four/singleton/
        """
        if not hasattr(cls, "instance"):
            cls.instance = super(Storage, cls).__new__(cls)
            cls.storage = {}
        return cls.instance

    def get(self, document_id: str) -> str:
        """Function to get a document from the storage."""
        return self.storage.get(document_id)

    def save(self, document: Document) -> str:
        """Funciton to save a document to the storage."""
        self.storage[document.id] = document
        return document.id
