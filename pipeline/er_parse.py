"""Parse Cambridge 9708 examiner reports into per-question-part comments for Paper 2 variants.

Usage: python3 -I er_parse.py <er_dir> <out_json>
Output: {"<Series> <Year> <variant>": {"key_messages": str, "general": str, "parts": {"1(a)": str, ...}}}
"""
import json
import re
import sys
from pathlib import Path

import pdfplumber

er_dir, out_path = Path(sys.argv[1]), Path(sys.argv[2])

FOOTER = re.compile(
    r'^(©\s*\d{4}|© UCLES \d{4}|Cambridge International Advanced (Subsidiary )?(and Advanced )?Level|ECONOMICS|'
    r'9708 Economics (June|November|March) \d{4}|Principal Examiner Report for Teachers|\d{1,2})\s*$')

SUBHEAD = re.compile(r'^(Comprehensive responses|Limited responses|AO1 and AO2|AO3|What candidates did well|What candidates needed to improve)\s*:?$')


def clean(lines):
    out = [l.rstrip() for l in lines if not FOOTER.match(l.strip())]
    text = '\n'.join(out)
    # join wrapped lines into paragraphs; keep bullets and blank-line breaks
    paras, cur = [], ''
    for l in text.split('\n'):
        s = l.strip()
        if not s:
            continue
        if SUBHEAD.match(s):
            # June 2026+ reports group bullets under sub-headings; keep each heading on its own line
            if cur:
                paras.append(cur)
            paras.append(s.rstrip(':') + ':')
            cur = ''
            continue
        if s.startswith('•') and cur:
            paras.append(cur)
            cur = s
        else:
            cur = f'{cur} {s}' if cur else s
    if cur:
        paras.append(cur)
    return '\n'.join(paras).strip()


result = {}
for pdf in sorted(er_dir.glob('9708 Economics * Examiner Report.pdf')):
    m = re.match(r'9708 Economics (\w+) (\d{4}) Examiner Report\.pdf', pdf.name)
    series, year = m.group(1), int(m.group(2))
    with pdfplumber.open(pdf) as doc:
        lines = []
        for page in doc.pages:
            lines += (page.extract_text() or '').split('\n')
    # split into component sections
    starts = [(i, re.match(r'^\s*Paper 9708/(\d\d)\s*$', l).group(1)) for i, l in enumerate(lines)
              if re.match(r'^\s*Paper 9708/(\d\d)\s*$', l)]
    for k, (i, comp) in enumerate(starts):
        if not comp.startswith('2'):
            continue
        sec = lines[i + 1: starts[k + 1][0] if k + 1 < len(starts) else len(lines)]
        joined = '\n'.join(sec).replace('', '•')
        joined = re.sub(r'Comments on (individual|specific) questions', 'Comments on individual questions', joined)

        def between(a, b):
            ia = joined.find(a)
            if ia < 0:
                return ''
            ib = joined.find(b, ia + len(a)) if b else -1
            return joined[ia + len(a): ib if ib > 0 else None]

        # June 2026+ reports have no 'General comments' section: key messages run up to the question comments
        key_end = 'General comments' if 'General comments' in joined else 'Comments on individual questions'
        key = clean(between('Key messages', key_end).split('\n'))
        general = clean(between('General comments', 'Comments on individual questions').split('\n'))
        body = between('Comments on individual questions', None).split('\n')
        parts, qnum, cur, buf = {}, None, None, []

        shared = []  # parts covered by one combined comment, e.g. '(a) and (b) ...'

        def flush():
            if cur and buf:
                for c in [cur] + shared:
                    assert c not in parts, f'{series} {year} {comp}: duplicate {c}'
                    parts[c] = clean(buf)

        for l in body:
            s = l.strip()
            mq = re.match(r'^Question\s*(\d)?\s*(?:[:–-].*)?$', s)  # also 'Question 1: Compulsory Data Response' (w21/21)
            if mq:
                flush()
                shared[:] = []
                # one report prints a bare "Question" heading: treat it as the next number
                qnum = mq.group(1) or str(int(qnum or 0) + 1)
                cur, buf = None, []
                continue
            if re.match(r'^(Section [ABC]|Essays|Data [Rr]esponse)\s*$', s):
                continue
            # a part marker is followed by a space and a capital; '(b), little ...' is a wrapped sentence
            mp = re.match(r'^\(([a-f])\)\s+(?:\((i{1,3}|iv|I{1,3}|IV)\)\s+)?([A-Z0-9‘\'"].*)$', s)
            msub = re.match(r'^\((i{1,3}|iv)\)\s+([A-Z‘\'"].*)$', s)
            mboth = re.match(r'^\(([a-f])\) and \(([a-f])\)\s+([A-Z].*)$', s)
            if mboth and qnum:
                flush()
                cur, letter, buf = f'{qnum}({mboth.group(1)})', mboth.group(1), [mboth.group(3)]
                shared[:] = [f'{qnum}({mboth.group(2)})']
                continue
            if mp and qnum:
                flush()
                shared[:] = []
                cur = f'{qnum}({mp.group(1)})' + (f'({mp.group(2).lower()})' if mp.group(2) else '')
                letter = mp.group(1)
                buf = [mp.group(3)]
            elif msub and qnum and cur:
                flush()
                shared[:] = []
                cur = f'{qnum}({letter})({msub.group(1)})'
                buf = [msub.group(2)]
            elif cur:
                buf.append(l)
        flush()
        result[f'{series} {year} {comp}'] = {'key_messages': key, 'general': general, 'parts': parts}

# Errors in Cambridge's published reports, corrected by hand.
# June 2026 9708/21 Q2(b): the 'Limited responses' bullets are a copy of Q2(a)'s (public goods / health care),
# not about taxing demerit goods. Keep only the Q2(b) 'Comprehensive responses' and say why.
_k = 'June 2026 21'
if _k in result and '2(b)' in result[_k]['parts']:
    a, b = result[_k]['parts']['2(a)'], result[_k]['parts']['2(b)']
    lim_a, lim_b = a.split('Limited responses:')[-1], b.split('Limited responses:')[-1]
    if 'Limited responses:' in b and lim_a == lim_b:
        result[_k]['parts']['2(b)'] = (b.split('Limited responses:')[0].rstrip() +
                                       '\n[The published report repeats the Question 2(a) "Limited responses" bullets here, so they are left out.]')

# June 2022 9708/21: the report labels Question 3's second part '(c)' ('In the second part of the question…'); it is 3(b).
_k = 'June 2022 21'
if _k in result and '3(c)' in result[_k]['parts'] and '3(b)' not in result[_k]['parts']:
    result[_k]['parts'] = {('3(b)' if p == '3(c)' else p): t for p, t in result[_k]['parts'].items()}

# Any other repeated 'Limited responses' block is reported so it can be checked by hand.
for k, v in result.items():
    seen = {}
    for p, t in v['parts'].items():
        if 'Limited responses:' in t:
            lim = t.split('Limited responses:')[-1]
            if lim in seen:
                print(f'WARNING {k}: {p} repeats the Limited responses of {seen[lim]}')
            seen[lim] = p

out_path.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding='utf-8')
for k, v in result.items():
    print(k, '| key', len(v['key_messages']), '| general', len(v['general']), '| parts', list(v['parts']))
