from state import PipelineState
from models.schemas import VideoIntent
from state import PipelineState
from utils.cache import load_cache, save_cache

CACHE_FILE = "output/cache/intent.json"


class IntentParser:
    def __init__(self, llm):
        self.llm = llm.with_structured_output(VideoIntent)

    def __call__(self, state: PipelineState):
        cached = load_cache(CACHE_FILE)

        if cached:
            print("✓ Loaded Intent from cache")
            state["intent"] = cached
            return state

        prompt = state["user_prompt"]
        result = self.llm.invoke(prompt)
        state["intent"] = result.model_dump()

        save_cache(CACHE_FILE, state["intent"])
        print("✓ Intent cached")

        return state