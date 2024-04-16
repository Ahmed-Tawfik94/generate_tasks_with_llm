
from typing import List

from langchain_core.pydantic_v1 import BaseModel,Field, conlist
from .shared import Event

class BlankCodeAnswerItem(BaseModel):
    py: str


class BlankCodePrecode(BaseModel):
    py: str


class BlankCodePy(BaseModel):
    field_0: List[str] = Field(..., alias='0')


class BlankCodeSolution(BaseModel):
    py: BlankCodePy


class BlankCodeMetadata(BaseModel):
    answer: List[BlankCodeAnswerItem]
    caption: str
    update_difficulty: bool
    difficulty: int
    events: List[Event]
    language: str
    hint: str
    hints: List
    intro: str
    precode: BlankCodePrecode
    problem: str
    type: str
    tag: List
    auto_verify: bool
    solution: BlankCodeSolution


class BlankCode(BaseModel):
    task_type: str = "html"
    action: str = "blank_code"
    metadata: BlankCodeMetadata
