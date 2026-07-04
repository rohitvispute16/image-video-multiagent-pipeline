from pathlib import Path

from models.remotion_schema import RemotionScript


class ScriptGenerator:

    def __init__(self, llm):
        self.llm = llm.with_structured_output(RemotionScript)

    def __call__(self, state):

        storyboard = state["storyboard"]

        prompt = f"""
You are an expert Remotion developer.

Generate a complete Video.tsx component.

Requirements:

- Use AbsoluteFill
- Use Sequence
- Use Img
- Display captions
- Use fade transitions
- Return ONLY valid TypeScript code.

Storyboard:

{storyboard}
"""

        result = self.llm.invoke(prompt)

        output_dir = Path("remotion/src")
        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / "Video.tsx"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result.code)

        state["remotion_code"] = result.code

        print("✅ Video.tsx generated successfully")

        return state