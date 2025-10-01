#!/usr/bin/env python3
"""TM3 GenAI Inference Bridge

Routes prompts to DigitalOcean GenAI or OpenAI depending on available API keys.
"""

import json
import os
import requests
import sys

DO_GENAI_API_KEY = os.getenv("DO_GENAI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

GENAI_API_URL = "https://api.digitalocean.com/v2/genai/inference"
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

def infer(prompt: str, model: str = "gpt-4") -> dict:
    """Call the DigitalOcean GenAI API."""
    if not DO_GENAI_API_KEY:
        raise ValueError("DigitalOcean API key not set")
    headers = {
        "Authorization": f"Bearer {DO_GENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {"model": model, "prompt": prompt}
    response = requests.post(GENAI_API_URL, headers=headers, json=data)
    return response.json()

def infer_openai(prompt: str, model: str = "gpt-4o") -> dict:
    """Fallback inference using the OpenAI API."""
    if not OPENAI_API_KEY:
        raise ValueError("OpenAI API key not set")
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
    }
    response = requests.post(OPENAI_API_URL, headers=headers, json=data)
    return response.json()

def main(argv: list[str]) -> None:
    if len(argv) < 2:
        raise SystemExit("Usage: python genai_inference_bridge.py <prompt>")

    prompt = argv[1]
    if DO_GENAI_API_KEY:
        output = infer(prompt)
    elif OPENAI_API_KEY:
        output = infer_openai(prompt)
    else:
        raise SystemExit("No API key provided")

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main(sys.argv)
