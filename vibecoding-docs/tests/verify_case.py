"""Check observable fixture results without pretending to grade Agent reasoning.

The program reads a completed isolated case. It never edits the result directory.
Exact file preservation, unwanted installation, ADR numbering, and duplicate
headings are deterministic checks; intent, immediate conflict reporting, and
semantic correctness still require the rubric in cases.json.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def verify_structural(case: dict[str, Any], actual: dict[str, str]) -> list[str]:
    """Return structural failures for one completed case.

    case contains the documented before snapshot and expect constraints.
    actual maps result-relative POSIX file paths to decoded text. Missing files
    stay absent. The function has no filesystem effects; an empty failure list
    covers structural constraints only, not the semantic expectations.
    """
    before = case["before"]
    expect = case["expect"]
    failures: list[str] = []
    for path in expect.get("unchanged", []):
        if actual.get(path) != before.get(path):
            failures.append(f"File changed despite preservation requirement: {path}")
    for path in expect.get("changed", []):
        if path not in actual or actual[path] == before.get(path):
            failures.append(f"Required update missing: {path}")
    for path in expect.get("created", []):
        if path not in actual:
            failures.append(f"Required file missing: {path}")
    for path in expect.get("forbidden_created", []):
        if path not in before and path in actual:
            failures.append(f"Unrequested installation: {path}")
    for required in expect.get("preserve", []):
        if not any(required in text for text in actual.values()):
            failures.append(f"Existing user content lost: {required}")
    for path, required_texts in expect.get("contains", {}).items():
        for required in required_texts:
            if required not in actual.get(path, ""):
                failures.append(f"Required text missing: {path}: {required}")
    for path, headings in expect.get("heading_count", {}).items():
        text = actual.get(path, "")
        for heading, count in headings.items():
            matches = re.findall(r"^#{1,6}[ \t]+" + re.escape(heading) + r"[ \t]*$", text, re.M)
            if len(matches) != count:
                failures.append(f"Heading count mismatch: {path}: {heading}")
    prefix = expect.get("new_adr_prefix")
    if prefix:
        added = set(actual) - set(before)
        if not any(Path(path).name.startswith(prefix) for path in added):
            failures.append(f"New ADR with required prefix missing: {prefix}")
    return failures


def read_result(root: Path) -> dict[str, str]:
    """Read completed fixture text for deterministic comparison.

    root is the isolated result directory. Returned keys are relative POSIX paths.
    Newline bytes are preserved so unchanged snapshots remain exact. Binary
    files and internal .git/cache artifacts are excluded; invalid UTF-8
    is skipped rather than decoded into misleading replacement characters.
    No generated files or bytecode are written.
    """
    result: dict[str, str] = {}
    for path in root.rglob("*"):
        if not path.is_file() or any(part in {".git", "__pycache__"} for part in path.relative_to(root).parts):
            continue
        try:
            result[path.relative_to(root).as_posix()] = path.read_bytes().decode("utf-8")
        except UnicodeDecodeError:
            continue
    return result


def main() -> int:
    """Read a case/result pair and return a structural verification exit status.

    Inputs come from command-line paths and the selected case id. Exit 1 means a
    deterministic invariant failed; exit 0 means those checks passed and human
    semantic review remains. Missing or unknown cases are explicit usage errors.
    This function only reads files and prints the result.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case_id")
    parser.add_argument("result_directory", type=Path)
    args = parser.parse_args()
    if not args.result_directory.is_dir():
        parser.error("result_directory must be an existing isolated case")
    cases = json.loads(Path(__file__).with_name("cases.json").read_text(encoding="utf-8"))["cases"]
    case = next((item for item in cases if item["id"] == args.case_id), None)
    if case is None:
        parser.error(f"Unknown case: {args.case_id}")
    failures = verify_structural(case, read_result(args.result_directory))
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("Structural checks passed; assess semantic expectations and reporting separately.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
