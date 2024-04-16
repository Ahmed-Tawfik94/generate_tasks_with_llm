from typing import List 
from enum import Enum

from langchain_core.pydantic_v1 import BaseModel,Field
from .shared import Event, Hint
from random import choices
VerificationType=["draw_matching","code_matching","ai_verification","trainer"]

class CodePythonAnswerItem(BaseModel):
    py: str


class CodePythonPrecode(BaseModel):
    py: str

class CodePythonMetadata(BaseModel):
    answer: List[CodePythonAnswerItem]
    auto_verify: bool
    caption: str
    difficulty: int
    events: List[Event]
    hint: str
    hints: List[Hint]
    intro: str
    precode: CodePythonPrecode
    problem: str
    tag: List
    type: str
    verification_type: str = Field(default=choices(VerificationType))


class CodePython(BaseModel):
    metadata: CodePythonMetadata
    task_type: str = "code"
    code_language: str = "python"

class CodePythonList(BaseModel):
    tasks:List[CodePython]