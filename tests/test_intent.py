from config import GEMINI_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI

from agents.intent_parser import IntentParser


def test_intent_parser():

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        api_key=GEMINI_API_KEY,
        temperature=0,
    )

    agent = IntentParser(llm)

    state = {
        "user_prompt": "Create a cinematic wedding reel with warm colors and minimal captions.",
        "intent": {}
    }

    result = agent(state)

    assert result["intent"] is not None
    assert "style" in result["intent"]