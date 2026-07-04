from agents.retry_agent import RetryAgent


class FakeResponse:
    code = "export const Video = () => null;"


class FakeLLM:

    def with_structured_output(self, schema):
        return self

    def invoke(self, prompt):
        return FakeResponse()


def test_retry():

    retry = RetryAgent(FakeLLM())

    state = {
        "compile_status": "FAILED",
        "compile_error": "Cannot find Img",
        "retries": 0,
        "remotion_code": "bad code",
    }

    result = retry(state)

    assert result["retries"] == 1

    assert result["remotion_code"] == "export const Video = () => null;"