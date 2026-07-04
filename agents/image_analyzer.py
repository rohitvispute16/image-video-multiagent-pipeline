import os
from PIL import Image
import google.generativeai as genai

from config import GEMINI_API_KEY
from state import PipelineState

from utils.cache import load_cache, save_cache

from config import IMAGE_FOLDER

CACHE_FILE = "output/cache/image_analysis.json"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


class ImageAnalyzer:

    def __call__(self, state: PipelineState):
        cached = load_cache(CACHE_FILE)

        if cached:
            print("✓ Loaded Image Analysis from cache")
            state["image_analysis"] = cached
            return state

        results = []

        image_folder = IMAGE_FOLDER

        for filename in os.listdir(image_folder):

            if filename.lower().endswith((".jpg", ".jpeg", ".png")):

                image_path = os.path.join(image_folder, filename)

                image = Image.open(image_path)

                prompt = """
Analyze this image.

Return JSON only.

{
  "description":"",
  "people":0,
  "emotion":"",
  "importance":0.0
}
"""

                response = model.generate_content(
                    [prompt, image]
                )

                results.append({
                    "image": filename,
                    "analysis": response.text
                })

        state["image_analysis"] = results
        save_cache(
            CACHE_FILE,
            results
        )

        print("✓ Image Analysis cached")

        return state