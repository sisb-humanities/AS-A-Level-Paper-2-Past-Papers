# AS Level Economics Paper 2 Past Paper Tracker (9708)

A searchable database of Cambridge International AS Level Economics **Paper 2 (Data Response and Essays)** past papers, with a front end for teachers and students at SISB Nonthaburi.

**Open the tracker:** `index.html` (GitHub Pages: Settings → Pages → Deploy from a branch → `main` / root).

## What's in it

- **40 papers, 506 question parts:** March, June and November series from March 2021 to June 2026 (9708/21–24).
- Every question part is tagged with its syllabus topic and sub-topic (2026–28 codes), command word, evaluation (AO3) marks, key concepts and the data-response context.
- The full mark scheme for every part, plus the Principal Examiner's comment where a report exists (all papers except June 2021).
- Flags for parts that can't be answered from the public paper (copyright redactions, charts with no printed values) and for 2021–22 content that is no longer on the AS syllabus.

## The tracker (`index.html`)

| Tab | What it does |
| --- | --- |
| Browse questions | Filter by topic (tick whole units or single topics), year, series, paper, section (data response / micro essay / macro essay), marks, command word; open the mark scheme, examiner comment, source extract and similar questions from other papers |
| Patterns | Topic × paper heatmap, most and least examined topics, command words, what examiners keep criticising, recurring questions, examiner key messages |
| Test builder | Add whole questions or single parts, or fill a test automatically from the topics covered so far; download the paper and mark scheme as Word files (A4, 1.5 cm margins, page numbers) |
| Practice | Random question by topic; write an answer, then self-mark against the mark scheme and examiner comment. History is kept in the browser |

Marking with Claude only works in the Claude-hosted version of the page. On GitHub Pages, students mark their own answers against the mark scheme.

## Files

```
index.html                         the tracker (data embedded; works offline)
data/9708_AS_past_papers.json      master database: one record per question part
data/9708_AS_past_papers_review.xlsx   review workbook: Questions, Topic Matrix, Repeated Questions,
                                   Examiner Key Messages, Review Sample, Schema & Notes
pipeline/                          scripts that build the database and page from the PDFs
PIPELINE.md                        how each batch is processed, batch log, known issues
```

## Adding papers

See `PIPELINE.md`. In short: convert the new question papers and mark schemes to text, run `extract.py`, add tags for the new parts, run `build.py` on the new papers, then `merge_master.py`. Use `add_er.py` for examiner reports, then `workbook.py` and `build_page.py` to rebuild the outputs.

## Syllabus notes

- **2023 onwards:** Section A data response (20 marks), Section B micro essay (Q2 or Q3), Section C macro essay (Q4 or Q5). 12-mark parts are marked with the generic Level descriptors (Tables A and B).
- **2021–22 (2020–22 syllabus):** Section A data response, then one essay from Q2–Q4. Mark schemes are point-based, so evaluation marks were read from each mark scheme. These are mapped to the current topic codes and labelled "2020–22 syllabus" in the tracker.

## Copyright

Question papers, mark schemes and examiner reports © Cambridge University Press & Assessment. Compiled for internal teaching use at SISB Nonthaburi; not for redistribution.
