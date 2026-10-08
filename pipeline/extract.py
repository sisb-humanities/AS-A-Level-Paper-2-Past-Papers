"""Extract 9708 Paper 2 question parts + mark schemes from pdftotext -layout output.

Usage: python3 -I extract.py <txt_dir> <out_json>
"""
import json
import re
import sys
from pathlib import Path

txt_dir = Path(sys.argv[1])
out_path = Path(sys.argv[2])

QID = re.compile(r'^\s{0,8}([1-5]\([a-f]\)(?:\((?:i|ii|iii|iv)\))?)\s{2,}(.*)$')
NOISE = [
    re.compile(r'^\s*©\s*(Cambridge University Press|UCLES)'),
    re.compile(r'^\s*9708/2\d\s+Cambridge International AS & A Level'),
    re.compile(r'^\s*PUBLISHED(\s+\d{4})?\s*$'),
    re.compile(r'^\s*Question\s+Answer\s+Marks\s*$'),
    re.compile(r'^\s*Section [ABC]\b.*$'),
    re.compile(r'^\s*(EITHER|OR)\s*$'),
    re.compile(r'Please use a text box to show the mark split'),  # instruction to markers, not mark scheme content
    re.compile(r'^\s*Follow the point-based marking guidance at the top of this mark scheme\.\s*$'),
]
TRAIL_MARK = re.compile(r'^(.*?\S)\s{3,}(\d{1,2})\s*$')
AO_LINE = re.compile(r'^(AO[123].*?)\s{3,}(\d{1,2})\s*$')


def is_noise(line):
    return any(p.search(line) for p in NOISE)


def clean_block(lines):
    """Strip the answer-column indent, keep paragraph breaks, normalise bullets."""
    out = []
    for raw in lines:
        s = raw.rstrip()
        if not s.strip():
            out.append('')
            continue
        s = s.strip()
        m = AO_LINE.match(s)
        if m:
            s = f'{m.group(1).strip()}: {m.group(2)}'
        s = re.sub(r'^•\s+', '• ', s)
        out.append(s)
    # join wrapped lines into paragraphs; bullets start new lines
    paras, cur = [], ''
    for s in out:
        if s == '':
            if cur:
                paras.append(cur)
                cur = ''
            continue
        if s.startswith('•') or s.startswith('AO') or re.match(r'^(Level \d|Up to|Max|Reserve|Guidance|Note|Evaluation|Indicative|Responses may|Accept|A one-sided|For |Explanation of|AO\d)', s):
            if cur:
                paras.append(cur)
            cur = s
        else:
            cur = f'{cur} {s}' if cur else s
    if cur:
        paras.append(cur)
    text = '\n'.join(paras)
    text = text.replace('‑', '-')
    return text.strip()


def parse_ms(path):
    lines = path.read_text(encoding='utf-8').splitlines()
    # start at the first question row (after generic level tables)
    start = next(i for i, l in enumerate(lines) if re.match(r'^\s{0,8}1\(a\)', l))
    blocks = {}
    order = []
    cur = None
    first_line_marks = {}
    for line in lines[start:]:
        if is_noise(line):
            continue
        m = QID.match(line)
        if m:
            qid, rest = m.group(1), m.group(2)
            if qid not in blocks:
                blocks[qid] = []
                order.append(qid)
                tm = TRAIL_MARK.match(rest)
                if tm and not rest.strip().startswith('AO'):
                    rest = tm.group(1)
                    first_line_marks[qid] = int(tm.group(2))
            cur = qid
            blocks[qid].append(rest)
            continue
        if cur:
            blocks[cur].append(line)
    result = {}
    for qid in order:
        text = clean_block(blocks[qid])
        result[qid] = {'ms_raw': text, 'marks_ms': first_line_marks.get(qid)}
    return result


def lines_to_paras(lines):
    """Cell text from pdfplumber has no blank lines: start a paragraph at bullets and after '(1 mark)' style endings."""
    paras, cur = [], ''
    for l in lines:
        s = l.strip().replace('\uf0b7', '•').replace('‑', '-')
        if not s:
            continue
        s = re.sub(r'^•\s*', '• ', s)
        # after a bullet, a line starting with a capital is a new item/heading (wrapped bullet lines start lower-case)
        if s.startswith('•') or (cur.startswith('•') and s[0].isupper()) or re.match(r'^(Level \d|Up to|Max|Reserve|Note|Evaluation|Indicative|Responses may|Accept|A one-sided|For |AO\d|\d+ marks? max)', s):
            if cur:
                paras.append(cur)
            cur = s
        else:
            cur = f'{cur} {s}' if cur else s
        if re.search(r'(\((up to )?\d+ marks?\)|marks? maximum|max(imum)?\s*\d* ?marks?\.?)$', cur, re.I):
            paras.append(cur)
            cur = ''
    if cur:
        paras.append(cur)
    return paras


def parse_ms_table(pdf_path):
    """Mark schemes laid out as a 4-column table (Question, Answer, Marks, Guidance) — pdftotext interleaves the
    Guidance column with the answer, so read the table cells with pdfplumber. Rows continuing onto the next page
    have an empty Question cell."""
    import pdfplumber
    cells, order, cur = {}, [], None
    with pdfplumber.open(pdf_path) as doc:
        for page in doc.pages:
            for table in page.extract_tables():
                for row in table:
                    vals = [c for c in row if c not in (None, '')]
                    if not vals or vals[:2] == ['Question', 'Answer'] or 'Question' in vals and 'Answer' in vals:
                        continue
                    qid = (row[0] or '').strip()
                    if re.match(r'^[1-5]\([a-f]\)(\((i|ii|iii|iv)\))?$', qid):
                        cur = qid
                        if cur not in cells:
                            cells[cur] = {'answer': [], 'marks': None, 'guidance': []}
                            order.append(cur)
                    elif qid or cur is None:
                        continue
                    rest = [c for c in row[1:] if c not in (None, '')]
                    # remaining non-empty cells are answer, marks, guidance in that order (marks is a bare number)
                    for c in rest:
                        if re.fullmatch(r'\s*\d{1,2}\s*', c) and cells[cur]['marks'] is None:
                            cells[cur]['marks'] = int(c)
                        elif cells[cur]['marks'] is None and not cells[cur]['guidance']:
                            cells[cur]['answer'] += c.split('\n')
                        else:
                            cells[cur]['guidance'] += c.split('\n')
    out = {}
    for q in order:
        c = cells[q]
        out[q] = {'answer_lines': c['answer'], 'guidance': lines_to_paras(c['guidance']), 'marks_ms': c['marks']}
    return out


def norm_words(s):
    return re.sub(r'\W+', ' ', (s or '').replace('’', "'")).strip().lower()


def strip_question(answer_lines, question):
    """Drop the leading lines that repeat the question (fuzzy match against the question paper wording, since the
    mark scheme sometimes words it slightly differently, e.g. 'food and non-food' vs 'food and the non-food')."""
    import difflib
    best = (0.0, -1)
    # try the sub-part text without its stem first ('Using Fig. 1.1: Compare …' is printed as 'Compare …' in the MS)
    for target in dict.fromkeys([norm_words(question.split(': ', 1)[-1]), norm_words(question)]):
        acc = ''
        for i, l in enumerate(answer_lines):
            acc = f'{acc} {l}'.strip()
            n = norm_words(acc)
            if abs(len(n) - len(target)) <= 25:
                r = difflib.SequenceMatcher(None, n, target).ratio()
                if r > best[0]:
                    best = (r, i)
            if len(n) > len(target) + 40:
                break
    if best[0] >= 0.88:
        i = best[1]
        return ' '.join(answer_lines[:i + 1]).strip(), answer_lines[i + 1:]
    return '', answer_lines


def split_question_from_ms(ms_text):
    """First paragraph is the question; if it is only a quoted stem, take the next too."""
    paras = ms_text.split('\n')
    q = paras[0]
    rest = paras[1:]
    if q.rstrip().endswith('’') and rest:
        q = f'{q} {rest[0]}'
        rest = rest[1:]
    return q.strip(), '\n'.join(rest).strip()


def parse_qp(path):
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    parts = {}
    qnum = None
    cur_id, buf = None, []
    stim_lines, in_stim, stim_title = [], False, None
    pre, in_pre = [], False  # essay preamble printed before (a)
    stems = {}  # text printed after (d) but before its (i): 'Explain how … as' / 'Using Fig. 1.1' (2022 papers)
    inline = False  # (i)/(ii) are a list inside one part (only the last carries the mark), e.g. s21/23 2(a)
    for line in lines:
        if re.match(r'^\s*(EITHER|OR|Either|Or)\s*$', line) or 'Section ' in line or 'Answer one question' in line:
            continue
        if is_noise(line) or re.match(r'^\s*\d\s*$', line) or 'Turn over' in line:
            continue
        mq = re.match(r'^\s{0,4}([1-5])\s{2,}(\S.*)$', line)
        if mq and not re.match(r'^\s*\(', mq.group(2)):
            # chart axis labels ('4      250') look like question numbers: accept only the next question, and
            # only once the current one has a part (so nothing inside the Section A source can start Question 2)
            d = mq.group(1)
            nxt = (qnum is None and d == '1') or (qnum is not None and int(d) == int(qnum) + 1 and any(k.startswith(f'{qnum}(') for k in parts))
            if not nxt:
                if cur_id:
                    buf.append(line)
                elif in_stim:
                    stim_lines.append(line)
                continue
            qnum = mq.group(1)
            if qnum == '1':
                stim_title = mq.group(2).strip()
                in_stim = True
            else:
                pre, in_pre = [mq.group(2)], True
            continue
        mq2 = re.match(r'^\s{0,4}([1-5])\s{2,}\(([a-f])\)\s+(.*)$', line)
        mp = re.match(r'^\s+\(([a-f])\)\s+(?:\((i|ii|iii|iv)\)\s+)?(.*)$', line)
        msub = None if mp else re.match(r'^\s+\((i|ii|iii|iv)\)\s+(.*)$', line)
        if mq2:
            qnum = mq2.group(1)
            mp = re.match(r'^\s*\(([a-f])\)\s+(?:\((i|ii|iii|iv)\)\s+)?(.*)$', f' ({mq2.group(2)}) {mq2.group(3)}')
        if mp:
            in_stim = False
            cur_letter = mp.group(1)
            stems.pop(cur_letter, None)
            inline = False
            cur_id = f'{qnum}({cur_letter})' + (f'({mp.group(2)})' if mp.group(2) else '')
            buf = ([*pre] if in_pre and mp.group(1) == 'a' else []) + [mp.group(3)]
            pre, in_pre = [], False
        elif msub:
            sub, text = msub.group(1), msub.group(2).strip()
            if inline and cur_id:
                buf.append(f'({sub}) {text}')
            elif cur_id and cur_id not in parts and re.search(r'\)\((i|ii|iii|iv)\)$', cur_id):
                # the previous sub-part never got a mark: this is an inline list, so the part is the bare letter
                stem = stems.pop(cur_letter, '')
                prev = cur_id[cur_id.rindex('('):]
                first = buf[0][len(stem) + 2:] if stem and buf[0].startswith(stem) else buf[0]
                cur_id = cur_id[:cur_id.rindex('(')]
                buf = ([stem] if stem else []) + [f'{prev} {first.strip()}'] + buf[1:] + [f'({sub}) {text}']
                inline = True
            else:
                if cur_id and '(' not in cur_id[cur_id.index(')') + 1:] and cur_id not in parts and buf:
                    stems[cur_letter] = ' '.join(b.strip() for b in buf if b.strip()).rstrip(':,')
                cur_id = f'{qnum}({cur_letter})({sub})'
                stem = stems.get(cur_letter)
                sep = ' ' if stem and stem[-1] in '.?' else ': '
                buf = [f'{stem}{sep}{text}' if stem else text]
        elif cur_id:
            buf.append(line)
        elif in_pre:
            pre.append(line)
        elif in_stim:
            stim_lines.append(line)
        if cur_id:
            joined = ' '.join(b.strip() for b in buf if b.strip())
            mm = re.search(r'\[(\d{1,2})\]\s*$', joined)
            if mm:
                qtext = joined[:mm.start()].strip()
                parts[cur_id] = {'question': qtext.replace('‑', '-'), 'marks': int(mm.group(1))}
                cur_id, buf = None, []
    stim = '\n'.join(l.strip() for l in stim_lines).strip()
    stim = re.sub(r'\n{2,}', '\n\n', stim)
    return parts, stim_title, stim.replace('‑', '-')


pdf_dir = Path(sys.argv[3]) if len(sys.argv) > 3 else None  # needed for table-layout mark schemes
papers = []
for f in sorted(txt_dir.glob('9708 Economics * Mark Scheme  2?.txt')):
    m = re.match(r'9708 Economics (\w+) (\d{4}) Mark Scheme  (2\d)\.txt', f.name)
    series, year, var = m.group(1), int(m.group(2)), m.group(3)
    qpf = f.name.replace('Mark Scheme', 'Question Paper')
    papers.append((series, year, var, f.name, qpf if (txt_dir / qpf).exists() else None))

out = []
for series, year, var, msf, qpf in papers:
    qp, stim_title, stim = ({}, None, None)
    if qpf:
        qp, stim_title, stim = parse_qp(txt_dir / qpf)
    table_mode = re.search(r'Marks\s+Guidance', (txt_dir / msf).read_text(encoding='utf-8')) is not None
    if table_mode:
        assert pdf_dir, f'{msf}: table-layout mark scheme, pass the PDF folder as the third argument'
        tab = parse_ms_table(pdf_dir / msf.replace('.txt', '.pdf'))
        ms = {}
        for qid, d in tab.items():
            # a bare row like 1(d) that only holds the stem of 1(d)(i)/(ii): the stem is already in the sub-parts
            if qid not in qp and any(k.startswith(qid + '(') for k in tab):
                continue
            q_text, body = strip_question(d['answer_lines'], qp.get(qid, {}).get('question', ''))
            paras = lines_to_paras(body)
            if d['guidance']:
                paras += ['Guidance: ' + d['guidance'][0]] + d['guidance'][1:]
            ms[qid] = {'ms_raw': '\n'.join([q_text or (qp.get(qid, {}).get('question') or '')] + paras), 'marks_ms': d['marks_ms']}
    else:
        ms = parse_ms(txt_dir / msf)
    # Mark scheme mislabels a single part as a sub-part (s23/23 prints '1(b)(i)' with no (ii); the QP has 1(b))
    for qid in list(ms):
        bare = qid[:-len('(i)')] if qid.endswith('(i)') else None
        if bare and f'{bare}(ii)' not in ms and bare in qp and qid not in qp:
            ms = {(bare if k == qid else k): v for k, v in ms.items()}
            print(f'renamed {series} {year} {var} {qid} -> {bare} (as in the question paper)')
    for qid, d in ms.items():
        q_from_ms, ms_body = split_question_from_ms(d['ms_raw'])
        row = {
            'qid': qid,
            'question_ms': q_from_ms,
            'question_qp': qp.get(qid, {}).get('question'),
            'marks_ms': d['marks_ms'],
            'marks_qp': qp.get(qid, {}).get('marks'),
            'mark_scheme': ms_body,
        }
        out.append({'series': series, 'year': year, 'variant': var, **row,
                    'stimulus_title': stim_title if qid.startswith('1') else None,
                    'stimulus_text': stim if qid.startswith('1') else None})

out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
print(len(out), 'rows')
for r in out:
    print(r['year'], r['variant'], r['qid'], 'ms', r['marks_ms'], 'qp', r['marks_qp'], '|', (r['question_qp'] or r['question_ms'])[:70])
