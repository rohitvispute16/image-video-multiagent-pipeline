import subprocess
from pathlib import Path

from state import PipelineState


class CompilerAgent:

    def __call__(self, state: PipelineState):

        print("🔨 Compiling Remotion project...")

        remotion_dir = Path("remotion").resolve()

        print("Project Path:", remotion_dir)

        if not remotion_dir.exists():

            state["compile_status"] = "FAILED"
            state["compile_error"] = f"Remotion folder not found: {remotion_dir}"

            return state

        result = subprocess.run(
            [
                "npm",
                "exec",
                "remotion",
                "bundle"
            ],
            cwd=remotion_dir,
            capture_output=True,
            text=True,
            shell=True
        )

        if result.returncode == 0:

            print("✅ Compilation Successful")

            state["compile_status"] = "SUCCESS"

            state["compile_error"] = None

        else:

            print("❌ Compilation Failed")

            state["compile_status"] = "FAILED"

            state["compile_error"] = result.stderr + "\n" + result.stdout

        return state