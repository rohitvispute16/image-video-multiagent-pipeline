from pathlib import Path

from models.remotion_schema import RemotionScript


class RetryAgent:

    def __init__(self, llm):

        self.llm = llm.with_structured_output(
            RemotionScript
        )

    def __call__(self, state):

        if state["compile_status"] == "SUCCESS":

            print("Nothing to fix.")

            return state

        if state["retries"] >= 3:

            print("Maximum retry attempts reached.")

            return state

        print(f"Retry Attempt {state['retries'] + 1}")

        prompt = f"""
You are an expert React + TypeScript + Remotion developer.

The following code failed to compile.

Compiler Error:

{state["compile_error"]}

Current Video.tsx:

{state["remotion_code"]}

Fix every compiler error.

Return ONLY the corrected TypeScript code.
"""

        result = self.llm.invoke(prompt)

        Path("remotion/src").mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            "remotion/src/Video.tsx",
            "w",
            encoding="utf-8"
        ) as f:

            f.write(result.code)

        state["remotion_code"] = result.code

        state["retries"] += 1

        print("✓ Video.tsx updated")

        return state