from typing import List

from langchain_core.pydantic_v1 import BaseModel,Field, conlist

class VideoMetadata(BaseModel):
    difficulty: int
    caption: str
    faqs: List
    hint: str
    hints: List
    intro: str
    tag: List
    video: str
    video_source: str


class Video(BaseModel):
    index: int
    task_type: str = "html"
    metadata: VideoMetadata
