# TM3Global

This repository demonstrates TM3's generative AI integrations. It includes
sample code for an OpenAI real-time voice server, a DigitalOcean GenAI
inference bridge, and website assets.

## Running the Node server

The Node server is stored in the file `Bash `. It requires Node.js 20 or later
and the `OPENAI_API_KEY` environment variable.

Install dependencies and start the server:

```bash
npm install express node-fetch dotenv
node 'Bash '
```

The server listens on port **4000** and exposes `/session` to obtain
OpenAI real-time session tokens.

## Running the Python bridge

`genai_inference_bridge.py` calls DigitalOcean GenAI. It needs Python 3 and
`DO_GENAI_API_KEY`.

Install the dependency and run:

```bash
pip install requests
python genai_inference_bridge.py
```

## Environment variables

- `OPENAI_API_KEY` – OpenAI API token used by the Node server.
- `DO_GENAI_API_KEY` – DigitalOcean GenAI token used by the Python bridge.

## Purpose

These examples show how TM3 software can integrate OpenAI's real-time
capabilities with DigitalOcean's GenAI service and front-end assets.
