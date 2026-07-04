from langgraph.graph import StateGraph, START, END

from state import PipelineState

from agents.intent_parser import IntentParser
from agents.image_analyzer import ImageAnalyzer
from agents.storyboard_writer import StoryboardWriter
from agents.script_generator import ScriptGenerator
from agents.compiler import CompilerAgent
from agents.retry_agent import RetryAgent
from agents.renderer import Renderer
from agents.drive_downloader import DriveDownloader


def compiler_router(state: PipelineState):
    """
    Decide what happens after compilation.

    SUCCESS  -> Renderer
    FAILED   -> Retry Agent
    3 Retries -> END
    """

    if state["compile_status"] == "SUCCESS":
        print("\n✅ Compilation successful")
        return "renderer"

    if state["retries"] >= 3:
        print("\n❌ Maximum retry attempts reached.")
        return END

    print(f"\n🔁 Retrying... Attempt {state['retries'] + 1}")
    return "retry"


def build_graph(llm):
    """
    Build and compile the LangGraph workflow.
    """

    # --------------------------------------------------
    # Create Agents
    # --------------------------------------------------

    intent = IntentParser(llm)

    image = ImageAnalyzer()

    storyboard = StoryboardWriter(llm)

    script = ScriptGenerator(llm)

    compiler = CompilerAgent()

    retry = RetryAgent(llm)

    renderer = Renderer()

    download = DriveDownloader()

    # --------------------------------------------------
    # Create Workflow
    # --------------------------------------------------

    workflow = StateGraph(PipelineState)

    # --------------------------------------------------
    # Add Nodes
    # --------------------------------------------------

    workflow.add_node("intent", intent)

    workflow.add_node("image", image)

    workflow.add_node("storyboard", storyboard)

    workflow.add_node("script", script)

    workflow.add_node("compiler", compiler)

    workflow.add_node("retry", retry)

    workflow.add_node("renderer", renderer)

    workflow.add_node("download", download)

    # --------------------------------------------------
    # Entry Point
    # --------------------------------------------------

    workflow.set_entry_point("download")

    # --------------------------------------------------
    # Main Pipeline
    # --------------------------------------------------

    workflow.add_edge("download", "intent")
    workflow.add_edge("intent", "image")

    workflow.add_edge("image", "storyboard")

    workflow.add_edge("storyboard", "script")

    workflow.add_edge("script", "compiler")

    # --------------------------------------------------
    # Conditional Routing
    # --------------------------------------------------

    workflow.add_conditional_edges(
        "compiler",
        compiler_router,
        {
            "renderer": "renderer",
            "retry": "retry",
            END: END,
        },
    )

    # --------------------------------------------------
    # Retry Loop
    # --------------------------------------------------

    workflow.add_edge(
        "retry",
        "compiler"
    )

    # --------------------------------------------------
    # Finish
    # --------------------------------------------------

    workflow.add_edge(
        "renderer",
        END
    )

    # --------------------------------------------------
    # Compile Graph
    # --------------------------------------------------

    graph = workflow.compile()

    return graph