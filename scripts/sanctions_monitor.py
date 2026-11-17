"""Compare today's sanctions export with the previous snapshot and re-screen clients.

Usage: python sanctions_monitor.py clients.txt [snapshot_dir]
clients.txt: one client name per line. Every hit must go through manual review
against the indicators in docs/04-screening.md and be recorded in the decision log.
Check the file path against the OpenSanctions documentation; commercial use of the
data requires a licence. Illustrative: not run against the live service.
"""
import csv
import io
import json
import pathlib
import sys
import time

import requests
from rapidfuzz import fuzz

from name_matching import norm

URL = 'https://data.opensanctions.org/datasets/latest/sanctions/targets.simple.csv'


def load_targets(url=URL):
    r = requests.get(url, timeout=180)
    r.raise_for_status()
    rows = csv.DictReader(io.StringIO(r.text))
    return {row['id']: row for row in rows}


def diff_targets(old, new):
    added = [new[k] for k in new.keys() - old.keys()]
    removed = [old[k] for k in old.keys() - new.keys()]
    changed = [new[k] for k in new.keys() & old.keys() if new[k] != old[k]]
    return added, removed, changed


def rescreen(clients, added, threshold=88):
    hits = []
    for rec in added:
        for c in clients:
            score = fuzz.token_set_ratio(norm(c), norm(rec.get('name', '')))
            if score >= threshold:
                hits.append((c, rec.get('name'), rec.get('id'), score))
    return hits


def latest_snapshot(snap_dir):
    files = sorted(pathlib.Path(snap_dir).glob('targets_*.json'))
    if not files:
        return None, {}
    return files[-1], json.loads(files[-1].read_text(encoding='utf-8'))


def run(clients, snap_dir='snapshots', fetch=load_targets):
    pathlib.Path(snap_dir).mkdir(exist_ok=True)
    prev_path, old = latest_snapshot(snap_dir)
    new = fetch()
    out = pathlib.Path(snap_dir) / f'targets_{time.strftime("%Y-%m-%d")}.json'
    out.write_text(json.dumps(new, ensure_ascii=False), encoding='utf-8')
    if not old:
        return None  # first run: nothing to compare yet
    added, removed, changed = diff_targets(old, new)
    return {'previous': str(prev_path), 'added': len(added), 'removed': len(removed),
            'changed': len(changed), 'hits': rescreen(clients, added)}


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    names = [l.strip() for l in open(sys.argv[1], encoding='utf-8') if l.strip()]
    print(run(names, *(sys.argv[2:3])))
