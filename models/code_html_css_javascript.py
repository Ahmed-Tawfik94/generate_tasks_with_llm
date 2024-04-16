from typing import List

from langchain_core.pydantic_v1 import BaseModel,Field, conlist
from .shared import Event, Hint
class CodeHtmlCssJavascriptAnswerItem(BaseModel):
    css: str
    html: str
    javascript: str


class CodeHtmlCssJavascriptPrecode(BaseModel):
    css: str
    html: str
    javascript: str


class CodeHtmlCssJavascriptMetadata(BaseModel):
    answer: List[CodeHtmlCssJavascriptAnswerItem]
    auto_verify: bool
    caption: str
    difficulty: int
    drawing: bool
    events: List[Event]
    hint: str
    hints: List[Hint]
    intro: str
    precode: CodeHtmlCssJavascriptPrecode
    problem: str
    publish_web: bool
    tag: List
    type: str
    verification_type: str


class CodeHtmlCssJavascript(BaseModel):
    metadata: CodeHtmlCssJavascriptMetadata
    task_type: str = "html"


