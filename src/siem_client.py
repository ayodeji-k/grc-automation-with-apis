import json
from pathlib import Path


def send_events(findings: list[dict], output_path: str) -> int:
    """Mock SIEM integration. Writes newline-delimited JSON events."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for finding in findings:
            event = {"event_type": "grc_compliance_finding", **finding}
            handle.write(json.dumps(event) + "\n")
    return len(findings)
