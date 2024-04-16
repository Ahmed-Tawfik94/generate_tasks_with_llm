from typing import List

from langchain_core.pydantic_v1 import BaseModel,Field, conlist
from .shared import Event, Hint
class CodeCssAnswerItem(BaseModel):
    css: str
    html: str


class CodeCssPrecode(BaseModel):
    css: str
    html: str


class CodeCssMetadata(BaseModel):
    answer: List[CodeCssAnswerItem]
    auto_verify: bool
    caption: str
    difficulty: int
    drawing: bool
    events: List[Event]
    hint: str
    hints: List[Hint]
    intro: str
    precode: CodeCssPrecode
    problem: str
    tag: List
    type: str
    verification_type: str


class CodeCss(BaseModel):
    metadata: CodeCssMetadata
    task_type: str = "html"
