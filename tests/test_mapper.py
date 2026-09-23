from src.nist_mapper import map_controls

def test_known_mapping():
    item = map_controls({"category":"missing_patch"}, {"missing_patch":["SI-2","RA-5"]})
    assert item["nist_controls"] == ["SI-2", "RA-5"]

def test_default_mapping():
    item = map_controls({"category":"unknown"}, {})
    assert item["nist_controls"] == ["RA-5"]
