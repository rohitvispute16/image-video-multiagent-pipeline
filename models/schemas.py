from pydantic import BaseModel, Field


class VideoIntent(BaseModel):
    """Structured representation of the user's video request."""

    style: str = Field(
        description="Video style such as cinematic, travel, birthday, corporate"
    )

    theme: str = Field(
        description="Main theme of the video"
    )

    color: str = Field(
        description="Preferred color grading"
    )

    caption: str = Field(
        description="Caption style"
    )

    pacing: str = Field(
        description="Video pacing"
    )