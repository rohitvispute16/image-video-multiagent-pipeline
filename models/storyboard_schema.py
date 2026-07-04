from typing import List
from pydantic import BaseModel

class Scene(BaseModel):
    scene: int
    image: str
    duration: int
    caption: str
    transition: str

class Storyboard(BaseModel):
    scenes: List[Scene]