"""Make the review workbook (9708_AS_past_papers_review.xlsx) from the master JSON.

Usage: python3 -I workbook.py <master_json> <out_xlsx>
"""
import json
import random
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

master_path, out_path = Path(sys.argv[1]), Path(sys.argv[2])
master = json.loads(master_path.read_text(encoding='utf-8'))
records = master['questions']
TOPIC_NAMES = master['topics']
BATCH_LOG = master['batches']

# ---------------------------------------------------------------- workbook
NAVY = '1F3864'
F = 'Arial'
hdr_font = Font(name=F, bold=True, color='FFFFFF', size=10)
hdr_fill = PatternFill('solid', fgColor=NAVY)
body = Font(name=F, size=10)
bold = Font(name=F, size=10, bold=True)
title_font = Font(name=F, size=14, bold=True, color=NAVY)
input_fill = PatternFill('solid', fgColor='FFF2CC')
flag_fill = PatternFill('solid', fgColor='FCE4D6')
thin = Side(style='thin', color='BFBFBF')
box = Border(left=thin, right=thin, top=thin, bottom=thin)
wrap_top = Alignment(wrap_text=True, vertical='top')
top = Alignment(vertical='top')


def header(ws, row, cols):
    for c, (name, width) in enumerate(cols, 1):
        cell = ws.cell(row=row, column=c, value=name)
        cell.font, cell.fill, cell.border = hdr_font, hdr_fill, box
        cell.alignment = Alignment(wrap_text=True, vertical='center')
        ws.column_dimensions[get_column_letter(c)].width = width
    ws.row_dimensions[row].height = 30


wb = Workbook()

# --- Questions
ws = wb.active
ws.title = 'Questions'
cols = [('ID', 18), ('Year', 7), ('Series', 9), ('Paper', 9), ('Section', 8), ('Q', 5), ('Part', 5), ('Choice', 13),
        ('Marks', 7), ('AO3 marks', 7), ('Command word', 11), ('2nd command', 10), ('Diagram', 8), ('Calc', 6),
        ('Stem patterns', 24), ('Primary topic', 9), ('Primary topic name', 26), ('All topics', 16), ('Sub-topics', 18),
        ('Key concepts', 32), ('Context (data response)', 26), ('Question', 60), ('Mark scheme', 70),
        ('MS page', 7), ('QP page', 7), ('Question text from', 12), ('Flags', 40), ('Reviewed?', 10), ('Reviewer notes', 30), ('Similar question in another paper', 34), ('Examiner report comment', 70)]
header(ws, 1, cols)
for i, r in enumerate(records, 2):
    vals = [r['id'], r['year'], r['series'], r['component'], r['section'], r['question'], r['part'] + (f"({r['subpart']})" if r['subpart'] else ''), r['choice'],
            r['marks'], r['ao3_marks'], r['command_word'], r['command_word_2'], 'Yes' if r['diagram'] else '',
            'Yes' if r['calculation'] else '', '; '.join(r['stem_patterns']), r['primary_topic'],
            TOPIC_NAMES[r['primary_topic']], ';' + ';'.join(r['topics']) + ';', ', '.join(r['subtopics']),
            ', '.join(r['key_concepts']), r['context'], r['question_text'], r['mark_scheme'],
            r['source']['mark_scheme_page'], r['source']['question_paper_page'], r['source']['question_text_from'],
            ' | '.join(r['flags']), 'Correct' if r['review_status'].startswith('sample') else '', 'Checked in pilot sample' if r['review_status'].startswith('sample') else '',
            ', '.join(f"{x['id']} ({x['similarity']:.0%})" for x in r['similar_to']), r['examiner_comment'] or '']
    for c, v in enumerate(vals, 1):
        cell = ws.cell(row=i, column=c, value=v)
        cell.font, cell.border = body, box
        cell.alignment = wrap_top if c in (15, 20, 21, 22, 27, 30, 31) else top
    if r['flags']:
        ws.cell(row=i, column=27).fill = flag_fill
    for c in (28, 29):
        ws.cell(row=i, column=c).fill = input_fill
    ws.row_dimensions[i].height = 60
last_q = len(records) + 1
ws.freeze_panes = 'B2'
ws.auto_filter.ref = f'A1:{get_column_letter(len(cols))}{last_q}'
dv = DataValidation(type='list', formula1='"Correct,Fix needed"', allow_blank=True)
ws.add_data_validation(dv)
dv.add(f'AB2:AB{last_q}')

# --- Topic matrix (formulas over Questions)
tm = wb.create_sheet('Topic Matrix')
tm['A1'] = 'How often each AS topic appears (count of question parts tagged with it)'
tm['A1'].font = title_font
tm['A2'] = 'Columns read variant/series/year, e.g. 23/O/N/25 = 9708/23 Oct/Nov 2025. Counts any tag (primary or secondary). "Marks as primary" sums marks where the topic is the main focus. Updates automatically as rows are added to Questions.'
tm['A2'].font = Font(name=F, size=9, italic=True)
papers = []
for r in records:
    k = (r['year'], r['series'], r['component'], r['paper_ref'])
    if k not in papers:
        papers.append(k)
mcols = [('Code', 7), ('Topic', 40)] + [(ref.replace('9708/', ''), 10) for _, _, _, ref in papers] + [('Total parts', 10), ('As primary', 10), ('Marks as primary', 11)]
header(tm, 4, mcols)
QS = "Questions"
for j, code in enumerate(TOPIC_NAMES, 5):
    tm.cell(row=j, column=1, value=code)
    tm.cell(row=j, column=2, value=TOPIC_NAMES[code])
    for k, (y, ser, comp, _) in enumerate(papers, 3):
        tm.cell(row=j, column=k, value=f'=COUNTIFS({QS}!$R$2:$R$1000,"*;"&$A{j}&";*",{QS}!$B$2:$B$1000,{y},{QS}!$C$2:$C$1000,"{ser}",{QS}!$D$2:$D$1000,"{comp}")')
    tc = 3 + len(papers)
    first, lastc = get_column_letter(3), get_column_letter(tc - 1)
    tm.cell(row=j, column=tc, value=f'=SUM({first}{j}:{lastc}{j})')
    tm.cell(row=j, column=tc + 1, value=f'=COUNTIF({QS}!$P$2:$P$1000,$A{j})')
    tm.cell(row=j, column=tc + 2, value=f'=SUMIF({QS}!$P$2:$P$1000,$A{j},{QS}!$I$2:$I$1000)')
    for c in range(1, tc + 3):
        cell = tm.cell(row=j, column=c)
        cell.font, cell.border = body, box
        if c >= 3:
            cell.alignment = Alignment(horizontal='center')
last_t = 4 + len(TOPIC_NAMES)
tot = last_t + 1
tm.cell(row=tot, column=2, value='Total').font = bold
for c in range(3, 3 + len(papers) + 3):
    L = get_column_letter(c)
    cell = tm.cell(row=tot, column=c, value=f'=SUM({L}5:{L}{last_t})')
    cell.font, cell.alignment = bold, Alignment(horizontal='center')
tm.cell(row=tot + 2, column=1, value='Check: "Marks as primary" total should be 100 per 2023+ paper (Q1 = 20 plus four 20-mark optional essays, all stored) and 80 per 2022 paper (Q1 plus three optional essays).').font = Font(name=F, size=9, italic=True)
tm.cell(row=tot + 3, column=2, value='Expected marks total').font = body
tm.cell(row=tot + 3, column=3 + len(papers) + 2, value=sum(80 if y <= 2022 else 100 for y, _, _, _ in papers)).font = body
tm.cell(row=tot + 4, column=2, value='Matches?').font = bold
mc = get_column_letter(3 + len(papers) + 2)
tm.cell(row=tot + 4, column=3 + len(papers) + 2, value=f'=IF({mc}{tot}={mc}{tot + 3},"OK","CHECK")').font = bold
tm.freeze_panes = 'C5'
for k in range(3, 3 + len(papers)):
    tm.column_dimensions[get_column_letter(k)].width = 9
tm.row_dimensions[4].height = 30
from openpyxl.formatting.rule import ColorScaleRule  # noqa: E402
tm.conditional_formatting.add(f'C5:{get_column_letter(2 + len(papers))}{last_t}',
                              ColorScaleRule(start_type='num', start_value=0, start_color='FFFFFF', end_type='num', end_value=3, end_color='8EA9DB'))
tm.conditional_formatting.add(f'{get_column_letter(3 + len(papers))}5:{get_column_letter(3 + len(papers))}{last_t}',
                              ColorScaleRule(start_type='num', start_value=0, start_color='F8CBAD', end_type='num', end_value=4, end_color='A9D08E'))

# --- Review sample
rv = wb.create_sheet('Review Sample')
rv['A1'] = 'Spot-check sample for batches 2–11 (one part per paper, data response or essay; choice fixed per paper)'
rv['A1'].font = title_font
rv['A2'] = ('How to use: open the source PDF at the page shown, then fill the yellow cells with Correct or Fix needed. '
            'If a fix is needed, write the correction in Notes (e.g. "Primary topic should be 2.3"). '
            'Errors here tell us whether the tagging approach needs adjusting before scaling up.')
rv['A2'].font = Font(name=F, size=9, italic=True)
rv['A2'].alignment = Alignment(wrap_text=True)
rv.merge_cells('A2:J2')
rv.row_dimensions[2].height = 40
random.seed(9708)
# stratified over the newest batch: one Section A part + one essay part per paper
PENDING = [b['id'] for b in BATCH_LOG if b['id'] != 'pilot-2026-10-08']
sample = []
for ref in [p[3] for p in papers]:
    group = [r for r in records if r['paper_ref'] == ref and r['batch'] in PENDING]
    if not group:
        continue
    rng = random.Random(ref)  # per-paper seed: samples stay put when new papers are added
    want_a = rng.random() < 0.5  # data-response or essay part, decided by this paper alone
    sample.append(rng.choice([r for r in group if (r['section'] == 'A') == want_a]))

rcols = [('ID', 18), ('Question', 55), ('Topics', 14), ('Command', 10), ('MS page', 8),
         ('Topics right?', 12), ('Command right?', 12), ('Mark scheme complete?', 13), ('Question text exact?', 13), ('Notes', 35)]
header(rv, 4, rcols)
for i, r in enumerate(sample, 5):
    vals = [r['id'], r['question_text'], ', '.join(r['topics']), r['command_word'], r['source']['mark_scheme_page']]
    for c, v in enumerate(vals, 1):
        cell = rv.cell(row=i, column=c, value=v)
        cell.font, cell.border, cell.alignment = body, box, wrap_top
    for c in range(6, 11):
        cell = rv.cell(row=i, column=c)
        cell.fill, cell.border, cell.font = input_fill, box, body
    rv.row_dimensions[i].height = 55
dv2 = DataValidation(type='list', formula1='"Correct,Fix needed"', allow_blank=True)
rv.add_data_validation(dv2)
dv2.add(f'F5:I{4 + len(sample)}')

# --- Schema
sc = wb.create_sheet('Schema & Notes')
sc['A1'] = '9708 AS past paper database — schema (v1) and batch log'
sc['A1'].font = title_font
rows = [
    ('Unit of record', 'One row per question part (e.g. 9708/21 June 2026 Q2(b)); sub-parts such as 1(a)(i) get their own row (ID ends Q1ai). Section B/C rows carry "Either 2 or 3" etc.'),
    ('ID format', '9708_<series><yy>_<variant>_Q<number><part>, e.g. 9708_s26_22_Q1a. s = May/June, w = Oct/Nov, m = Feb/March. Paper ref 9708/23/O/N/25 matches the code printed on the paper.'),
    ('Topics', 'Syllabus codes from the 2026–28 syllabus (AS 1.1–6.5). First code = primary focus; others = secondary. Stored as ;4.6;5.3; so filters cannot confuse 1.6 with 11.6 later.'),
    ('Sub-topics', 'Finer syllabus points (e.g. 4.6.3 nominal vs real data) — useful for precise test building.'),
    ('Command words', 'From the syllabus command-word list. "2nd command" is the evaluative tail of 8-mark and 4-mark questions ("...and consider").'),
    ('AO3 marks', 'Evaluation marks available: 0 (2-mark), 1 (4-mark), 2 (6-mark and 8-mark), 4 (12-mark). 1-mark sub-parts have 0. Checked against all 2023–26 mark schemes: one exception, 9708/23 Oct/Nov 2023 Q1(c) (4 marks, 2 for evaluation). 2022 parts: read from each mark scheme.'),
    ('Similar question', 'Pairs of question parts in different papers that share their main topic and a syllabus sub-topic, and have similar wording (text similarity ≥ 55%). Wording alone over-matches because many stems share "Assess whether … always …". See the Repeated Questions tab.'),
    ('Examiner comment', 'From the Principal Examiner Report for Teachers: what candidates did well and badly on that part. Paper-level key messages are on the Examiner Key Messages tab. Only papers whose report has been uploaded have comments.'),
    ('Flags', 'Section A parts are flagged automatically when Cambridge has removed source material for copyright: (1) part needs a removed table/figure, (2) part quotes removed text, (3) source partly removed but part answerable from general knowledge.'),
    ('Stem patterns', 'Recurring question shapes detected from wording: absolute claim (always/only/alone), compare two options, benefits vs costs, to what extent, diagram required, uses data.'),
    ('Mark scheme', 'Question-specific content only. The generic level descriptors (Table A AO1/AO2, Table B AO3) are the same for every 12-mark question and are stored once, not per row.'),
    ('Master file', '9708_AS_past_papers.json is the master. This workbook is a view of it for reviewing and filtering.'),
    ('', ''),
    ('Batch log', ''),
    ('pilot-2026-10-08', '9708/21 May/June 2025; 9708/21 and 9708/22 May/June 2026. 39 question parts. Sample of 6 checked by James: all correct.'),
    ('batch2-2026-10-08', '9708/23 and 9708/24 May/June 2025; 9708/23 and 9708/24 Oct/Nov 2025; 9708/23 and 9708/24 May/June 2026. 78 question parts.'),
    ('batch3-2026-10-08', '9708/21 and 9708/22 Oct/Nov 2025. 27 question parts. First paper with sub-parts: 9708/22 Q1(a)(i) and (ii), 1 mark each.'),
    ('batch4-2026-10-08', '9708/22 May/June 2025; 9708/21, 22, 23 Oct/Nov 2024; 9708/22 Feb/March 2024. 66 question parts. First examiner reports (Oct/Nov 2024, Feb/March 2024): comments linked to every part of the four papers they cover.'),
    ('batch5-2026-10-08', '9708/21, 22, 23 May/June 2024 + June 2024 examiner report. 40 question parts. 9708/23 has only four data-response parts (1(b) split into (i) and (ii)).'),
    ('batch6-2026-10-08', 'Examiner reports only: May/June 2025, Oct/Nov 2025, May/June 2026 (all 12 papers). Every part in the database now has an examiner comment. From June 2026 the reports list "Comprehensive responses" and "Limited responses" and have no General comments section.'),
    ('batch7-2026-10-08', '9708/22 Feb/March 2023; 9708/21, 22, 23 May/June 2023; 9708/21, 22, 23 Oct/Nov 2023. 92 question parts. 9708/23 May/June 2023 is the only paper with a 1(f): six data-response parts (four 2-mark, two 6-mark).'),
    ('batch8-2026-10-08', 'Examiner reports only: Feb/March, May/June and Oct/Nov 2023 (all 7 papers). Every part in the database now has an examiner comment. The 2022 reports were parsed too and kept aside (er_2022_pending.json in the Project) until the 2022 papers are added.'),
    ('batch9-2026-10-08', '9708/22 Feb/March 2022; 9708/21, 22, 23 May/June 2022; 9708/21, 22, 23 Oct/Nov 2022 + their examiner reports. 82 question parts. 2020–22 syllabus: Section B = one essay from Q2–Q4 (no micro/macro split), so each paper stores 80 marks; mark schemes are point-based with a Guidance column, so evaluation marks were read from each mark scheme (8-mark parts have none). Topics use the current codes.'),
    ('batch10-2026-10-08', '9708/22 Feb/March 2021; 9708/21, 22, 23 May/June 2021; 9708/21, 22, 23 Oct/Nov 2021. 82 question parts, same 2020–22 syllabus rules as 2022 (80 marks per paper, evaluation marks read from each mark scheme). Examiner reports added in batch11.'),
    ('batch11-2026-10-08', 'Examiner reports only: Feb/March and Oct/Nov 2021 (4 papers, 47 parts). The May/June 2021 report has not been uploaded, so 9708/21–23 May/June 2021 have no comments. Parser fix: headings like "Question 1: Compulsory Data Response" and a stray "Essays" line, which also cleaned the end of two 2022 comments (May/June and Oct/Nov 2022 9708/21 Q1(e)).'),
    ('', ''),
    ('Known issues', ''),
    ('Redacted source material', 'Ten of 40 public question papers have part of the Section A article and/or tables removed for copyright. Exam-day originals would restore them.'),
    ('2026 9708/22 Q1(a)', 'The ± symbols in the mark scheme tolerance did not extract; shown as "(.0.2)". Check the PDF.'),
    ('2026 9708/21 Q2(b) report', 'The published examiner report repeats the Q2(a) "Limited responses" bullets under Q2(b); they are left out and a note says so.'),
    ('Charts without values', '9708/23 May/June 2023 Q1(a) and 9708/23 Oct/Nov 2023 Q1(b) need Fig. 1.1, a chart with no printed values. Flagged "Chart needed"; use the original paper.'),
    ('2023 mark scheme errors', '9708/23 May/June 2023: the mark scheme labels Q1(b) as 1(b)(i) (there is no (ii)); the question paper label is used. 9708/23 Oct/Nov 2023 Q1(c) gives 2 of its 4 marks for the judgement, so AO3 = 2, not the usual 1.'),
    ('2022 (old syllabus) parts', 'Functions of money (9708/22 Feb/March 2022 Q1(d)(i)–(ii), 9708/22 Oct/Nov 2022 Q2(a)) is no longer AS content: flagged. Charts with no printed values: 9708/22 May/June 2022 Q1(a)(i)–(iii), 9708/23 May/June 2022 Q1(a) and Q1(b)(i), 9708/23 May/June 2021 Q1(a)(i)–(ii), 9708/23 Oct/Nov 2021 Q1(a) and Q1(b)(ii). Functions of money also in 9708/21 Oct/Nov 2021 Q1(c). 2022 mark schemes split each part into Answer and Guidance columns; Guidance is kept after the answer.'),
    ('Data-only parts', 'A few 2-mark data parts (e.g. "compare the change in population") test data handling more than a syllabus topic; tagged to the nearest topic with the concept "data interpretation".'),
]
for i, (a, b) in enumerate(rows, 3):
    sc.cell(row=i, column=1, value=a).font = bold
    c = sc.cell(row=i, column=2, value=b)
    c.font, c.alignment = body, Alignment(wrap_text=True, vertical='top')
sc.column_dimensions['A'].width = 22
sc.column_dimensions['B'].width = 110

# --- Generic level descriptors stored once
gl = wb.create_sheet('Level Descriptors')
gl['A1'] = 'Generic level descriptors for 12-mark essays (Paper 2, parts 2(b)–5(b))'
gl['A1'].font = title_font
gl['A3'] = 'Table A: AO1 Knowledge and understanding and AO2 Analysis (8 marks) — Level 3: 6–8, Level 2: 3–5, Level 1: 1–2, 0: no creditable response.'
gl['A4'] = 'Table B: AO3 Evaluation (4 marks) — Level 2: 3–4 (justified conclusion, developed evaluation), Level 1: 1–2 (vague conclusion, simple evaluative comment), 0: no creditable response.'
gl['A5'] = 'Full wording: see any 9708/2x mark scheme (generic marking pages before the questions).'
for c in ('A3', 'A4', 'A5'):
    gl[c].font, gl[c].alignment = body, Alignment(wrap_text=True)
gl.column_dimensions['A'].width = 120

rq = wb.create_sheet('Repeated Questions', 2)
rq['A1'] = 'Questions that recur across papers (same main topic and sub-topic, similar wording)'
rq['A1'].font = title_font
rq['A2'] = 'Useful for spotting favourite questions — and for avoiding giving students the same question twice in a test.'
rq['A2'].font = Font(name=F, size=9, italic=True)
header(rq, 4, [('Similarity', 10), ('Marks A / B', 9), ('Question A', 18), ('Wording A', 60), ('Question B', 18), ('Wording B', 60)])
byid = {r['id']: r for r in records}
pairs = sorted({(x['similarity'], *sorted((r['id'], x['id']))) for r in records for x in r['similar_to']}, reverse=True)
for i, (sim, a, b) in enumerate(pairs, 5):
    vals = [sim, f"{byid[a]['marks']} / {byid[b]['marks']}", a, byid[a]['question_text'], b, byid[b]['question_text']]
    for c, v in enumerate(vals, 1):
        cell = rq.cell(row=i, column=c, value=v)
        cell.font, cell.border, cell.alignment = body, box, wrap_top
    rq.cell(row=i, column=1).number_format = '0%'
    rq.row_dimensions[i].height = 48
if not pairs:
    rq['A5'] = 'None found yet.'

ek = wb.create_sheet('Examiner Key Messages', 3)
ek['A1'] = 'Examiner report key messages (per paper)'
ek['A1'].font = title_font
header(ek, 3, [('Paper', 16), ('Key messages', 90), ('General comments', 70)])
for i, (ref, v) in enumerate(sorted(master['examiner_reports'].items()), 4):
    for c, val in enumerate([ref, v['key_messages'], v['general']], 1):
        cell = ek.cell(row=i, column=c, value=val)
        cell.font, cell.border, cell.alignment = body, box, wrap_top
    ek.row_dimensions[i].height = 260

for s in wb.worksheets:
    s.sheet_view.showGridLines = s.title in ('Questions',)

wb.save(out_path)
print('workbook', out_path, 'records', len(records), 'sample', len(sample))
