"""Merge a partial build (new papers only) into the master JSON, then redo the repeat detection over everything.

Usage: python3 -I merge_master.py <master_json> <new_partial_json> <out_json>
The partial is build.py's output for a raw.json holding only the new papers. Papers already in the master are
refused (re-extract everything with build.py instead). Batches, topics and the AO3 note come from the partial
(it carries the current build.py BATCH_LOG); stimuli and examiner reports are combined.
"""
import difflib
import json
import re
import sys
from pathlib import Path

old = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
new = json.loads(Path(sys.argv[2]).read_text(encoding='utf-8'))
out_path = Path(sys.argv[3])

old_refs = {q['paper_ref'] for q in old['questions']}
new_refs = {q['paper_ref'] for q in new['questions']}
clash = old_refs & new_refs
assert not clash, f'papers already in the master: {sorted(clash)}'

MONTH = {'m': 3, 's': 6, 'w': 11}
records = old['questions'] + new['questions']
records.sort(key=lambda x: (x['year'], MONTH[x['series_code'][0]], x['variant'], x['question'], x['part'], len(x['subpart']), x['subpart']))
assert len({r['id'] for r in records}) == len(records), 'duplicate ids'


def norm(s):  # same as build.py
    return re.sub(r'\W+', ' ', (s or '').replace('’', "'")).strip().lower()


# repeat detection (same rule as build.py): different papers, same primary topic, shared sub-topic, wording >= 0.55
before = {r['id']: {x['id'] for x in r['similar_to']} for r in old['questions']}
for a in records:
    a['similar_to'] = []
for i, a in enumerate(records):
    for b in records[i + 1:]:
        if a['paper_ref'] == b['paper_ref'] or a['primary_topic'] != b['primary_topic'] or not set(a['subtopics']) & set(b['subtopics']):
            continue
        ratio = difflib.SequenceMatcher(None, norm(a['question_text']), norm(b['question_text'])).ratio()
        if ratio >= 0.55:
            a['similar_to'].append({'id': b['id'], 'similarity': round(ratio, 2)})
            b['similar_to'].append({'id': a['id'], 'similarity': round(ratio, 2)})
# old-old links must not change (they depend only on the two records)
for r in old['questions']:
    now = {x['id'] for x in r['similar_to'] if x['id'] in before}
    assert now == before[r['id']], f'repeat links changed for {r["id"]}'

batches = new['batches']
for b in batches:
    b['rows'] = sum(1 for x in records if x['batch'] == b['id'])
    # keep examiner-report notes recorded on the master (e.g. by add_er.py)
    ob = next((o for o in old['batches'] if o['id'] == b['id']), None)
    if ob and ob.get('examiner_reports'):
        b['examiner_reports'] = sorted(set(b.get('examiner_reports', [])) | set(ob['examiner_reports']))

master = {**new, 'batches': batches, 'stimuli': {**old['stimuli'], **new['stimuli']},
          'examiner_reports': {**old['examiner_reports'], **new['examiner_reports']}, 'questions': records}
out_path.write_text(json.dumps(master, ensure_ascii=False, indent=1), encoding='utf-8')
links = sum(len(r['similar_to']) for r in records) // 2
new_links = sum(1 for r in new['questions'] for x in r['similar_to'])
print(f'papers {len(old_refs)} + {len(new_refs)} = {len(old_refs | new_refs)}; parts {len(records)}; repeat pairs {links} '
      f'(links touching new papers: {new_links})')
