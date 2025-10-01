# TM3Global

## GenAI Inference Bridge

`genai_inference_bridge.py` dispatches prompts to either DigitalOcean GenAI or OpenAI.
Set the appropriate API key and run:

```bash
export DO_GENAI_API_KEY=your_do_key
python genai_inference_bridge.py "Hello Sovereign World"
```

If `DO_GENAI_API_KEY` is unset but `OPENAI_API_KEY` is available, the script will
use the OpenAI API instead.
