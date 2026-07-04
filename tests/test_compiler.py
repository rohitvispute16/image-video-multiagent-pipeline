from agents.compiler import CompilerAgent


def test_compiler():

    compiler = CompilerAgent()

    state = {
        "compile_status": "",
        "compile_error": None,
    }

    result = compiler(state)

    assert result["compile_status"] in [
        "SUCCESS",
        "FAILED",
    ]