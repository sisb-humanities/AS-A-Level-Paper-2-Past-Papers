"""Inject the master database into the tracker page template.

Usage: python3 -I build_page.py <master_json> <template_html> <out_html> <levels>
<levels> is either a 9708/2x mark scheme .txt (Tables A/B are cut from it) or levels.json
(claude/pipeline/levels.json in the Project: {"A": ..., "B": ...}, already cut from June 2026 MS 21).
"""
import json
import re
import sys
from pathlib import Path

master_path, tpl_path, out_path, levels_src = map(Path, sys.argv[1:5])
m = json.loads(master_path.read_text(encoding='utf-8'))

KEEP = ['id', 'paper_ref', 'year', 'series', 'series_code', 'variant', 'section', 'section_name', 'question', 'part',
        'subpart', 'label', 'choice', 'marks', 'ao3_marks', 'marking', 'command_word', 'command_word_2', 'diagram',
        'calculation', 'stem_patterns', 'topics', 'primary_topic', 'subtopics', 'key_concepts', 'context',
        'question_text', 'stimulus_title', 'mark_scheme', 'examiner_comment', 'flags', 'similar_to']
qs = []
for q in m['questions']:
    r = {k: q.get(k) for k in KEEP}
    r['ms_page'] = q['source']['mark_scheme_page']
    r['qp_page'] = q['source']['question_paper_page']
    # data / micro / macro: from the section (2023+: B = micro, C = macro); 2022 essays (one of Q2–Q4) from the topic unit
    if q['section'] == 'A':
        r['area'] = 'data'
    elif q['year'] >= 2023:
        r['area'] = 'micro' if q['section'] == 'B' else 'macro'
    else:
        r['area'] = 'micro' if q['primary_topic'].split('.')[0] in '123' else 'macro'
    qs.append(r)

if levels_src.suffix == '.json':
    levels = json.loads(levels_src.read_text(encoding='utf-8'))
else:
    # generic level descriptors (Tables A and B), taken verbatim from a 2026 mark scheme
    txt = levels_src.read_text(encoding='utf-8')

    def table(start, end):
        seg = txt[txt.index(start): txt.index(end, txt.index(start))]
        seg = re.sub(r'©.*?\n.*?Mark Scheme.*?\n\s*PUBLISHED\s*\n', '', seg, flags=re.S)
        lines = [l.strip() for l in seg.split('\n') if l.strip()]
        return '\n'.join(lines)

    levels = {
        'A': table('Table A: AO1 Knowledge and understanding and AO2 Analysis', 'Table B: AO3 Evaluation'),
        'B': table('Table B: AO3 Evaluation', 'Section A Data response'),
    }
assert set(levels) == {'A', 'B'} and all(levels.values())

data = {
    'topics': m['topics'],
    'units': m['units'],
    'stimuli': m['stimuli'],
    'examiner_reports': m['examiner_reports'],
    'levels': levels,
    'questions': qs,
}
blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
tpl = tpl_path.read_text(encoding='utf-8')
assert '/*__DATA__*/' in tpl
out_path.write_text(tpl.replace('/*__DATA__*/', blob), encoding='utf-8')
print(out_path, round(out_path.stat().st_size / 1024), 'KB,', len(qs), 'questions')
