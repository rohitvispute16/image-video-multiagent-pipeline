from config import GEMINI_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI

from agents.storyboard_writer import StoryboardWriter


def test_storyboard():

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        api_key=GEMINI_API_KEY,
        temperature=0,
    )

    agent = StoryboardWriter(llm)

    state = {
        "intent": {
            "style": "cinematic",
            "theme": "wedding",
        },

        "image_analysis": [
            {
                "image": "img1.jpg",
                "analysis": {
                    "description": "Bride smiling",
                    "emotion": "happy",
                },
            }
        ],

        "storyboard": [],
    }

    result = agent(state)

    assert len(result["storyboard"]) > 0