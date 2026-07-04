from typing import TypedDict, List, Dict, Optional


class PipelineState(TypedDict):
    # User input
    user_prompt: str

    # Input images
    images: List[str]

    # Image analysis results
    image_analysis: list
   
    # Parsed user intent
    intent: Dict

    # Storyboard
    storyboard: List[Dict]

    # Generated Remotion code
    remotion_code: str

    # Compilation error (if any)
    compile_error: str | None
    compile_status: str

    # Retry count
    retries: int

    # Rendering status
    render_status: str

    # Final output video path
    video_path: str

    