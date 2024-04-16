from typing import List

from langchain_core.pydantic_v1 import BaseModel,Field, conlist,validator
from .shared import Hint
class QuestionAnswer(BaseModel):
    text: str
    value: int


class Question(BaseModel):
    success: str
    hint: str = Field(description="contain the hint of the correct answer")
    answers: conlist(QuestionAnswer,min_items=4 ,max_items=4) # type: ignore
    failed: str
    text: str
    answer: str = Field(description="contain the text of the correct answer")
    type: str = Field(description="this value will be setted to multiple choise if has more than one answer signle_choise if not")




class QuizMetadata(BaseModel):
    questions: conlist(Question,min_items=1, max_items=1) # type: ignore
    difficulty: int
    multi_choice: bool = Field(description="this value depends on the question if have multiple answers set to true else false ")
    caption: str
    intro: str
    tag: List
    hints: List[Hint] = ...

class Quiz(BaseModel):
    task_type: str = "html"
    action: str = "quiz"
    metadata: QuizMetadata

class QuizList(BaseModel):
    tasks:List[Quiz]
