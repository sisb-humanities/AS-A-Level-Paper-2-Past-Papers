"""Merge extraction + tags into the master JSON (the review workbook is made from it by workbook.py).

Usage: python3 -I build.py <scratch_dir> <txt_dir> <out_dir>
With only some papers' text in <txt_dir>/raw.json, the output holds only those papers: merge it with merge_master.py.
"""
import json
import re
import sys
from pathlib import Path

scratch, txt_dir, out_dir = map(Path, sys.argv[1:4])
sys.path.insert(0, str(scratch))
from tags import T, TOPIC_NAMES, UNIT_NAMES  # noqa: E402


raw = json.loads((scratch / 'raw.json').read_text(encoding='utf-8'))
from tags2 import T2  # noqa: E402
try:
    from tags3 import T3  # noqa: E402  (2023 papers, batch7)
    T2.update(T3)
except ImportError:
    pass
OFF_SYLLABUS = {}
try:
    from tags4 import T4, OFF_SYLLABUS  # noqa: E402  (2022 papers, batch9 — 2020–22 syllabus)
    T2.update(T4)
except ImportError:
    pass
try:
    from tags5 import T5, OFF_SYLLABUS5  # noqa: E402  (2021 papers, batch10 — 2020–22 syllabus)
    T2.update(T5)
    OFF_SYLLABUS = {**OFF_SYLLABUS, **OFF_SYLLABUS5}
except ImportError:
    pass
import difflib  # noqa: E402

SERIES = {'June': ('May/June', 's', 'M/J'), 'November': ('Oct/Nov', 'w', 'O/N'), 'March': ('Feb/March', 'm', 'F/M')}
AO3_RULE = {1: 0, 2: 0, 4: 1, 6: 2, 8: 2, 12: 4}
BATCH_OF = {}
for _p in [('June', 2025, '21'), ('June', 2026, '21'), ('June', 2026, '22')]:
    BATCH_OF[_p] = 'pilot-2026-10-08'
for _p in [('June', 2025, '23'), ('June', 2025, '24'), ('November', 2025, '23'), ('November', 2025, '24'), ('June', 2026, '23'), ('June', 2026, '24')]:
    BATCH_OF[_p] = 'batch2-2026-10-08'
for _p in [('November', 2025, '21'), ('November', 2025, '22')]:
    BATCH_OF[_p] = 'batch3-2026-10-08'
for _p in [('June', 2025, '22'), ('November', 2024, '21'), ('November', 2024, '22'), ('November', 2024, '23'), ('March', 2024, '22')]:
    BATCH_OF[_p] = 'batch4-2026-10-08'
for _p in [('June', 2024, '21'), ('June', 2024, '22'), ('June', 2024, '23')]:
    BATCH_OF[_p] = 'batch5-2026-10-08'
for _p in [('March', 2023, '22'), ('June', 2023, '21'), ('June', 2023, '22'), ('June', 2023, '23'), ('November', 2023, '21'), ('November', 2023, '22'), ('November', 2023, '23')]:
    BATCH_OF[_p] = 'batch7-2026-10-08'
for _p in [('March', 2022, '22'), ('June', 2022, '21'), ('June', 2022, '22'), ('June', 2022, '23'), ('November', 2022, '21'), ('November', 2022, '22'), ('November', 2022, '23')]:
    BATCH_OF[_p] = 'batch9-2026-10-08'
for _p in [('March', 2021, '22'), ('June', 2021, '21'), ('June', 2021, '22'), ('June', 2021, '23'), ('November', 2021, '21'), ('November', 2021, '22'), ('November', 2021, '23')]:
    BATCH_OF[_p] = 'batch10-2026-10-08'
ER = json.loads((scratch / 'er.json').read_text(encoding='utf-8')) if (scratch / 'er.json').exists() else {}
BATCH_LOG = [
    {'id': 'pilot-2026-10-08', 'papers': ['9708/21 s25', '9708/21 s26', '9708/22 s26']},
    {'id': 'batch2-2026-10-08', 'papers': ['9708/23 s25', '9708/24 s25', '9708/23 w25', '9708/24 w25', '9708/23 s26', '9708/24 s26']},
    {'id': 'batch3-2026-10-08', 'papers': ['9708/21 w25', '9708/22 w25']},
    {'id': 'batch4-2026-10-08', 'papers': ['9708/22 s25', '9708/21 w24', '9708/22 w24', '9708/23 w24', '9708/22 m24'], 'examiner_reports': ['Nov 2024', 'March 2024']},
    {'id': 'batch5-2026-10-08', 'papers': ['9708/21 s24', '9708/22 s24', '9708/23 s24'], 'examiner_reports': ['June 2024']},
    {'id': 'batch6-2026-10-08', 'papers': [], 'examiner_reports': ['June 2025', 'June 2026', 'Nov 2025']},
    {'id': 'batch7-2026-10-08', 'papers': ['9708/22 m23', '9708/21 s23', '9708/22 s23', '9708/23 s23', '9708/21 w23', '9708/22 w23', '9708/23 w23']},
    {'id': 'batch8-2026-10-08', 'papers': [], 'examiner_reports': ['June 2023', 'March 2023', 'Nov 2023']},
    {'id': 'batch9-2026-10-08', 'papers': ['9708/22 m22', '9708/21 s22', '9708/22 s22', '9708/23 s22', '9708/21 w22', '9708/22 w22', '9708/23 w22'], 'examiner_reports': ['June 2022', 'March 2022', 'Nov 2022']},
    {'id': 'batch10-2026-10-08', 'papers': ['9708/22 m21', '9708/21 s21', '9708/22 s21', '9708/23 s21', '9708/21 w21', '9708/22 w21', '9708/23 w21']},
    {'id': 'batch11-2026-10-08', 'papers': [], 'examiner_reports': ['March 2021', 'Nov 2021']},
]
CHECKED_BY_JAMES = {'9708_s25_21_Q1c', '9708_s25_21_Q5b', '9708_s26_21_Q3b', '9708_s26_21_Q5b', '9708_s26_22_Q1a', '9708_s26_22_Q2b'}
NEEDS_REMOVED_DATA = {'9708_s25_24_Q1d', '9708_m21_22_Q1a'}  # m21 Q1(a) needs the removed Table 1.1 (price index)
# The redaction rule assumes a Table/Fig reference means removed data; here the figure/table is in the public paper
_PART = 'Section A source partly removed for copyright; this part can still be attempted from general knowledge.'
_CHART22 = 'Chart needed: Fig. 1.1 is a line chart with no printed values, so the source extract here cannot show it. Use the original paper.'
NOT_REMOVED = {'9708_s22_22_Q1ai': _CHART22, '9708_s22_22_Q1aii': _CHART22, '9708_s22_22_Q1aiii': _CHART22,
               '9708_s22_22_Q1c': _PART}  # Table 1.1 (budget balance) is printed in full  # refers to a period shown only in the removed Fig. 1.1
EXTRA_FLAGS = {'9708_s26_22_Q1a': 'Mark scheme tolerance symbols (±) did not survive PDF extraction: shown as "(.0.2)" / "( 0.2)". Check against the PDF.',
               # charts with no printed values: the public paper has them, the text extract cannot
               '9708_s23_23_Q1a': 'Chart needed: Fig. 1.1 is a bar chart with no printed values, so the source extract here cannot show it. Use the original paper.',
               '9708_w23_23_Q1b': 'Chart needed: Fig. 1.1 is a line chart with no printed values, so the source extract here cannot show it. Use the original paper.',
               '9708_s22_23_Q1a': 'Chart needed: Fig. 1.1 is a bar chart with no printed values, so the source extract here cannot show it. Use the original paper.',
               '9708_s22_23_Q1bi': 'Chart needed: Fig. 1.2 is a line chart with no printed values, so the source extract here cannot show it. Use the original paper.',
               '9708_s21_23_Q1ai': 'Chart needed: Fig. 1.1 is a line chart with no printed values, so the source extract here cannot show it. Use the original paper.',
               '9708_s21_23_Q1aii': 'Chart needed: Fig. 1.2 is a line chart with no printed values, so the source extract here cannot show it. Use the original paper.',
               '9708_w21_23_Q1a': 'Chart needed: Fig. 1.1 is a bar chart with no printed values, so the source extract here cannot show it. Use the original paper.',
               '9708_w21_23_Q1bii': 'Chart needed: Fig. 1.1 is a bar chart with no printed values, so the source extract here cannot show it (Table 1.1 is included). Use the original paper.'}
# Parts where the mark scheme's evaluation allowance differs from the AO3 rule
AO3_OVERRIDE = {'9708_w23_23_Q1c': 2}  # 4-mark 'State two ... and consider': up to 2 marks for the judgement


def norm(s):
    return re.sub(r'\W+', ' ', (s or '').replace('’', "'")).strip().lower()


def strip_leaked_question(question, ms):
    """Mark schemes that split a preamble from the question leave the question line at the top of the MS body."""
    paras = ms.split('\n')
    first = paras[0]
    if 20 < len(first) < 500 and not first.startswith(('•', 'Up to', 'Use Table', 'For ', 'AO')):
        if difflib.SequenceMatcher(None, norm(first), norm(question)[-len(norm(first)) - 15:]).ratio() > 0.8:
            return '\n'.join(paras[1:]).strip()
    return ms


def redaction_flag(question, stim):
    if not stim or 'Content removed' not in stim:
        return None
    if re.search(r'\b(Table|Figs?\.)\s*\d', question):
        return 'Needs data removed from the published paper (copyright): the table/figure this part refers to is not in the public copy.'
    for quote in re.findall(r'‘([^’]{6,})’', question):
        if norm(quote) not in norm(stim):
            return 'Quotes source text removed from the published paper (copyright); answerable only in general terms from this copy.'
    return 'Section A source partly removed for copyright; this part can still be attempted from general knowledge.'


def find_page(stem, pattern):
    pages = (txt_dir / f'{stem}.txt').read_text(encoding='utf-8').split('\f')
    for i, p in enumerate(pages, 1):
        if re.search(pattern, p, re.M):
            return i
    return None


def qp_page(stem, qnum, part):
    pages = (txt_dir / f'{stem}.txt').read_text(encoding='utf-8').split('\f')
    if qnum == '1':
        start = next(i for i, p in enumerate(pages) if 'Section A' in p)
        for i in range(start, len(pages)):
            if re.search(rf'^\s+\({part}\)\s', pages[i], re.M):
                return i + 1
        return None
    start = next(i for i, p in enumerate(pages) if 'Section B' in p)
    for i in range(start, len(pages)):
        p = pages[i][pages[i].find('Section B'):] if i == start else pages[i]
        m = re.search(rf'^{qnum}\s+\S', p, re.M)
        if m:
            if part == 'a' or re.search(rf'^\s+\({part}\)\s', p[m.end():], re.M):
                return i + 1
            return i + 2
    return None


def stem_patterns(q):
    ql = q.lower()
    pats = []
    if re.search(r'\b(always|only|alone|inevitable)\b', ql):
        pats.append('absolute claim (always/only/alone)')
    if re.search(r'\boutweigh', ql):
        pats.append('benefits vs costs')
    if re.search(r'\b(more effective|more damaging|more harmful|stronger than|better than|the best way|should be reduced through)\b', ql) or re.search(r'\bwhether (either )?.+ or .+', ql):
        pats.append('compare two options')
    if 'extent' in ql:
        pats.append('to what extent')
    if 'diagram' in ql:
        pats.append('diagram required')
    if re.search(r'using (the data in )?table', ql) or 'calculate' in ql:
        pats.append('uses data')
    return pats


records = []
for r in raw:
    sname, y, v, q = r['series'], r['year'], r['variant'], r['qid']
    slabel, scode, sshort = SERIES[sname]
    tag = T2.get((sname, y, v, q)) or T[(y, v, q)]
    qnum, part = q[0], q[2]
    subpart = (re.search(r'\)\((\w+)\)$', q) or [None, ''])[1]
    old_syllabus = y <= 2022  # 2020–22 syllabus: Section B = one essay from Q2–Q4, point-based mark schemes
    if old_syllabus:
        section = 'A' if qnum == '1' else 'B'
    else:
        section = 'A' if qnum == '1' else ('B' if qnum in '23' else 'C')
    question = r['question_qp'] or r['question_ms']
    marks = r['marks_qp'] or r['marks_ms']
    ms_stem = f'9708 Economics {sname} {y} Mark Scheme  {v}'
    qp_stem = ms_stem.replace('Mark Scheme', 'Question Paper') if r['question_qp'] else None
    rid = f'9708_{scode}{str(y)[2:]}_{v}_Q{qnum}{part}{subpart}'
    stim_all = next((x['stimulus_text'] for x in raw if (x['series'], x['year'], x['variant']) == (sname, y, v) and x['qid'].startswith('1(a)')), None)
    flags = []
    if section == 'A':
        f = redaction_flag(question, stim_all)
        if rid in NOT_REMOVED and f:
            f = NOT_REMOVED[rid]
        if rid in NEEDS_REMOVED_DATA and f:
            f = 'Needs data removed from the published paper (copyright): the table/figure this part refers to is not in the public copy.'
        if f:
            flags.append(f)
    if rid in EXTRA_FLAGS:
        flags.append(EXTRA_FLAGS[rid])
    if rid in OFF_SYLLABUS:
        flags.append(OFF_SYLLABUS[rid])
    rec = {
        'id': rid,
        'syllabus': '9708', 'level': 'AS', 'paper': 2, 'paper_name': 'AS Level Data Response and Essays',
        'series': slabel, 'series_code': f'{scode}{str(y)[2:]}', 'year': y, 'variant': v,
        'component': f'9708/{v}', 'paper_ref': f'9708/{v}/{sshort}/{str(y)[2:]}', 'section': section,
        'section_name': 'Data response' if section == 'A' else ('Essay (2020–22 syllabus)' if old_syllabus else {'B': 'Microeconomics essay', 'C': 'Macroeconomics essay'}[section]),
        'question': int(qnum), 'part': part, 'subpart': subpart, 'label': f'{qnum}({part})' + (f'({subpart})' if subpart else ''),
        'choice': '' if section == 'A' else ('One of 2, 3 or 4' if old_syllabus else ('Either 2 or 3' if section == 'B' else 'Either 4 or 5')),
        'marks': marks,
        # 2022 mark schemes have no AO labels: evaluation marks are read from each mark scheme (tags4 'ao3')
        'ao3_marks': tag['ao3'] if old_syllabus else AO3_OVERRIDE.get(rid, AO3_RULE[marks]),
        'marking': 'points (2020–22 mark scheme)' if old_syllabus else ('levels (Tables A & B)' if marks == 12 else 'points'),
        'command_word': tag['cmd'], 'command_word_2': tag['cmd2'],
        'diagram': 'diagram' in question.lower(),
        'calculation': tag['cmd'] == 'Calculate',
        'stem_patterns': stem_patterns(question),
        'topics': tag['topics'],
        'primary_topic': tag['topics'][0],
        'subtopics': tag['sub'],
        'units': sorted({t.split('.')[0] for t in tag['topics']}),
        'key_concepts': tag['concepts'],
        'context': tag['context'],
        'question_text': question,
        'stimulus_title': r['stimulus_title'] if section == 'A' else None,
        'mark_scheme': strip_leaked_question(question, r['mark_scheme']),
        'examiner_comment': ER.get(f'{sname} {y} {v}', {}).get('parts', {}).get(q),
        'source': {
            'mark_scheme_file': f'{ms_stem}.pdf',
            'mark_scheme_page': find_page(ms_stem, rf'^\s{{0,8}}{re.escape(q)}(?:\(i\))?\s{{2,}}'),  # (i): s23/23 MS mislabels 1(b) as 1(b)(i)
            'question_paper_file': f'{qp_stem}.pdf' if qp_stem else None,
            'question_paper_page': qp_page(qp_stem, qnum, part) if qp_stem else None,
            'question_text_from': 'question paper' if r['question_qp'] else 'mark scheme',
        },
        'flags': flags,
        'review_status': 'sample checked by James' if rid in CHECKED_BY_JAMES else 'unreviewed',
        'batch': BATCH_OF[(sname, y, v)],
    }
    records.append(rec)

MONTH = {'m': 3, 's': 6, 'w': 11}
records.sort(key=lambda x: (x['year'], MONTH[x['series_code'][0]], x['variant'], x['question'], x['part'], len(x['subpart']), x['subpart']))

# near-duplicate questions across papers (recurring questions)
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

stimuli = {}
for r in raw:
    if r['qid'] in ('1(a)', '1(a)(i)'):
        slabel, scode, _ = SERIES[r['series']]
        key = f"9708_{scode}{str(r['year'])[2:]}_{r['variant']}_Q1"
        stimuli[key] = {
            'title': r['stimulus_title'],
            'text': r['stimulus_text'],
            'complete': bool(r['stimulus_text']) and 'Content removed' not in (r['stimulus_text'] or ''),
        }

for b in BATCH_LOG:
    b['rows'] = sum(1 for x in records if x['batch'] == b['id'])

master = {
    'schema_version': 1,
    'syllabus': '9708 Cambridge International AS & A Level Economics',
    'topic_codes_from': '9708 syllabus for 2026–2028 (v2); AS numbering 1.1–6.5 matches the 2023–2025 syllabus',
    'topics': TOPIC_NAMES,
    'units': UNIT_NAMES,
    'ao3_rule': 'AO3 (evaluation) marks by part size: 1→0, 2→0, 4→1, 6→2, 8→2, 12→4 (checked against every 2023–26 mark scheme; one exception: 9708/23 Oct/Nov 2023 Q1(c), 4 marks with 2 for evaluation). 2022 papers (2020–22 syllabus) have no AO labels: evaluation marks are read from each mark scheme; 8-mark essay parts have none.',
    'batches': BATCH_LOG,
    'stimuli': stimuli,
    'examiner_reports': {f"9708/{k.split()[2]}/{SERIES[k.split()[0]][2]}/{k.split()[1][2:]}": {'key_messages': v['key_messages'], 'general': v['general']} for k, v in ER.items()},
    'questions': records,
}
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / '9708_AS_past_papers.json').write_text(json.dumps(master, ensure_ascii=False, indent=1), encoding='utf-8')

print('records', len(records), 'papers', len({r['paper_ref'] for r in records}))
