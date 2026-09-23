import argparse
from pathlib import Path
from time import perf_counter

from src.scanner_client import fetch_findings
from src.normalizer import normalize_finding
from src.risk_engine import enrich_risk
from src.nist_mapper import load_mapping, map_controls
from src.siem_client import send_events
from src.report_generator import generate_reports

ROOT = Path(__file__).resolve().parents[1]


def run(findings_path: str, mapping_path: str, report_dir: str):
    start = perf_counter()
    raw = fetch_findings(findings_path)
    mapping = load_mapping(mapping_path)
    processed = [map_controls(enrich_risk(normalize_finding(item)), mapping) for item in raw]
    siem_count = send_events(processed, str(Path(report_dir) / "siem_events.ndjson"))
    json_report, csv_report = generate_reports(processed, report_dir)
    elapsed = perf_counter() - start
    print(f"Processed findings: {len(processed)}")
    print(f"SIEM events generated: {siem_count}")
    print(f"Controls mapped: {sum(len(x['nist_controls']) for x in processed)}")
    print(f"Automated processing time: {elapsed:.4f}s")
    print(f"JSON report: {json_report}")
    print(f"CSV report: {csv_report}")
    return processed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GRC compliance automation MVP")
    parser.add_argument("--findings", default=str(ROOT / "data/sample_findings.json"))
    parser.add_argument("--mapping", default=str(ROOT / "config/nist_800_53_mapping.json"))
    parser.add_argument("--reports", default=str(ROOT / "reports"))
    args = parser.parse_args()
    run(args.findings, args.mapping, args.reports)
