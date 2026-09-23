# GRC Compliance Automation MVP

A portfolio-ready Python MVP that converts vulnerability findings into traceable GRC evidence. It normalizes scanner data, assigns CVSS-based severity, maps findings to a small NIST SP 800-53 control set, emits SIEM-compatible JSON events, and generates audit-oriented JSON/CSV reports.

## Current scope

- Mock vulnerability scanner adapter using JSON input
- Finding normalization and evidence metadata
- CVSS severity classification
- Sample NIST SP 800-53 mapping: RA-5, SI-2, CM-6, AC-6, SI-4
- Mock SIEM integration using newline-delimited JSON
- JSON and CSV audit reports
- Pytest unit tests
- Processing-time instrumentation

> The control mapping is an illustrative starting point for a portfolio lab. A production compliance determination requires organization-specific control implementation context, assessment procedures, and human review.

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.main
```

Expected output includes the number of findings processed, SIEM events generated, controls mapped, processing time, and report paths.

## Test

```bash
pytest -q
```

## Outputs

Running the pipeline creates:

- `reports/audit_report.json`
- `reports/audit_report.csv`
- `reports/siem_events.ndjson`

## Next milestones

1. Add authenticated Wazuh API integration.
2. Add a real vulnerability-management REST API adapter.
3. Expand the control catalog and make mappings evidence/rule driven.
4. Add remediation SLA and overdue-finding logic.
5. Add manual-review baseline measurement to quantify time savings.
6. Generate a polished PDF audit evidence package.
