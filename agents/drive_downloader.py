import os
import shutil
import gdown

from state import PipelineState


class DriveDownloader:

    def __call__(self, state: PipelineState):

        drive_url = state.get("drive_url")

        if not drive_url:
            print("📁 Using local images.")
            return state

        input_folder = "input/images"
        public_folder = "remotion/public"

        os.makedirs(input_folder, exist_ok=True)
        os.makedirs(public_folder, exist_ok=True)

        # Clear old images
        for folder in [input_folder, public_folder]:
            for file in os.listdir(folder):
                path = os.path.join(folder, file)

                if os.path.isfile(path):
                    os.remove(path)

                elif os.path.isdir(path):
                    shutil.rmtree(path)

        print("⬇ Downloading Google Drive folder...")

        gdown.download_folder(
            url=drive_url,
            output=input_folder,
            quiet=False,
            use_cookies=False,
        )

        print("\nDownloaded files:")

        # Find images recursively
        for root, _, files in os.walk(input_folder):

            for file in files:

                if file.lower().endswith((".jpg", ".jpeg", ".png")):

                    src = os.path.join(root, file)

                    # Copy image to top-level input/images
                    dst_input = os.path.join(input_folder, file)

                    if src != dst_input:
                        shutil.copy2(src, dst_input)

                    # Copy image to Remotion public
                    dst_public = os.path.join(public_folder, file)

                    shutil.copy2(dst_input, dst_public)

                    print(file)

        print("✅ Images copied to Remotion.")

       

        return state