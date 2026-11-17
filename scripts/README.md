# Scripts

Small illustrative helpers that go with [docs/07-tools.md](../docs/07-tools.md).

| Script | What it does |
| --- | --- |
| `evidence_log.py` | Hash a saved file and append an entry to a JSONL evidence log |
| `name_matching.py` | Normalise names and score fuzzy matches (hypothesis only) |
| `opensanctions_match.py` | Screen one person through the OpenSanctions `/match` API |
| `sanctions_monitor.py` | Diff two sanctions snapshots and re-screen a client list |

```
pip install -r requirements.txt
```

Tested only on synthetic local data. The two OpenSanctions scripts were never run against the live service: check the documentation, terms and licence first. Use fictitious or lawfully obtained data only.
