from typing import List

from langchain_core.pydantic_v1 import BaseModel,Field, conlist

class LectureMetadata(BaseModel):
    auto_verify: bool = Field(description="",default=True)
    caption: str
    difficulty: int
    hint: str
    hints: List
    intro: str
    problem: str = Field(description="contains the content of the lesson lecture")
    tag: List


class Lecture(BaseModel):
    action: str = "text"
    task_type: str = "html"
    metadata: LectureMetadata
