from pydantic import BaseModel, Field


class ImageMetadata(BaseModel):
    image: str = Field(description="Image filename")
    description: str = Field(description="Short description")
    people: int = Field(description="Number of people visible")
    emotion: str = Field(description="Main emotion")
    importance: float = Field(description="Importance score between 0 and 1")