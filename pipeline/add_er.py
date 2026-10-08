"""Merge examiner reports into the master JSON without re-extracting the papers.

For batches that add only examiner reports for papers already in the database (no PDFs of the papers needed).
Usage: python3 -I add_er.py <master_json> <er_json> <batch_id> <out_json>
er_json is the output of er_parse.py. Existing comments are only replaced if the text differs (reported).
"""
import json
import sys
from pathlib import Path

master_path, er_path, batch_id, out_path = sys.argv[1], sys.argv[2], sys.argv[3], Path(sys.argv[4])
m = json.loads(Path(master_path).read_text(encoding='utf-8'))
er = json.loads(Path(er_path).read_text(encoding='utf-8'))
SHORT = {'June': 'M/J', 'November': 'O/N', 'March': 'F/M'}
LABEL = {'June': 'June', 'November': 'Nov', 'March': 'March'}

by_ref = {}
for q in m['questions']:
    by_ref.setdefault(q['paper_ref'], {})[q['label']] = q

added, changed, series_done = 0, 0, []
for key, rep in er.items():
    series, year, comp = key.split()
    ref = f'9708/{comp}/{SHORT[series]}/{year[2:]}'
    if ref not in by_ref:
        print(f'skip {key}: paper {ref} not in the database yet')
        continue
    labels = by_ref[ref]
    missing = [l for l in labels if l not in rep['parts']]
    extra = [p for p in rep['parts'] if p not in labels]
    assert not missing and not extra, f'{ref}: report parts do not match database (missing {missing}, extra {extra})'
    for lab, q in labels.items():
        new = rep['parts'][lab]
        if q.get('examiner_comment') is None:
            added += 1
        elif q['examiner_comment'] != new:
            changed += 1
            print(f'changed {q["id"]}')
        q['examiner_comment'] = new
    m['examiner_reports'][ref] = {'key_messages': rep['key_messages'], 'general': rep['general']}
    s = f'{LABEL[series]} {year}'
    if s not in series_done:
        series_done.append(s)

batch = next((b for b in m['batches'] if b['id'] == batch_id), None)
if batch is None:
    batch = {'id': batch_id, 'papers': [], 'rows': 0}
    m['batches'].append(batch)
batch['examiner_reports'] = sorted(set(batch.get('examiner_reports', []) + series_done))

n = sum(1 for q in m['questions'] if q['examiner_comment'])
papers = len({q['paper_ref'] for q in m['questions'] if q['examiner_comment']})
out_path.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding='utf-8')
print(f'added {added}, changed {changed}; parts with a comment: {n} of {len(m["questions"])} from {papers} papers; '
      f'reports: {len(m["examiner_reports"])}')
