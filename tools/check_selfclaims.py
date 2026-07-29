#!/usr/bin/env python3
"""Check the claims this repository makes *about itself* against itself.

Why this exists
---------------
`check_verbatim.py` guards quotations. It cannot guard the other half of what
this repository asserts: its own bookkeeping. Those claims decay in a specific
way — the same fact gets written in two places, one place is maintained, and
the other is not.

Three defects found in this repository fell into three different classes:

  1. A verbatim quote widened past its source.
     -> caught by tools/check_verbatim.py.
  2. A claim that all the quoted guides live in one repository under one
     licence, when one of them does not.
     -> NOT caught here. See "What this does not cover" below.
  3. A status line reading "2 of 9 blocks written" beside a table listing
     nine, because only the table was being updated.
     -> caught here.

Class 3 is invisible to a human reader by construction: the two statements sit
in different parts of a long file, and the one you are editing looks right.
A machine that counts is the only reliable reader.

What it checks
--------------
  A. Progress counters ("N of 9 blocks written") equal the number of block
     sections that actually exist.
  B. The block-status table's "written below" rows equal that same number.
  C. `[NOT YET WRITTEN]` markers in the table equal the number not written.
  D. Every repo-local path written in backticks exists on disk.
     (This is the class that let `tools/check-verbatim.sh` — a file that never
     existed — sit in NOTICE while the real file was `check_verbatim.py`.)
  E. The corpus guide-count claim ("eighteen guides") equals the number of
     guide sections in language-style-guide-patterns.md.

What this does not cover
------------------------
Class 2 — a prose claim about which upstream repository or licence a guide
belongs to. A registry-plus-sentence-matching prototype was written and
measured before this file was committed: it produced 27 flags of which nearly
all were false, and it missed the one real instance, whose sentence does not
name the guide it is wrong about. It was not installed. Verifying licence and
provenance claims against upstream remains a human step, and NOTICE says so.

Recording that failure here is deliberate: the next person to have this idea
should know it was tried and measured, not assume it was overlooked.

Usage
-----
    python tools/check_selfclaims.py
    python tools/check_selfclaims.py --self-test   # prove it goes red

Exit code 0 = green, 1 = the repository contradicts itself.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
BLOCKS_FILE = "catalog/for-engineers-3-6-9.md"
CORPUS_FILE = "catalog/language-style-guide-patterns.md"

# Sections in the corpus file that are not a guide read-through.
NON_GUIDE_SECTIONS = ("Cross-language pattern", "Honesty note")

WORD_NUMBERS = {
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
}

# Top-level directories and root files that are part of this repository, used
# to tell a repo-local path from an upstream one like `pyguide.md`.
LOCAL_PREFIXES = ("catalog/", "tools/", "skills/")
LOCAL_ROOT_FILES = {"README.md", "README.ja.md", "NOTICE", "LICENSE"}

PATH_RE = re.compile(r"`([A-Za-z0-9_./-]+\.(?:md|py|sh|txt|yml|json))`")


def read(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def md_files() -> list[pathlib.Path]:
    files = [p for p in REPO.rglob("*.md") if ".git" not in p.parts]
    notice = REPO / "NOTICE"
    if notice.exists():
        files.append(notice)
    return files


def is_local(path: str) -> bool:
    return path.startswith(LOCAL_PREFIXES) or path in LOCAL_ROOT_FILES


def check(injected: str = "") -> list[str]:
    """Return a list of failure messages. Empty list means green."""
    failures: list[str] = []
    blocks_text = read(BLOCKS_FILE) + injected

    # --- A / B / C: block bookkeeping -----------------------------------
    written = len(re.findall(r"^### Block \d+ — ", blocks_text, re.M))
    total_match = re.search(r"\| 9 \|", blocks_text)
    total = 9 if total_match else written

    for m in re.finditer(r"(\d+) of (\d+) (?:blocks )?written", blocks_text):
        claimed, of = int(m.group(1)), int(m.group(2))
        # A counter inside a sentence describing a past state is exempt only
        # if it is explicitly marked as historical.
        context = blocks_text[max(0, m.start() - 200):m.start()]
        if "read \"" in context or "read '" in context or "used to read" in context:
            continue
        if of != total or claimed != written:
            failures.append(
                f"A. {BLOCKS_FILE}: counter says '{m.group(0)}' but "
                f"{written} block sections exist (of {total})."
            )

    table_written = len(re.findall(r"\*\*written below\*\*", blocks_text))
    if table_written != written:
        failures.append(
            f"B. {BLOCKS_FILE}: status table marks {table_written} rows "
            f"'written below' but {written} block sections exist."
        )

    table_pending = len(re.findall(r"\| `\[NOT YET WRITTEN\]`", blocks_text))
    if table_pending != total - written:
        failures.append(
            f"C. {BLOCKS_FILE}: table has {table_pending} [NOT YET WRITTEN] "
            f"rows but {total - written} of {total} blocks are unwritten."
        )

    # --- D: repo-local paths exist ---------------------------------------
    for f in md_files():
        text = f.read_text(encoding="utf-8")
        if f.name == pathlib.Path(BLOCKS_FILE).name:
            text += injected
        for path in sorted(set(PATH_RE.findall(text))):
            if is_local(path) and not (REPO / path).exists():
                rel = f.relative_to(REPO)
                failures.append(
                    f"D. {rel}: references `{path}`, which does not exist."
                )

    # --- E: corpus guide count -------------------------------------------
    corpus = read(CORPUS_FILE)
    sections = re.findall(r"^## (.+)$", corpus, re.M)
    guide_sections = [s for s in sections if not s.startswith(NON_GUIDE_SECTIONS)]
    actual = len(guide_sections)

    for f in md_files():
        text = f.read_text(encoding="utf-8")
        if f.name == pathlib.Path(BLOCKS_FILE).name:
            text += injected
        flat = re.sub(r"\s+", " ", text)
        for m in re.finditer(r"\b(" + "|".join(WORD_NUMBERS) + r")\b[^.]{0,40}?guides", flat):
            claimed = WORD_NUMBERS[m.group(1).lower()]
            # "the seventeen guides above plus this one" is arithmetic, not a
            # total. Skip a count that is immediately being added to.
            if re.match(r"[^.]{0,60}?\bplus\b", flat[m.end():]):
                continue
            if claimed != actual:
                rel = f.relative_to(REPO)
                failures.append(
                    f"E. {rel}: claims '{m.group(1)} ... guides' but "
                    f"{CORPUS_FILE} has {actual} guide sections."
                )
    return failures


def report(failures: list[str]) -> int:
    if not failures:
        print("green: the repository's claims about itself match the repository.")
        print("  checked: block counters, status table, [NOT YET WRITTEN] markers,")
        print("           repo-local path references, corpus guide count.")
        return 0
    print("RED: the repository contradicts itself.\n")
    for f in failures:
        print(f"  {f}")
    print("\n  Fix the claim, or fix the thing it claims about — but not neither.")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="inject a stale counter and confirm the check goes red",
    )
    args = parser.parse_args()

    if args.self_test:
        injected = "\n\nStatus: 2 of 9 blocks written.\n"
        print("self-test: injecting a stale progress counter --")
        print(f"  {injected.strip()}\n")
        failures = check(injected=injected)
        if not any(f.startswith("A.") for f in failures):
            print("SELF-TEST FAILED: the stale counter passed. The check is decorative.")
            return 1
        report(failures)
        print("\nself-test passed: the stale counter was rejected.")
        print("now re-running without it --\n")
        return report(check())

    return report(check())


if __name__ == "__main__":
    sys.exit(main())
