"""Build GitHub-readable Previous/Next pages from a practice fixture and SQLite.

    python tools/build_steps.py assets/steps/PNP-P031/walkthrough.json
    python tools/build_steps.py assets/steps/PNP-P031/walkthrough.json --check

Paths inside a manifest are relative to that manifest. The final query is read
from the learner's saved Markdown. Each SELECT runs against the same fixture.
"""

import argparse
import html
import json
import math
import os
import re
import sqlite3
from pathlib import Path
from urllib.parse import quote


def ident(name):
    return '"' + name.replace('"', '""') + '"'


def display(value):
    if value is None:
        return "NULL"
    if isinstance(value, str):
        if not value or value != value.strip():
            return repr(value)
        return value
    return str(value)


def markdown_table(headers, rows):
    def line(items):
        return "| " + " | ".join(html.escape(display(v)).replace("|", "&#124;").replace("\n", "<br>") for v in items) + " |"
    body = [line(headers), line(["---"] * len(headers)), *(line(row) for row in rows)]
    if not rows:
        body.extend(["", "*0 rows*"])
    return "\n".join(body)


def read_solution(path, heading, index):
    lines = path.read_text(encoding="utf-8").splitlines()
    level = None
    start = None
    for i, line in enumerate(lines):
        match = re.fullmatch(r"(#{1,6}) (.+)", line)
        if match and match[2] == heading:
            level, start = len(match[1]), i + 1
            break
    if start is None:
        raise ValueError(f"Missing learner solution heading in {path}: {heading}")
    stop = next((i for i in range(start, len(lines)) if re.match(rf"^#{{1,{level}}} ", lines[i])), len(lines))
    blocks = re.findall(r"^\x60\x60\x60sql\s*\n(.*?)^\x60\x60\x60[ \t]*$", "\n".join(lines[start:stop]), re.M | re.S | re.I)
    if index < 0 or index >= len(blocks):
        raise ValueError(f"Missing SQLite block {index + 1} in {heading}")
    return blocks[index].rstrip()


def dataset(db, sql):
    cursor = db.execute(sql)
    if not cursor.description:
        raise ValueError("A walkthrough stage must return rows")
    return [col[0] for col in cursor.description], [list(row) for row in cursor.fetchall()]


def same_result(actual, expected, unordered):
    names, rows = actual
    if names != expected["columns"] or len(rows) != len(expected["rows"]):
        return False
    def cells_equal(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return math.isclose(a, b, rel_tol=1e-12, abs_tol=1e-10)
        return a == b
    def row_equal(a, b):
        return len(a) == len(b) and all(cells_equal(x, y) for x, y in zip(a, b))
    if not unordered:
        return all(row_equal(a, b) for a, b in zip(rows, expected["rows"]))
    unmatched = list(expected["rows"])
    for row in rows:
        index = next((i for i, other in enumerate(unmatched) if row_equal(row, other)), None)
        if index is None:
            return False
        unmatched.pop(index)
    return True


def build(manifest):
    conf = json.loads(manifest.read_text(encoding="utf-8"))
    record = manifest.parent / conf["record"]
    final_sql = read_solution(record, conf["solution_heading"], conf.get("solution_block", 0))
    steps = conf["steps"]
    if not steps or not steps[-1].get("final") or any(s.get("final") for s in steps[:-1]):
        raise ValueError("Mark exactly the last stage final")
    if len({step["id"] for step in steps}) != len(steps):
        raise ValueError("Each step needs a unique ID")

    with sqlite3.connect(":memory:") as db:
        db.execute("PRAGMA trusted_schema=OFF")
        sources = {}
        for table in conf["tables"]:
            name = table["name"]
            columns = table["columns"]
            if any(kind not in {"INTEGER", "TEXT", "REAL", "NUMERIC", "BLOB"} for _, kind in columns):
                raise ValueError(f"Unknown column type in {name}")
            ddl = ", ".join(f"{ident(field)} {kind}" for field, kind in columns)
            db.execute(f"CREATE TABLE {ident(name)} ({ddl})")
            marks = ", ".join("?" for _ in columns)
            db.executemany(f"INSERT INTO {ident(name)} VALUES ({marks})", table["rows"])
            if name in sources:
                raise ValueError(f"Duplicate fixture table {name}")
            source_color = table.get("color", "")
            fields = [(source_color + " " + col[0]).strip() for col in columns]
            sources[name] = (table.get("label", name), fields, table["rows"])
        db.execute("PRAGMA query_only=ON")
        pages = {}
        previous_id = None
        definitions = conf.get("ctes", {})
        for i, step in enumerate(steps):
            key = step["id"]
            if key in sources:
                raise ValueError(f"Duplicate stage/table ID {key}")
            if step.get("final"):
                sql = final_sql
            else:
                names = step.get("with", [])
                prefix = ",\n".join(f"{name} AS (\n{definitions[name]}\n)" for name in names)
                sql = ("WITH " + prefix + "\n" if prefix else "") + step["sql"]
            cols, rows = dataset(db, sql)
            if step.get("final") and not same_result((cols, rows), conf["expected"], conf.get("unordered", False)):
                raise ValueError(f"{record.name}: final saved SQLite result differs from the expected fixture")
            if "expected_count" in step and len(rows) != step["expected_count"]:
                raise ValueError(f"{key}: expected {step['expected_count']} rows, got {len(rows)}")
            inputs = step.get("inputs", [previous_id] if previous_id else [t["name"] for t in conf["tables"]])
            color_map = {**conf.get("column_colors", {}), **step.get("column_colors", {})}
            field_labels = [(color_map.get(c, "") + " " + c).strip() for c in cols]
            shown_rows = rows
            if source_field := step.get("row_source_field"):
                source_index = cols.index(source_field)
                palette = {t["name"]: t["color"] for t in conf["tables"]}
                shown_rows = [
                    [f"{palette[row[source_index]]} {display(cell)}" for cell in row]
                    for row in rows
                ]
            before = []
            for name in inputs:
                title, fields, data = sources[name]
                unit = "row" if len(data) == 1 else "rows"
                before.extend([f"**{title} · {len(data)} {unit}**", "", markdown_table(fields, data), ""])
            sources[key] = (step["title"], field_labels, shown_rows)
            previous_id = key
            def button(direction, destination):
                if destination is None:
                    return f"<kbd>{direction}</kbd>"
                return f"[![{direction}](../{direction.lower()}.svg)]({destination:02}.md)"
            nav = " ".join([button("Previous", i if i else None), button("Next", i+2 if i+1 < len(steps) else None), f" · **{i+1} of {len(steps)}**"])
            record_href = quote(os.path.relpath(record, manifest.parent), safe="/")
            parts = [f"# {conf['question']} · {step['title']}", "", nav, "", step["change"], "",
                     "## SQL added or changed", "", "\x60\x60\x60sql", step["added_sql"], "\x60\x60\x60", "",
                     "## Input to this step", "", *before,
                     f"## Result · {len(rows)} " + ("row" if len(rows)==1 else "rows"), "",
                     markdown_table(field_labels, shown_rows), "",
                     "<details>", "<summary>Full SQLite query for this step</summary>", "",
                     "\x60\x60\x60sql", sql, "\x60\x60\x60", "", "</details>", "", nav, "", f"[Back to the question and saved solutions]({record_href})", ""]
            pages[f"{i+1:02}.md"] = "\n".join(parts)
    return pages


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    pages = build(args.manifest)
    outdated = []
    for name, text in pages.items():
        path = args.manifest.parent / name
        if path.exists() and path.read_text(encoding="utf-8") == text:
            continue
        if args.check:
            outdated.append(name)
        else:
            path.write_text(text, encoding="utf-8")
    extras = {p.name for p in args.manifest.parent.glob("[0-9][0-9].md")} - set(pages)
    if extras or outdated:
        raise SystemExit(f"Stale stage files (changed or extra): {sorted(extras | set(outdated))}")
    print(f"{args.manifest.parent.name}: {len(pages)} stages verified")


if __name__ == "__main__":
    main()
