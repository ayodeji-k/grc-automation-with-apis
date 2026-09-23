def severity_from_cvss(cvss: float) -> str:
    if not 0 <= cvss <= 10:
        raise ValueError("CVSS must be between 0 and 10")
    if cvss >= 9.0:
        return "CRITICAL"
    if cvss >= 7.0:
        return "HIGH"
    if cvss >= 4.0:
        return "MEDIUM"
    if cvss > 0:
        return "LOW"
    return "NONE"


def enrich_risk(finding: dict) -> dict:
    enriched = finding.copy()
    enriched["severity"] = severity_from_cvss(enriched["cvss"])
    return enriched
