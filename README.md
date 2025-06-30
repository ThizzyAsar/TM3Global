# TM3 Global

This repository contains a minimal demo of the TM3 Flame Sovereign Portal. The project includes a small Flask web app, a Node.js helper service for creating OpenAI realtime sessions and a Python bridge to DigitalOcean's GenAI API.

## Local setup

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   npm install express node-fetch dotenv --prefix server
   ```
2. **Set environment variables**
   Create a `.env` file based on `.env.example` and fill in the required API keys.
3. **Run the Flask app**
   ```bash
   python app.py
   ```
4. **Run the Node.js service**
   ```bash
   node server/index.js
   ```

## DigitalOcean GenAI

The `genai_inference_bridge.py` script demonstrates how to call DigitalOcean's GenAI API. Set `DO_GENAI_API_KEY` and run:

```bash
python genai_inference_bridge.py
```


