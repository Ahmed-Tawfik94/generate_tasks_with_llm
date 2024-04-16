from typing import List

from langchain_core.pydantic_v1 import BaseModel,Field, conlist
from .shared import  Hint
class BlankMetadata(BaseModel):
    answer: str
    caption: str
    difficulty: int
    hint: str
    hints: List[Hint]
    intro: str
    precode: str
    problem: str
    tag: List
    type: str


class Blank(BaseModel):
    task_type: str = "html"
    action: str = "blank"
    metadata: BlankMetadata
    code_language: str
