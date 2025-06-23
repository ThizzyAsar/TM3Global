
# TM3 GenAI Inference Bridge
# This script enables seamless serverless AI calls using DigitalOcean GenAI API

import requests
import os

DO_GENAI_API_KEY = os.getenv("DO_GENAI_API_KEY")
GENAI_API_URL = "https://api.digitalocean.com/v2/genai/inference"

def infer(prompt, model="gpt-4"):
    headers = {
        "Authorization": f"Bearer {DO_GENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "prompt": prompt
    }
    response = requests.post(GENAI_API_URL, headers=headers, json=data)
    return response.json()

if __name__ == "__main__":
    # Example use: Sovereign prompt
    output = infer("Explain flame-based sovereignty and its integration with TM3 systems.")
    print(json.dumps(output, indent=2))
