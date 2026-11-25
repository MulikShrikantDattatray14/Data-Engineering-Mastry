# SQL Practice Record Skills — Canonical Standard

## Source of truth

**PNP-P026.md is the canonical reference for every PNP and Bosscoder practice-question record.** Before presenting, solving, updating, or saving any question, inspect PNP-P026.md and follow its structure, depth, visual language, and quality bar. Do not make the learner repeat this instruction.

Canonical example: [PNP-P026.md](Joins/medium/PNP-P026.md).

## Required record structure

Use the same section sequence and equivalent level of completeness as PNP-P026.md. Adapt only where a section is genuinely inapplicable to the question; explain why rather than silently omitting it.

1. **Title, topic and difficulty** — source ID, concise title, topic, difficulty.
2. **Question** — original source wording, business scenario, task, source link, table-color key.
3. **Required output columns** — one row per output column, in required order; source/calculation, meaning, row-level rule, eligibility/benchmark/display rules and example.
4. **Practice example · Sample input** — each named source table separately; distinguish source-provided data from added practice data.
5. **Expected output** — exact requested columns and order.
6. **How the sample produces this output** — trace real IDs and values, arithmetic, inclusion/exclusion, duplicates, grouping, NULLs and ordering.
7. **Step 1 · Your approach before writing SQL** — stop for the learner's independent plain-English plan before revealing SQL.
8. **Approach review / agreed approach** — rate the learner's plan out of 10, identify correct reasoning and gaps, allow revision, then save the agreed progression.
9. **Final learner solution — SQLite** — exact locked learner query, not silently rewritten.
10. **Final learner solution — SQL Server adaptation** — separate executable dialect adaptation; disclose any unverified engine execution.
11. **Important learnings** — question-specific concepts, patterns, decisions, mistakes corrected, edge cases, and reusable rules learned. Explain why, not just what.
12. **Visual walkthrough** — question-specific diagram plus full-size link and Previous/Next stages/fixture when available.
13. **Step-by-step walkthrough** — actual FROM source, each operation in execution order, SQL fragment, intermediate rows/output, row counts, and why each operation is needed. Trace concrete sample IDs. Explain join preservation, keys, duplicates, filters, grouping, calculations, NULL/zero, and sort as applicable.
14. **Official solution** — preserve the source answer verbatim, identify dialect and exact source; add separate SQLite and SQL Server adaptations.
15. **Comparison with the course answer** — explain semantic and dialect differences; never silently normalize the learner query or official answer.
16. **Verification** — engine/version and date, exact sample output checks, row counts, edge cases, reconciliation/invariants, dialect execution status, and anything still pending.

## Mandatory working protocol

- Follow the source question order and the learner's repo as source of truth. Do not invent or skip questions.
- Present the original question, output contract, named input tables, expected output and worked sample before Step 1.
- Pause at Step 1. Do not reveal the solution before the learner has attempted the approach.
- Ask what one result row represents; identify driving source/table order; joins and keys; row-preservation rules; row/group/metric filters; grouping and aggregation; duplicates; NULL/zero/boundaries/ties; sorting; and trace sample rows.
- Review and score the approach /10. Let the learner revise before SQL.
- Build the query incrementally using the same sample. Show intermediate result sets and row counts. Explain why each clause belongs and what changes.
- Preserve the learner-selected final SQL verbatim. Keep official SQL separate. Distinguish tested observations from guarantees over all possible datasets.
- Keep all existing valid content when repairing a record. Never delete or replace content merely to make headings match. Add missing sections, correct inaccurate statements transparently, and retain source links/assets.
- Use source colors consistently in question, sample, walkthrough and visual. Use 🟪 for calculations combining sources. Label every table and preserve color on NULLs.
- Every walkthrough stage must connect to the same sample and saved learner query. Final visual rows must match the saved query's output.
- Save the verified query, expected output, learnings and checks to the question's own MD file. Update index/status only when appropriate. Verify the committed file contents and report exactly which paths changed.
- If a record lacks a meaningful section (for example, a multi-table join explanation for a single-table query), mark it not applicable with a reason rather than fabricate content.

## Pre-save and audit checklist

- [ ] PNP-P026 structure and level of detail used as reference.
- [ ] Source wording, ID, topic and difficulty retained.
- [ ] Table-color key and named inputs are correct.
- [ ] Required output columns fully specified in order.
- [ ] Source sample distinguished from added practice data.
- [ ] Expected output and worked sample arithmetic independently checked.
- [ ] Learner's approach captured, reviewed /10 and agreed before SQL.
- [ ] Final learner SQLite SQL preserved verbatim.
- [ ] SQL Server adaptation kept separate and verification status stated.
- [ ] Important learnings and edge cases recorded.
- [ ] Visual and written walkthrough match the sample and final SQL.
- [ ] Official answer preserved, sourced and adapted separately.
- [ ] Comparison explains meaningful differences.
- [ ] Verification records engine, checks, edge cases and pending work.
- [ ] Existing content/assets/links preserved; no unrelated files changed.
- [ ] GitHub file re-fetched after commit to verify the final content.

## Previous-question repair rule

When auditing an older record, compare it against PNP-P026.md and this checklist. Add missing material without losing existing content. Do not claim an older record is compliant until its full contents, assets and saved query have been checked. Keep an audit list of checked, repaired and still-pending question IDs.

## Exact PNP-P026 section order — mandatory, not approximate

The heading sequence in PNP-P026.md is the required canonical order. Every completed PNP and Bosscoder record must use the same sequence and heading names, adapting only the question title, source dialect, and truly inapplicable content:

1. `# PNP Pxxx — <question title>` or `# Bosscoder x.xx — <question title>`
2. `## Question`
3. `### Required output columns`
4. `### Practice example · Sample input` (or clearly labeled assignment-provided example)
5. `### Expected output`
6. `### How the sample produces this output`
7. `## Step 1 · Your approach before writing SQL`
8. `## Final learner solution — SQLite` (or `## My solution — SQLite`; preserve the repo's established exact label for the record once standardized)
9. `## Important learnings from <ID>`
10. `## Visual walkthrough`
11. `## Step-by-step walkthrough`
12. `## Learner solution — SQL Server adaptation`
13. `## Official solution`
14. `## Comparison with the course answer`
15. `## Verification`

The content under each section must meet the depth demonstrated by P026. Do not substitute headings such as `Progressive walkthrough`, `Step-by-step solution`, `Step-by-step explanation`, or `Written step-by-step explanation`: standardize them to the exact heading `## Step-by-step walkthrough`. A question with no join still needs the walkthrough; explain its single-table, scalar, CTE, or set-operation stages instead of inventing a join.

For Bosscoder records, retain the assignment's original statement and official solution, but use the same section order and exact walkthrough heading. If a section is genuinely not applicable, keep its heading and state why it is not applicable; do not silently omit it.

## Completion gate

A record is **not complete** merely because it has SQL, a visual, or a verification section. Before marking it solved/complete, fetch the saved file and check every section above in order, plus the query, worked sample, visual, written walkthrough, official answer, comparison and verification. If any item is missing, the record remains **needs repair**. Apply the same gate to all future records.

## Index update — mandatory finalization step

Immediately after a question is solved, its final learner solution is reviewed and confirmed 100% correct for the stated requirements, and its saved Markdown file passes the PNP-P026 structure/completion gate, update the practice-question index in the same completion workflow.

- Update the relevant category index/README and the main practice-question `README.md` wherever that question is listed or counted.
- Add the question exactly once, under the correct category and difficulty, with the correct ID, title, and working relative link.
- Update any totals, progress counts, status tables, or navigation lists affected by the new completed question.
- Do not index a question as solved/completed while its final solution is unverified, its required sections are missing, or its file has not been saved.
- After the index write, fetch the updated index file(s) from GitHub and verify the entry, link, category, counts, and absence of duplicates.
- Treat the question and its index entry as one completion transaction: if the index cannot be updated or verified, report the question as solution-complete but index-pending; do not claim full completion.
- Apply this to every future PNP and Bosscoder question and when repairing historical records whose index entries are missing or incorrect.

## Mandatory dual-visual standard — overview flowchart + progressive walkthrough

Every completed PNP and Bosscoder solution record must contain **both** visual types below. They serve different purposes and must not replace one another.

### A. Row-preservation / query-flow overview (flowchart)

Include a compact, readable flowchart similar to the P034 row-preservation map:

- Show the source tables as separate inputs, using the same source-color key as the question and sample tables.
- Show the JOIN operation(s), including the JOIN type and the order in which tables enter the query.
- Show key transformations such as COALESCE/fallback labels, filtering, grouping, aggregation, window calculations, percentage/metric calculation, and final sorting, as applicable.
- Show parallel branches when a denominator, lookup, CTE, or independent aggregate is computed separately, and where the branches combine.
- Make row-preservation intent explicit: which unmatched rows survive and why.
- Keep labels concise and ensure the flow is readable at normal viewing size.
- Use a native, editable text-based diagram format in the Markdown source (Mermaid is acceptable); do not rely only on a raster screenshot.
- The flowchart is an overview of query architecture. It does **not** count as the progressive visual walkthrough.

### B. Progressive visual walkthrough (P026-style)

Include a second visual that demonstrates **how the actual sample rows move and change progressively through the saved learner query**, stage by stage. This is the P026-style teaching visual and is mandatory.

- Start from the exact sample input rows and show each meaningful query stage in SQL execution/logical transformation order.
- Show intermediate result tables after each important operation: source selection, each JOIN, row classification/labeling, filters, grouping, aggregation, calculations, and sorting, as applicable.
- Preserve the source-color convention in headers, values, NULLs, keys, derived columns and explanations: 🟥/🟩/🟦 for source-specific data and 🟪 for combined/calculated values. Match the question's own color key.
- Track concrete row IDs and values across stages. Make added rows, removed rows, unmatched rows, duplicate/group membership and NULL introduction visible.
- Explain what changed at each stage and why the corresponding clause is required. The reader must be able to trace a final output row backwards to its source rows.
- Use the exact same fixture and business rules as the question's expected output and the saved learner SQL. Do not introduce a second inconsistent sample.
- The final stage must match the saved learner query's expected output exactly, including output columns, row values, NULL/zero behavior and sort order.
- Include a full-size/open link to the visual asset where the repository's asset convention supports it. Keep the visual source/editable asset in the repository; do not commit only a flattened screenshot when a source format is available.
- For multi-step visuals, provide Previous/Next stage navigation or a numbered sequence of stage files where the established P026 asset convention is used. Ensure all links resolve.
- If the question has no joins, show the equivalent progressive stages (input → filtering/derivation → grouping/window/set operation → calculation → final result); never omit the progressive visual merely because there is no JOIN.

### Distinguishing the two visuals

- **Flowchart:** answers “What is the query architecture and why are these operations connected this way?”
- **Progressive walkthrough:** answers “What happens to these exact rows at every stage until the final result?”
- A flowchart alone is insufficient. A written walkthrough alone is insufficient. A single diagram is acceptable only if it genuinely contains both the architecture overview and the full row-by-row progressive transformations at readable detail; prefer two separate visuals as in this standard.

### Historical and future coverage

- Apply this dual-visual standard to every new question and every solution record created from now on.
- Audit all previously saved PNP and Bosscoder solution records against this standard and PNP-P026. Preserve existing valid visuals and assets; add whichever visual type is missing or repair whichever is inaccurate. Do not mark a historical record compliant until both visuals and their links have been fetched and checked.
- Maintain an explicit audit status for historical question IDs: flowchart present/verified, progressive visual present/verified, written walkthrough aligned, final visual output aligned, repair pending/completed.
- When repairing a historical question, use its own saved learner query and sample fixture. Do not copy P026's content or fabricate generic visuals.
- Do not claim every previous record has been retrofitted merely because this requirement was added to skills.md. Report the exact question IDs audited/repaired and the remaining backlog.

### Additions to the pre-save and audit checklist

- [ ] Row-preservation/query-flow overview flowchart is present, readable, source-colored and aligned to the actual query.
- [ ] Separate P026-style progressive visual shows the exact sample rows through every meaningful query stage.
- [ ] Progressive stages preserve row IDs, source colors, NULLs, grouping, calculations and ordering.
- [ ] Final progressive visual output exactly matches the saved learner query and expected output.
- [ ] Visual source assets and Previous/Next/full-size links exist and have been re-fetched/verified.
- [ ] Both visual types are present for any historical record claimed as repaired or compliant.

