from config import GEMINI_API_KEY
from graph.pipeline import build_graph
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=GEMINI_API_KEY,
    temperature=0,
)

graph = build_graph(llm)
user_prompt = input("Describe your video:\n> ")

drive_url = "https://drive.google.com/drive/folders/1LjPfQljJ71lsA1gKo4ZN-SCHwBfxSyk9"

state = {
    "user_prompt": user_prompt,

    "drive_url": drive_url,

    "images": [],

    "image_analysis": [],

    "intent": {},

    "storyboard": [],

    "remotion_code": "",

    "compile_status": "",

    "compile_error": None,

    "retries": 0,

    "render_status": "",

    "video_path": "",
}

result = graph.invoke(state)

print("\n==============================")
print("PIPELINE FINISHED")
print("==============================")

print(result)