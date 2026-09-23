# Architecture

```text
Vulnerability Findings (mock API / JSON)
        |
        v
Scanner Adapter -> Normalizer -> Risk Engine -> NIST 800-53 Mapper
                                             |             |
                                             v             v
                                      SIEM Event Sink   Audit Reports
                                      (mock NDJSON)     (JSON + CSV)
```

The adapters are deliberately isolated so the mock scanner and SIEM can later be replaced with authenticated REST API clients for tools such as Wazuh and a vulnerability-management platform.
