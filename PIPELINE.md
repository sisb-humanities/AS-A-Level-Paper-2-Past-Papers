# 9708 AS past paper database — how each batch is processed

Master data: `claude/9708_AS_past_papers.json` (schema v1). Always merge new batches into this file; never start a fresh one.
Front end: "Econ Past Paper Tracker" artifact — https://claude.ai/artifact/5urMyj4G4Jt5bkJxopEapJ (republish to this URL after each batch; capabilities `downloads` + `sample`, carried forward automatically).
Scripts: `claude/pipeline/` — extract.py, er_parse.py, add_er.py (reports-only batches), tags.py (pilot tags + topic names), tags2.py (2024–26 tags), tags3.py (2023 tags), tags4.py (2022 tags + OFF_SYLLABUS flags), tags5.py (2021 tags + OFF_SYLLABUS5), build.py (master JSON), merge_master.py (add a partial build to the master), workbook.py (review workbook from the master), build_page.py + tracker.template.html + levels.json (front end).

## Rebuilding in a new session
1. Download `claude/pipeline/*` and `claude/9708_AS_past_papers.json` from the Project into the workspace; put the scripts in a scratch dir.
2. Choose the route:
   - **New papers, old PDFs not available (normal case)** — partial build + merge:
     1. Put only the new PDFs through steps 3–4 below in their own folder (`new/txt`, `new/raw.json`).
     2. In `new/` put the tag file for the new papers (e.g. tags4.py → add its import to build.py like T3) and stubs: `tags.py` with TOPIC_NAMES / UNIT_NAMES copied from the master and `T = {}`, and `tags2.py` with `T2 = {}`.
     3. Add BATCH_OF / BATCH_LOG entries in build.py, then `python3 -I build.py new new/txt new/out` (output holds only the new papers).
     4. `python3 -I merge_master.py 9708_AS_past_papers.json new/out/9708_AS_past_papers.json out/9708_AS_past_papers.json` — refuses papers already in the master, re-runs repeat detection over everything and asserts that existing repeat links are unchanged.
   - **Examiner reports only** → `python3 -I er_parse.py er er.json` then `python3 -I add_er.py 9708_AS_past_papers.json er.json <batch-id> out/9708_AS_past_papers.json` (asserts the report's parts match the database exactly).
   - **Full rebuild** (all PDFs re-uploaded): steps 3–4 for every paper, real tags.py/tags2.py/tags3.py in the scratch dir, `python3 -I build.py <scratch> txt out`.
3. `pdftotext -layout` each PDF into `txt/`; examiner report PDFs go in `er/`. Uploads arrive as `<id>-9708_Economics_..._Question_paper__21.pdf`: strip the id prefix, turn underscores into spaces, "Question paper" → "Question Paper".
4. `python3 -I extract.py txt raw.json pdf` (the PDF folder is needed for table-layout mark schemes) (→ `python3 -I er_parse.py er er.json` if there are reports) → tags for the new parts.
5. `python3 -I workbook.py out/9708_AS_past_papers.json out/9708_AS_past_papers_review.xlsx`, then recalculate in LibreOffice (`soffice --headless --calc --convert-to xlsx --outdir recalc <file>`) and check Topic Matrix "Matches?" = OK.
6. `python3 -I build_page.py out/9708_AS_past_papers.json tracker.template.html out/econ-past-paper-tracker.html levels.json`, test it in headless Chromium, then publish to the artifact URL above.

## Per batch
1. Upload question paper + mark scheme for each variant, plus the series examiner report if available. Names as Cambridge/the school names them: `9708 Economics <June|November|March> <yyyy> <Mark Scheme|Question Paper>  <variant>.pdf` and `9708 Economics <Series> <yyyy> Examiner Report.pdf`. Papers are detected from these filenames.
2. Papers: extract with `pdftotext -layout`; split mark schemes on question-part rows (`1(a)`…`5(b)`, parts up to (f), including sub-parts like `1(a)(i)`, `1(b)(ii)`); drop page headers/footers (© Cambridge University Press / © UCLES, "PUBLISHED [year]") and the marker instruction "Please use a text box to show the mark split". Question numbers in the QP may be indented up to 4 spaces. Question wording comes from the question paper, including essay preambles printed before (a). If the MS repeats the question line after a preamble, it is stripped from the MS body. 2022 mark schemes are 4-column tables (Question | Answer | Marks | Guidance): pdftotext interleaves the Guidance column, so extract.py detects 'Marks  Guidance' in the header and reads the cells with pdfplumber; the repeated question is stripped by fuzzy match against the QP (MS wording differs slightly), and Guidance is appended as 'Guidance: …'. QP parser guards (batch10): a line starting with a digit is only a new question if it is the next number and the current question already has a part (chart axis labels like '4   250' inside the Section A source were read as Question 4); if a sub-part (i) ends without a mark before (ii) starts, (i)/(ii) are an inline list inside one part (s21/23 2(a), 3(a); m21 2(a); w21/23 3(a)) and the whole text is stored under the bare part. A stem printed between (d) and (i) ('Explain how … as', 'Using Fig. 1.1') is prefixed to each sub-part's question, and the bare 1(d) stem row is dropped. A mark scheme sub-part "(i)" with no "(ii)" is renamed to the question paper's bare label (s23/23 prints 1(b) as 1(b)(i)).
3. Examiner reports: extract with pdfplumber (pdftotext breaks "fi/ff" ligatures). Split by "Paper 9708/2x"; take Key messages, General comments, then per-part comments under "Comments on individual/specific questions". Handles: bare "Question" heading (= next number); 'Question 1: Compulsory Data Response' headings and stray 'Essays' / 'Data response' lines (w21/21; the fix also removed a trailing 'Essays' from s22/21 and w22/21 Q1(e)); combined "(a) and (b)" comments (copied to both parts); wrapped lines starting "(b), …" (part markers must be followed by a capital or a digit, e.g. "(a) 2-mark questions…"); mistyped "(a) (I)" sub-part (lower-cased); footer variants. Duplicate parts raise an error.
   - June 2026 format (expect it for later series): no "General comments" section, so key messages end at the question comments; key messages split into "What candidates did well" / "What candidates needed to improve"; each part split into "Comprehensive responses" / "Limited responses" (essays also "AO1 and AO2" / "AO3"). These sub-headings are kept as their own lines ending in ":".
   - Hand fix in er_parse.py: s22/21 — the report labels Q3's second part "(c)"; renamed 3(b).
   - Hand fix in er_parse.py: s26/21 Q2(b) — Cambridge's report repeats the Q2(a) "Limited responses" bullets; they are dropped with a note. The parser warns if any other part repeats another part's Limited responses.
4. Tag each part (2022: use current 2023+ topic codes; flag content no longer on the AS syllabus via OFF_SYLLABUS, e.g. functions of money): syllabus topics (2026–28 codes; first = primary), sub-topics, command word + "consider" tail, key concepts, data-response context. AO3 marks by rule: 1→0, 2→0, 4→1, 6→2, 8→2, 12→4, checked against all 26 mark schemes; one exception set in build.py AO3_OVERRIDE: w23/23 Q1(c) (4 marks, 2 for the judgement). 2022 mark schemes have no AO labels: each part's evaluation marks are read from its mark scheme and stored in tags4 ('ao3'); 8-mark (a) essay parts have 0, 12-mark (b) parts 4, Section A 'Discuss/Consider' parts 1–3. Q1 part order and count vary (w24/22 has the 4-marker at 1(b); s24/23 has only 1(a)–(d) with 1(b)(i)/(ii); s23/23 has 1(a)–(f): four 2-markers and two 6-markers; w23/21 and w23/23 put the 4-marker at 1(b)/1(c)).
5. Automatic flags on Section A: needs removed table/figure; quotes removed text; source partly removed but answerable. Hand flags in build.py: s25/24 Q1(d) (needs removed data); EXTRA_FLAGS "Chart needed" for charts with no printed values (s23/23 Q1(a), w23/23 Q1(b), s22/23 Q1(a), Q1(b)(i)); NOT_REMOVED replaces the automatic 'needs removed data' flag where the referenced table/figure is actually printed (s22/22 Q1(a)(i)–(iii) chart, Q1(c) table) — these stay usable in tests/practice but the teacher needs the original paper.
6. Repeats: different papers, same primary topic, shared sub-topic, wording similarity ≥ 0.55.
7. Checks before merging: marks per paper = 100; every part has MS and QP pages; QP vs MS wording compared (low similarity = essay preamble or small MS rewording; QP wording is used); examiner comments per paper = parts; no changes to existing records except `similar_to`.
8. Review sample: one part per paper in unreviewed batches; the paper's own seed decides which part, so the sample does not change when other papers are added (tested: the 16 earlier picks are unchanged).

## Front end (tracker.template.html)
- Section filter works on a derived `area` (data / micro / macro) from build_page.py: 2023+ from the section (B = micro, C = macro — true for every 2023–26 essay), 2022 essays from the primary topic unit (1–3 micro, 4–6 macro). 2022 cards show '2020–22 syllabus'; Table A/B descriptors and levels-based Claude marking apply only where `marking` starts with 'levels' (not 2022).
- Tabs: Browse (filters, mark scheme / examiner report / source extract / similar), Patterns (topic × paper heatmap, facts, command words, examiner themes, recurring clusters, key messages — General comments heading hidden when a report has none), Test builder (basket in localStorage, auto-fill, Word export via `downloads` + docx@8.5.0 from jsDelivr: A4, 1.5 cm margins, centred page numbers, full-width 18 cm tables), Practice (random question, Claude marking via `sample.json` against MS + Table A/B + examiner comment; self-marking fallback; history in localStorage).
- Data is embedded inline by build_page.py (about 1.7 MB for 506 parts).

## Record = one question part
ID `9708_<s|w|m><yy>_<variant>_Q<n><part><subpart>`; `paper_ref` like `9708/23/O/N/25`, `9708/22/F/M/24`; `label` like `1(b)(ii)`. `examiner_comment` per part where a report exists; paper-level key messages under `examiner_reports`. Section A stimulus under `stimuli`. `similar_to` lists recurring questions.

## Batch log
- pilot-2026-10-08: 9708/21 s25, 9708/21 s26, 9708/22 s26 — 39 parts. Sample of 6 checked by James: all correct.
- batch2: 9708/23 + 24 s25, w25, s26 — 78 parts.
- batch3: 9708/21 + 22 w25 — 27 parts.
- batch4: 9708/22 s25; 9708/21–23 w24; 9708/22 m24; reports w24 + m24 — 66 parts.
- batch5: 9708/21–23 s24; report s24 — 40 parts.
- batch6: examiner reports only — June 2025, Nov 2025, June 2026 (12 papers, 158 parts). Merged with add_er.py.
- batch7: 9708/22 m23; 9708/21–23 s23; 9708/21–23 w23 — 92 parts. Partial build + merge_master.py.
- batch8: examiner reports only — March, June, Nov 2023 (7 papers, 92 parts), via add_er.py. 2022 reports parsed in the same run and merged in batch9.
- batch9: 9708/22 m22; 9708/21–23 s22; 9708/21–23 w22 + their examiner reports — 82 parts (80 marks per paper: Q1 + three essays).
- batch10: 9708/22 m21; 9708/21–23 s21; 9708/21–23 w21 — 82 parts.
- batch11: examiner reports only — March 2021 and Nov 2021 (4 papers, 47 parts) via add_er.py; two 2022 comments re-merged after the parser fix.
- Batches 2–11: review sample of 37 awaiting James (2021 picks: m21/22 Q2a, s21/21 Q3a, s21/22 Q1a, s21/23 Q2a, w21/21 Q1c, w21/22 Q2a, w21/23 Q4a) (2022 picks: m22/22 Q1c, s22/21 Q1a, s22/22 Q3b, s22/23 Q1bii, w22/21 Q1a, w22/22 Q1b, w22/23 Q1bi); earlier 23 picks unchanged (7 new: m23/22 Q1e, s23/21 Q2b, s23/22 Q4a, s23/23 Q3a, w23/21 Q3b, w23/22 Q1b, w23/23 Q1b).
- Total: 40 papers, 506 parts; examiner comments on 471 parts (all papers except June 2021); 208 repeat pairs.

## Coverage
- Papers: 2021 (March 22; June 21–23; Nov 21–23 — 2020–22 syllabus), 2022 (March 22; June 21–23; Nov 21–23 — 2020–22 syllabus), 2023 (March 22; June 21–23; Nov 21–23), 2024 (March 22; June 21–23; Nov 21–23), 2025 (June 21–24; Nov 21–24), June 2026 (21–24). 2023 is the first year of the current syllabus structure.
- Examiner reports: all papers except June 2021 (9708/21–23) — merge with add_er.py when uploaded.
- 2022 papers (2020–22 syllabus): Q1 data response plus ONE essay chosen from Q2–Q4 (8 + 12), so a paper stores 11–12 parts and 80 marks (the workbook's marks check expects 80 for 2022, 100 for 2023+). Section is 'B' for all 2022 essays, choice 'One of 2, 3 or 4'. Reports show s22/22 Q1(a)(i)–(iii), s22/23 and w22/23 Q1(b)(i)/(ii), m22/22 Q1(d)(i)/(ii), w22/22 Q1(a)–(f).
- Next back: 2020 papers are on the same 2020–22 syllabus (same pipeline); 2019 and earlier are an older syllabus again. Never examined in 40 papers: 1.2 Economic methodology, 4.1 National income statistics.

## Known issues
- 10 of 40 public question papers have Section A material removed for copyright (m23/22, s22/22, m21/22 among the older ones); 10 parts cannot be attempted from the public copy. m21/22 Q1(a) is hand-flagged (NEEDS_REMOVED_DATA): it needs the removed Table 1.1 without naming it.
- Source extracts are plain text: charts and tables extracted from the PDF appear as stray numbers; two 2023 charts have no printed values at all ("Chart needed" flag).
- s26/22 Q1(a): ± tolerance symbols lost in extraction.
- s24/23 Q2(a): the mark scheme preamble says "the only new car production allowed … will be for electric cars"; the question paper says "most new car production … will be of electric cars". Question paper wording is used.
- 2023 mark schemes sometimes word the question slightly differently from the question paper (e.g. w23/22 Q1(d) MS says "assess" where the QP says "consider"; w23/23 Q3(b) MS says "bus and rail (mass transit)"). Question paper wording is used.
- June 2026 report comments are formulaic, so they are less informative than 2024–25 comments.
- er_parse.py changes in batch6/7 (digit after a part marker, "(I)", part (f)) have not been re-run against the 2024 reports; the duplicate-part assertion would catch a misread on the next full rebuild. extract.py's part (f) change has not been re-run on the 2024–26 papers either (none of them has an (f)).
