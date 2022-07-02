from summarisr.document import Document
from summarisr.storage import Storage


def test_storage_get_returns_None():
    """Test that get returns the document."""
    # Set up
    storage = Storage()

    # Exercise
    document = storage.get("1")

    #
    assert document is None


def test_storage_get_returns_document():
    """Test that get returns the document."""
    # Set up
    storage = Storage()
    storage.storage["1"] = "document"

    # Exercise
    document = storage.get("1")

    #
    assert document == "document"


def test_storage_save_returns_document_id():
    """Test that get returns the document."""
    # Set up
    storage = Storage()
    document = Document(id="1", text="text", summary="summary")

    # Exercise
    output = storage.save(document=document)

    # Verify
    assert output == "1"
