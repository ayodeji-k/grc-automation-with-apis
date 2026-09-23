import csv
import json
from pathlib import Path


def generate_reports(findings: list[dict], report_dir: str) -> tuple[str, str]:
    directory = Path(report_dir)
    directory.mkdir(parents=True, exist_ok=True)
    json_path = directory / "audit_report.json"
    csv_path = directory / "audit_report.csv"
    json_path.write_text(json.dumps(findings, indent=2), encoding="utf-8")
    fields = ["finding_id", "asset", "title", "cve", "cvss", "severity", "status", "nist_controls", "remediation"]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for finding in findings:
            row = {key: finding.get(key) for key in fields}
            row["nist_controls"] = ";".join(finding.get("nist_controls", []))
            writer.writerow(row)
    return str(json_path), str(csv_path)
