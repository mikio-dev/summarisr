from summarisr.summarise import Summarise


def test_summarise_returns_summary():
    """Test that summarise returns the summary."""
    # Set up
    summarise = Summarise()

    # Exercise
    summary = summarise.summarise(text="text")

    # Verify
    assert summary is not None
    assert len(summary) > 0
