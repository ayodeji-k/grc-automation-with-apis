from src.normalizer import normalize_finding

def test_normalizer():
    raw = {"id":"1","asset":"host","title":"Issue","category":"vulnerability","cvss":7.5,"status":"open","remediation":"Patch"}
    item = normalize_finding(raw)
    assert item["finding_id"] == "1"
    assert item["status"] == "OPEN"
    assert item["evidence"]["source"] == "mock-vulnerability-scanner"
