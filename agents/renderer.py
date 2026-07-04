import subprocess
from pathlib import Path

from state import PipelineState


class Renderer:

    def __call__(self, state: PipelineState):

        # Don't render if compilation failed
        if state["compile_status"] != "SUCCESS":
            print("❌ Cannot render. Compilation failed.")
            state["render_status"] = "FAILED"
            return state

        print("🎬 Rendering video...")

        # Create output directory
        Path("output").mkdir(exist_ok=True)

        output_video = "output/video.mp4"

        try:

            result = subprocess.run(
                [
                    "npx",
                    "remotion",
                    "render",
                    "Video",
                    output_video,
                ],
                cwd="remotion",
                capture_output=True,
                text=True,
                check=True,
                shell=True,          # Required on Windows
            )

            print(result.stdout)

            print("✅ Video rendered successfully!")

            state["render_status"] = "SUCCESS"

            state["video_path"] = output_video

        except subprocess.CalledProcessError as e:

            print("❌ Rendering failed")

            print(e.stderr)

            state["render_status"] = "FAILED"

            state["video_path"] = ""

        return state