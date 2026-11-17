"""Fuzzy name matching for screening. A high score is a hypothesis, not proof.

Cyrillic, Arabic and Chinese names need transliteration first (see docs/02).
Tune the similarity threshold on your own data.
"""
import unicodedata

from rapidfuzz import fuzz, process


def norm(s):
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.lower().replace('-', ' ').replace(',', ' ')
    return ' '.join(sorted(s.split()))


def best_matches(query, candidates, limit=3):
    return process.extract(norm(query), [norm(c) for c in candidates],
                           scorer=fuzz.token_set_ratio, limit=limit)


if __name__ == '__main__':
    # Fictitious names only.
    print(best_matches('Petrov, Ivan', ['Ivan Petrov', 'Petrov Ivan A.', 'Ivanov Petr']))
