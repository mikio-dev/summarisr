from unittest.mock import MagicMock

import pytest

from summarisr.main import Document


@pytest.fixture
def long_text():
    text = """
        The Zen of Python, by Tim Peters

        Beautiful is better than ugly.
        Explicit is better than implicit.
        Simple is better than complex.
        Complex is better than complicated.
        Flat is better than nested.
        Sparse is better than dense.
        Readability counts.
        Special cases aren't special enough to break the rules.
        Although practicality beats purity.
        Errors should never pass silently.
        Unless explicitly silenced.
        In the face of ambiguity, refuse the temptation to guess.
        There should be one-- and preferably only one --obvious way to do it.
        Although that way may not be obvious at first unless you're Dutch.
        Now is better than never.
        Although never is often better than *right* now.
        If the implementation is hard to explain, it's a bad idea.
        If the implementation is easy to explain, it may be a good idea.
        Namespaces are one honking great idea -- let's do more of those!
    """
    return "".join(text.split("\n"))


@pytest.fixture
def non_ascii_text():
    text = """
        Français
        Русский
        日本語
    """
    return "".join(text.split("\n"))


@pytest.fixture
def storage():
    mock = MagicMock()
    mock.get.return_value = Document(id=1, text="text", summary="summary")
    mock.save.return_value = "1"
    return mock


@pytest.fixture
def storage_none():
    mock = MagicMock()
    mock.get.return_value = None
    return mock


@pytest.fixture
def summarise():
    mock = MagicMock()
    mock.summarise.return_value = "summary"
    return mock
