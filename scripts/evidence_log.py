"""Evidence log helper: hash a saved file and append an entry to a JSONL log.

Illustrative. Run only on synthetic or lawfully obtained material.
Usage: python evidence_log.py FILE SOURCE_URL "note"
"""
import hashlib
import json
import sys
import time


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def log_evidence(path, source_url, note, log='evidence_log.jsonl'):
    entry = {
        'file': str(path),
        'sha256': sha256(path),
        'source': source_url,
        'note': note,
        'logged_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
    }
    with open(log, 'a', encoding='utf-8') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    return entry


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    print(log_evidence(*sys.argv[1:4]))
