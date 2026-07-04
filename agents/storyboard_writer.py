from models.storyboard_schema import Scene
from rag.retriever import get_retriever
from models.storyboard_schema import Storyboard
from utils.cache import load_cache, save_cache

CACHE_FILE = "output/cache/storyboard.json"
class StoryboardWriter:

    def __init__(self, llm):
        self.llm = llm.with_structured_output(Storyboard)
        
    def __call__(self, state):
        cached = load_cache(CACHE_FILE)

        if cached:
            print("✓ Loaded Storyboard from cache")
            state["storyboard"] = cached
            return state

        retriever = get_retriever()
        docs = retriever.invoke(query)
       
        context = "\n".join(
            doc.page_content
            for doc in docs
        )

        prompt = f"""
            Context
            {context}

            Intent
            {state['intent']}

            Images
            {state['image_analysis']}

            Generate storyboard.
            """

        storyboard = self.llm.invoke(prompt)

        state["storyboard"] = [
            scene.model_dump()
            for scene in storyboard.scenes
        ]
        save_cache(
            CACHE_FILE,
            state["storyboard"]
        )

        print("✓ Storyboard cached")
        return state