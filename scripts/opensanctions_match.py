"""Screen one person against OpenSanctions via the /match API.

Pass name, date of birth and country, not just the name: fewer false positives.
Check request and response format, terms and licence in the current documentation.
Commercial use of the data requires a licence. Set OPENSANCTIONS_API_KEY.
For bulk checks, consider a local copy (yente) so customer names do not leave your systems.
"""
import os

import requests

URL = 'https://api.opensanctions.org/match/default'


def match_person(name, birth_date=None, nationality=None, api_key=None):
    api_key = api_key or os.environ['OPENSANCTIONS_API_KEY']
    props = {'name': [name]}
    if birth_date:
        props['birthDate'] = [birth_date]
    if nationality:
        props['nationality'] = [nationality]
    body = {'queries': {'q1': {'schema': 'Person', 'properties': props}}}
    r = requests.post(URL, json=body, headers={'Authorization': 'ApiKey ' + api_key}, timeout=30)
    r.raise_for_status()
    return r.json()['responses']['q1']['results']


if __name__ == '__main__':
    # Fictitious subject.
    for hit in match_person('Ivan Petrov', '1970-01-01', 'ru'):
        print(hit.get('caption'), '|', hit.get('score'), '|', hit.get('datasets'))
