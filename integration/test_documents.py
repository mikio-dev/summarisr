import pytest
from fastapi import HTTPException


def test_post_documents_returns_document(client):

    # Set up
    session, api_url = client
    url = f"{api_url}/documents/"
    data = {"text": "This is a test document"}

    # Exercise
    res = session.post(url=url, data=data)

    # Verify
    res_json = res.json()
    assert res.status_code == 201
    assert res_json is not None


@pytest.mark.parametrize(
    "input_text",
    [
        "This is a test document",
        """The Zen of Python, by Tim Peters

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
""",
    ],
    ids=["one-line", "multi-line"],
)
def test_get_documents_returns_summary(client, input_text):

    # Set up
    session, api_url = client
    url = f"{api_url}/documents/"
    data = {"text": input_text}

    # Exercise
    res_post = session.post(url=url, data=data)
    res_post_json = res_post.json()
    document_id = res_post_json["document_id"]
    res_get = session.get(url=f"{url}{document_id}")

    # Verify
    res_json = res_get.json()
    assert res_post.status_code == 201
    assert res_get.status_code == 200
    assert res_json["document_id"] == document_id
    assert len(res_json["summary"]) <= len(data["text"])


def test_get_documents_with_non_existent_id_returns_404(client):

    # Set up
    session, api_url = client
    url = f"{api_url}/documents/"

    # Exercise
    # with pytest.raises(HTTPException) as excinfo:
    res = session.get(url=f"{url}non-existent-id")

    # Verify
    assert res.status_code == 404
    assert res.json()["detail"] == "Document not found"
