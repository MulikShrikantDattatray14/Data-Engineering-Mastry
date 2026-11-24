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
