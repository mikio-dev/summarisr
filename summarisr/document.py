# pylint: disable=E0611
from pydantic import BaseModel


class Document(BaseModel):
    id: str
    text: str
    summary: str
