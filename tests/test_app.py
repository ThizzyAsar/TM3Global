import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import app  # noqa: E402


def test_home():
    client = app.app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200


def test_healthz():
    client = app.app.test_client()
    resp = client.get("/healthz")
    assert resp.status_code == 200
    assert resp.data == b"OK"
