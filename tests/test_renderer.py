from agents.renderer import Renderer


def test_renderer():

    renderer = Renderer()

    state = {
        "compile_status": "SUCCESS",
        "render_status": "",
        "video_path": "",
    }

    result = renderer(state)

    assert result["render_status"] in [
        "SUCCESS",
        "FAILED",
    ]