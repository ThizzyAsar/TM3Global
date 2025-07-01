# TM3 Global

This repository provides a minimal Flask application that serves as a placeholder dashboard for the TM3 Flame Sovereign System.

## Development

Install the required dependencies and run the application locally:

```bash
pip install -r requirements.txt
python app.py
```

The server will start on port `5000` and expose a basic health-check endpoint at `/healthz`.

## Testing

Unit tests are provided using `pytest`. Run all tests with:

```bash
pytest -q
```
