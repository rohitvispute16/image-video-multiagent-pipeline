from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

# Base project directory
BASE_DIR = Path(__file__).resolve().parent

# Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Models
TEXT_MODEL = "gemini-2.5-flash"
VISION_MODEL = "gemini-2.5-flash"

# Folders
INPUT_FOLDER = BASE_DIR / "input"
IMAGE_FOLDER = INPUT_FOLDER / "images"

OUTPUT_FOLDER = BASE_DIR / "output"
CACHE_DIR = OUTPUT_FOLDER / "cache"

# Cache files
INTENT_CACHE = CACHE_DIR / "intent.json"
IMAGE_CACHE = CACHE_DIR / "image_analysis.json"
STORYBOARD_CACHE = CACHE_DIR / "storyboard.json"