import uuid

from fastapi import Depends, FastAPI, Form, HTTPException

from .document import Document
from .storage import Storage
from .summarise import Summarise

# Application layer
app = FastAPI(title="Summarisr API", openapi_url="/openapi.json")


@app.get("/")
async def root():
    return {"message": "ok"}


@app.post("/documents/", status_code=201)
async def upload_text(
    text: str = Form(),
    storage: Storage = Depends(Storage),
    summarise: Summarise = Depends(Summarise),
) -> str:
    """
    The endpoint to upload a text document.
    :param text: The text to be summarised.
    :param storage: The storage instance to save the document.
    :return: The document ID.
    """
    document_id = str(uuid.uuid4())
    summary = summarise.summarise(text)
    document = Document(id=document_id, text=text, summary=summary)
    storage.save(document=document)
    return {"document_id": document_id}


@app.get("/documents/{document_id}", status_code=200)
async def get_summary(document_id: str, storage: Storage = Depends(Storage)) -> dict:
    """
    The endpoint to get the summary of a document.
    :param document_id: The document ID.
    :param storage: The storage instance to get the document.
    :return: The summary of the document in JSON.
    """
    text = storage.get(document_id)
    if text is None:
        raise HTTPException(status_code=404, detail="Document not found")

    return {"document_id": text.id, "summary": text.summary}
