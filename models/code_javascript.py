from typing import List

from langchain_core.pydantic_v1 import BaseModel,Field, conlist
from shared import Event, Hint
class CodeJavascriptAnswerItem(BaseModel):
    javascript: str


class CodeJavascriptPrecode(BaseModel):
    javascript: str


class CodeJavascriptMetadata(BaseModel):
    answer: List[CodeJavascriptAnswerItem]
    auto_verify: bool
    caption: str
    difficulty: int
    events: List[Event]
    hint: str
    hints: List[Hint]
    intro: str
    precode: CodeJavascriptPrecode
    problem: str
    tag: List
    type: str
    verification_type: str


class CodeJavascript(BaseModel):
    metadata: CodeJavascriptMetadata
    task_type: str = "html"
