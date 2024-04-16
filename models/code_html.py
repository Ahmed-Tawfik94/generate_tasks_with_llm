
from typing import List

from langchain_core.pydantic_v1 import BaseModel,Field, conlist
from .shared import Event, Hint
class CodeHtmlAnswerItem(BaseModel):
    html: str


class CodeHtmlPrecode(BaseModel):
    html: str


class CodeHtmlMetadata(BaseModel):
    answer: List[CodeHtmlAnswerItem]
    auto_verify: bool
    caption: str
    difficulty: int
    drawing: bool
    events: List[Event]
    hint: str
    hints: List[Hint]
    intro: str
    precode: CodeHtmlPrecode
    problem: str
    tag: List
    type: str
    verification_type: str


class CodeHtml(BaseModel):
    metadata: CodeHtmlMetadata
    task_type: str = "html"

