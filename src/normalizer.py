def normalize_finding(raw: dict) -> dict:
    required = ("id", "asset", "title", "category", "cvss", "status", "remediation")
    missing = [key for key in required if key not in raw]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")
    return {
        "finding_id": str(raw["id"]),
        "asset": str(raw["asset"]),
        "title": str(raw["title"]),
        "category": str(raw["category"]).lower(),
        "cve": raw.get("cve"),
        "cvss": float(raw["cvss"]),
        "status": str(raw["status"]).upper(),
        "remediation": str(raw["remediation"]),
        "evidence": {"source": "mock-vulnerability-scanner", "scanner_id": str(raw["id"])},
    }
