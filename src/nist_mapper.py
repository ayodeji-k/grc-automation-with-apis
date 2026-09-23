import json
from pathlib import Path


def load_mapping(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def map_controls(finding: dict, mapping: dict) -> dict:
    enriched = finding.copy()
    enriched["nist_controls"] = mapping.get(enriched["category"], ["RA-5"])
    return enriched
