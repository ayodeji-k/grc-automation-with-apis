import json
from pathlib import Path


def fetch_findings(path: str):
    """Mock vulnerability-scanner API adapter backed by JSON."""
    return json.loads(Path(path).read_text(encoding="utf-8"))
