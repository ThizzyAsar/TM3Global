import sys
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import genai_inference_bridge as bridge  # noqa: E402


def test_infer_success():
    expected = {"result": "ok"}
    with mock.patch("genai_inference_bridge.requests.post") as post:
        post.return_value.json.return_value = expected
        bridge.DO_GENAI_API_KEY = "token"
        result = bridge.infer("hello")
        post.assert_called_once()
        assert result == expected


def test_infer_missing_key():
    bridge.DO_GENAI_API_KEY = ""
    with mock.patch("genai_inference_bridge.requests.post"):
        try:
            bridge.infer("hello")
            assert False, "Expected ValueError"
        except ValueError:
            pass
