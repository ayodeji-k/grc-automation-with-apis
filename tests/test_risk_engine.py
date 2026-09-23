from src.risk_engine import severity_from_cvss

def test_severity_boundaries():
    assert severity_from_cvss(9.0) == "CRITICAL"
    assert severity_from_cvss(8.1) == "HIGH"
    assert severity_from_cvss(6.0) == "MEDIUM"
    assert severity_from_cvss(2.0) == "LOW"
    assert severity_from_cvss(0.0) == "NONE"
