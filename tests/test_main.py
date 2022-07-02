from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException

from summarisr import main


@pytest.mark.asyncio
async def test_root_succeeds():
    """Test that root() returns a default message."""
    output = await main.root()
    assert output == {"message": "ok"}


@pytest.mark.asyncio
async def test_upload_text_with_long_text_returns_document_id(
    long_text, storage, summarise
):
    """Test that uploading a long text returns the document_id."""

    # Set up
    main.uuid = MagicMock()
    main.uuid.uuid4.return_value = "1"

    # Exercise
    output = await main.upload_text(
        text=long_text, storage=storage, summarise=summarise
    )

    # Verify
    assert output == {"document_id": "1"}


@pytest.mark.asyncio
async def test_upload_text_with_non_ascii_text_returns_document_id(
    non_ascii_text, storage, summarise
):
    """Test that uploading a non-ascii text returns the document_id."""

    # Set up
    main.uuid = MagicMock()
    main.uuid.uuid4.return_value = "1"

    # Exercise
    output = await main.upload_text(
        text=non_ascii_text, storage=storage, summarise=summarise
    )

    # Verify
    assert output == {"document_id": "1"}


@pytest.mark.asyncio
async def test_upload_text_with_empty_text_returns_document_id(storage, summarise):
    """Test that uploading an empty text returns the document_id."""

    # Set up
    main.uuid = MagicMock()
    main.uuid.uuid4.return_value = "1"

    # Exercise
    output = await main.upload_text(text="", storage=storage, summarise=summarise)

    # Verify
    assert output == {"document_id": "1"}


@pytest.mark.asyncio
async def test_get_summary_returns_summary(storage) -> None:
    """Test that get_summary returns the summary."""

    # Set up

    # Exercise
    output = await main.get_summary(document_id="1", storage=storage)

    # Verify
    assert output == {"document_id": "1", "summary": "summary"}


@pytest.mark.asyncio
async def test_get_summary_with_unknown_id_returns_404(storage_none) -> None:
    """Test that get_summary with an unknown id returns 404."""

    # Set up

    # Exercise
    with pytest.raises(HTTPException) as excinfo:
        await main.get_summary(document_id="1", storage=storage_none)

    # Verify
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "Document not found"
