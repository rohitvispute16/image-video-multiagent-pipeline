import google.generativeai as genai

from config import (
    GEMINI_API_KEY,
    TEXT_MODEL,
    VISION_MODEL
)

# Configure API
genai.configure(api_key=GEMINI_API_KEY)

# Create reusable model objects
text_model = genai.GenerativeModel(TEXT_MODEL)
vision_model = genai.GenerativeModel(VISION_MODEL)