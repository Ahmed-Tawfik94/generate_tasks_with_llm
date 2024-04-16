from typing import List

from langchain_core.pydantic_v1 import BaseModel,Field, conlist


class Event(BaseModel):
    caption: str
    key: str

class Hint(BaseModel):
    cost: float
    text: str
