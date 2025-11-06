import os
import sys
from pathlib import Path
from unittest import mock

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import genai_inference_bridge as bridge  # noqa: E402


def _mock_response(json_payload):
    response = mock.Mock()
    response.json.return_value = json_payload
    response.raise_for_status.return_value = None
    return response


def test_infer_success():
    expected = {"result": "ok"}
    session = mock.Mock()
    session.post.return_value = _mock_response(expected)
    with mock.patch.dict(os.environ, {"DO_GENAI_API_KEY": "token"}, clear=True):
        result = bridge.infer("hello", session=session)
    session.post.assert_called_once_with(
        bridge.GENAI_API_URL,
        headers={
            "Authorization": "Bearer token",
            "Content-Type": "application/json",
        },
        json={"model": "gpt-4", "prompt": "hello"},
        timeout=bridge.DEFAULT_TIMEOUT,
    )
    assert result == expected


def test_infer_missing_key():
    session = mock.Mock()
    with mock.patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError):
            bridge.infer("hello", session=session)


def test_infer_invalid_prompt():
    with mock.patch.dict(os.environ, {"DO_GENAI_API_KEY": "token"}, clear=True):
        with pytest.raises(ValueError):
            bridge.infer("   ")


def test_infer_request_failure():
    session = mock.Mock()
    session.post.side_effect = requests.RequestException("boom")
    with mock.patch.dict(os.environ, {"DO_GENAI_API_KEY": "token"}, clear=True):
        with pytest.raises(bridge.GenAIInferenceError):
            bridge.infer("hello", session=session)


def test_infer_bad_json():
    response = mock.Mock()
    response.raise_for_status.return_value = None
    response.json.side_effect = ValueError("bad json")
    session = mock.Mock()
    session.post.return_value = response
    with mock.patch.dict(os.environ, {"DO_GENAI_API_KEY": "token"}, clear=True):
        with pytest.raises(bridge.GenAIInferenceError):
            bridge.infer("hello", session=session)
