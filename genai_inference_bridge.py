# TM3 GenAI Inference Bridge
# This script enables seamless serverless AI calls using DigitalOcean GenAI API

import json
import os
from typing import Any, Mapping, Optional

import requests

GENAI_API_URL = "https://api.digitalocean.com/v2/genai/inference"
DEFAULT_TIMEOUT = 30


class GenAIInferenceError(RuntimeError):
    """Raised when an inference request fails for non-user reasons."""


def _get_api_key(explicit_key: Optional[str] = None) -> str:
    """Return the API key to use for the request."""

    api_key = explicit_key or os.getenv("DO_GENAI_API_KEY")
    if not api_key:
        raise ValueError("DO_GENAI_API_KEY environment variable is not set")
    return api_key


def infer(
    prompt: str,
    model: str = "gpt-4",
    *,
    api_key: Optional[str] = None,
    session: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Mapping[str, Any]:
    """Call the DigitalOcean GenAI inference endpoint and return the JSON response."""

    if not isinstance(prompt, str) or not prompt.strip():
        raise ValueError("prompt must be a non-empty string")

    key = _get_api_key(api_key)
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }
    data = {"model": model, "prompt": prompt}
    request_client = session or requests

    try:
        response = request_client.post(
            GENAI_API_URL,
            headers=headers,
            json=data,
            timeout=timeout or DEFAULT_TIMEOUT,
        )
        response.raise_for_status()
    except requests.RequestException as exc:  # pragma: no cover - exception path
        raise GenAIInferenceError("Failed to call DigitalOcean GenAI API") from exc

    try:
        return response.json()
    except ValueError as exc:  # pragma: no cover - exception path
        raise GenAIInferenceError("DigitalOcean GenAI API returned non-JSON data") from exc


if __name__ == "__main__":
    # Example use: Sovereign prompt
    output = infer(
        "Explain flame-based sovereignty and its integration with TM3 systems."
    )
    print(json.dumps(output, indent=2))
