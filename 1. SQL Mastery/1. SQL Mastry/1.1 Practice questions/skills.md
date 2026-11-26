# SQL Practice Record Skills — Canonical Six-Section Standard

This file is the single source of truth for every PNP and Bosscoder question record. The mandatory structure is **exactly six top-level sections**. Do not add, remove, rename, or reorder them.

## Required six-section structure

1. **Question — Business Scenario & Task**
   - Preserve the original question wording, source, question ID, topic and difficulty.
   - Explain the business scenario and task.
   - State the row grain, eligibility rules and sorting requirements.
   - Document every required output column in the exact requested order. For each column, explain its source/calculation, business meaning, row-level behavior, NULL/zero/fallback behavior and any applicable rule.
   - Include the table-color key.
   - Any learner approach and approach review/score belongs here as a nested subsection; do not create a seventh section.

2. **Example — Input & Expected Output**
   - Show every complete input table separately, with column meanings.
   - State whether the data is supplied by the source or is an illustrative teaching fixture created for the record.
   - Show the complete expected output with exact columns, values and order.
   - Explain how the input produces the expected output: calculations, grouping, inclusion/exclusion, duplicates, NULLs, boundaries, sorting and row counts.
   - Never present invented data or inferred output as source-provided or executed output.

3. **My Solution — SQLite & SQL Server**
   - Preserve the learner's final SQLite SQL exactly as submitted.
   - Keep the SQL Server adaptation separate and clearly label its status.
   - Do not silently rewrite, optimize, normalize, or merge either dialect.
   - Record any known gaps or semantic differences beside the relevant solution without changing the preserved query.

4. **Official Solution**
   - Preserve the official source solution verbatim.
   - Identify the exact source file/page/question and source dialect/version where known.
   - Keep official SQL separate from the learner's SQL.
   - Any dialect adaptations must be clearly labeled as adaptations, not as the original official answer.

5. **Step-by-Step Detailed Walkthrough**
   - Use the user's complete progressive walkthrough prompt and its requirements. Use one example from beginning to end; never switch fixtures midway.
   - Begin with the complete input datasets, column meanings, initial row counts and expected result.
   - Explain the query in logical execution/dependency order, not merely textual clause order.
   - Every meaningful stage must contain all six parts, in this exact order:
     A. Original code fragment
     B. What happens here?
     C. Trace the single example
     D. Complete intermediate output
     E. Row count / state check
     F. Key takeaway
   - Show the complete intermediate result after each stage, not only changed rows. Explain why the operation is required, its inputs, transformations and relevant dialect behavior.
   - Cover applicable SQL behavior: FROM, JOIN and row preservation, WHERE, GROUP BY, aggregates, CTEs/subqueries, windows, SELECT-derived columns, NULL/zero, ORDER BY and LIMIT/OFFSET.
   - Preserve concrete IDs and values throughout. Make every final row traceable to source rows.
   - Do not create or include visuals: no SVGs, diagrams, flowcharts, screenshots, image-based walkthroughs, or Previous/Next visual pages. Use written explanations and readable Markdown tables only.
   - End this section with complete original query reference, final output, execution-flow summary, stage/row-count summary, edge cases and verification status. Clearly distinguish executed results from manually derived or expected results. State engine/version assumptions and never claim execution that did not occur.

6. **My New Learnings**
   - Record question-specific concepts, reusable SQL patterns, mistakes corrected, why the corrections matter, edge cases and interview takeaways.
   - Keep the learnings grounded in the actual question and verified example.

## Non-negotiable rules

- Exactly six top-level sections in every question Markdown file. Use nested headings under them as needed; no seventh top-level section for approach review, visuals, comparison, verification, or audit.
- Keep the six section titles and order exactly as written above.
- Do not delete valid question-specific content while reorganizing. Move it under the correct section and preserve useful assets and links.
- Keep original question, learner SQL and official SQL distinct. Preserve learner SQL verbatim.
- Use one consistent fixture across expected output, written walkthrough and visuals. Label illustrative fixtures honestly.
- Do not fabricate missing source data, query output, execution evidence, engine/version, or verification.
- A completed walkthrough must show each meaningful transformation and complete intermediate output with A–F. If a stage does not change the rows, still show and explain its state.
- Use source colors consistently across question, input, expected output, written walkthrough and visuals.
- Keep the walkthrough entirely text-and-table based. Do not add visual assets or visual navigation.
- If a requirement is genuinely inapplicable, retain the relevant nested subsection and state why. Do not invent content to fill it.
- Never mark a question solved while its final learner query, expected output, six-section structure, walkthrough, official answer and verification status have not been checked.

## Detailed walkthrough prompt (mandatory)

Use the user's full prompt titled **“Task: Explain Code Through a Detailed Progressive Walkthrough Using One Example”** as the governing template for Section 5 of every question record. Preserve all of its requirements: one consistent example; complete inputs and meanings; initial counts; logical execution order; meaningful stages with A–F; complete intermediate outputs; SQL-specific clause behavior; complete original code and final output; stage summary; learnings; edge cases; explicit distinction between executed and manually derived results; dialect/version assumptions; and exact preservation of learner code. Do not omit any stage, including unchanged stages. Use readable Markdown tables for intermediate datasets. Do not create visuals of any kind.

## Index-page standard

The practice index must display the same six section names only when showing the per-question structure/checklist. Do not expose the old long list of 15–20 sub-requirements as separate index columns or section numbers. Keep question navigation, topic, difficulty and solved/pending status as metadata, not additional content sections.

For every index update:
- Add a question once under the correct topic and difficulty with a working relative link.
- Show exactly these six structure checkpoints, in order: Question — Business Scenario & Task; Example — Input & Expected Output; My Solution — SQLite & SQL Server; Official Solution; Step-by-Step Detailed Walkthrough; My New Learnings.
- Verify the updated index from GitHub after saving. Check the question link, category, title, status, duplicate entries and the six displayed checkpoints.
- Do not mark a question solved if its verification is pending.

## Pre-save and post-save checklist

- [ ] Exactly six top-level sections, with exact titles and order.
- [ ] Original source question, scenario, task and output contract preserved.
- [ ] Complete input and expected output are grounded and reconciled.
- [ ] Learner SQLite and SQL Server solutions are separate; submitted SQL preserved verbatim.
- [ ] Official source answer is verbatim and sourced.
- [ ] One-fixture walkthrough has every meaningful stage with A–F and complete intermediate outputs.
- [ ] No diagrams, SVGs, screenshots, or other visuals are included; the walkthrough uses written stages and complete tables only.
- [ ] Learnings are question-specific and useful.
- [ ] Execution, dialect, edge-case and verification status are stated honestly.
- [ ] All assets and links have been fetched and checked.
- [ ] Index displays exactly six checkpoints and the correct question metadata/status.
- [ ] Re-fetch the committed question file, skills.md and changed index file(s) and verify the saved contents.

## Historical records

Apply this standard when creating or repairing any PNP or Bosscoder record. Reorganize existing content under the six sections without losing valid details. Track exactly which records have been audited and repaired; never claim the historical backlog is complete based only on this standard being updated.
