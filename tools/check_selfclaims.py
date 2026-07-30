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
  F. No commit in the history carries a `Co-Authored-By:` trailer (GR-013).
  G. The hook can actually run (G1: recorded executable in the index -- git
     skips a non-executable hook in silence), and any file that mentions it
     also states its three limits (G2), so the guard is never described as
     more than it is.
  H. Commits made after a recorded baseline use the GR-013 author.

Why F, G and H sit here rather than only in the hook
----------------------------------------------------
`.githooks/commit-msg` refuses the trailer while you are typing. It has three
holes, all of the same kind — they are holes in the *route*:

  * `git clone` does not carry it (`core.hooksPath` lives in `.git/config`),
  * `git commit --no-verify` walks straight past it,
  * it never looks at commits that already exist.

Enumerating routes never finishes; a new route is always one flag away. Check F
constrains the *result* instead: whatever route a commit took, if the trailer is
in the history, this goes red. That covers all three holes without knowing about
any of them.

Check G exists because the hook's presence is itself a claim. A repository that
says "commits are blocked from carrying the trailer" while shipping a guard that
a clone silently drops has made the same mistake this whole toolchain is built
to catch: stating a rule more broadly than the thing that enforces it.

There turned out to be a fourth hole, and it was found the honest way — by
measuring the pushed result instead of trusting the local action. The hook was
committed as mode 100644. `chmod +x` had been run, but this working copy has
`core.filemode = false`, so git recorded nothing; and git skips a
non-executable hook in complete silence. For one commit, anyone cloning this
repository onto Linux or macOS would have had a hook that never ran and never
said so. That is why G1 checks the index mode rather than the file on disk:
the disk bit is what was already believed, and belief is what failed.

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
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
BLOCKS_FILE = "catalog/for-engineers-3-6-9.md"
CORPUS_FILE = "catalog/language-style-guide-patterns.md"

HOOK = ".githooks/commit-msg"

# GR-013 took effect on 2026-07-30. Commits up to and including this one predate
# it, are published, and are not rewritten -- so check H starts after it. The
# baseline is named rather than inferred, so that "we comply" can never quietly
# come to mean "we moved the line."
GR013_BASELINE = "3608c1a"
GR013_AUTHOR = "NEWXUS <info@ouen-battle.com>"

# A file that describes the hook must also describe what the hook cannot do.
# Each entry is (label, regex that must appear somewhere in the same file).
HOOK_LIMITS = [
    ("not carried by clone", r"clone"),
    ("bypassable with --no-verify", r"--no-verify"),
    ("blind to existing commits", r"(already exist|existing commits|past commits)"),
]

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


def git(*args: str) -> str | None:
    """Run a git command, or return None if this is not a usable git checkout.

    A checkout is not guaranteed: this repository is also read as a plain
    directory of files. The history checks report that they were skipped
    rather than passing silently, because "no data" is not "no violations."
    """
    try:
        out = subprocess.run(
            ("git", "-C", str(REPO)) + args,
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
    except (OSError, ValueError):
        return None
    return out.stdout if out.returncode == 0 else None


def check(injected: str = "", injected_commit_body: str = "") -> list[str]:
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

    # --- F: no Co-Authored-By trailer anywhere in the history (GR-013) ----
    # The result, not the route. A commit made from a fresh clone with no
    # hooksPath, or with --no-verify, lands here just the same.
    log = git("log", "--format=%H%x00%B%x00")
    if log is None:
        failures.append(
            "F. skipped: not a usable git checkout, so the history could not be "
            "read. This is not a pass — GR-013 is unverified here."
        )
    else:
        entries = [e for e in log.split("\x00\x00") if e.strip()]
        if injected_commit_body:
            entries.append("0000000injected\x00" + injected_commit_body)
        for entry in entries:
            sha, _, body = entry.partition("\x00")
            if re.search(r"^Co-Authored-By:", body, re.M | re.I):
                subject = body.strip().splitlines()[0][:60] if body.strip() else ""
                failures.append(
                    f"F. commit {sha.strip()[:8]} carries a Co-Authored-By "
                    f"trailer (GR-013): \"{subject}\""
                )

    # --- G: the hook is never described as more than it is ----------------
    # G1: it has to be able to run at all. Git silently skips a hook that is
    # not executable -- no error, no output, the guard simply never fires. On
    # Windows `core.filemode` is false, so a local `chmod +x` is not recorded
    # in the index and the file reaches every other clone as 100644. This
    # repository shipped exactly that for one commit.
    mode = git("ls-files", "-s", HOOK)
    if mode is None:
        failures.append(
            f"G1. skipped: could not read the index mode of `{HOOK}`. "
            "Unverified, not passed."
        )
    elif mode.strip() and not mode.startswith("100755"):
        failures.append(
            f"G1. `{HOOK}` is recorded as mode {mode.split()[0]}, not 100755. "
            "Git skips a non-executable hook without saying so, so the guard "
            "would never fire for anyone who clones this. Fix with: "
            f"git update-index --chmod=+x {HOOK}"
        )

    # G2: wherever the hook is described, its limits are described too.
    for f in md_files():
        text = f.read_text(encoding="utf-8")
        if f.name == pathlib.Path(BLOCKS_FILE).name:
            text += injected
        if HOOK not in text:
            continue
        missing = [label for label, pat in HOOK_LIMITS
                   if not re.search(pat, text, re.I)]
        if missing:
            rel = f.relative_to(REPO)
            failures.append(
                f"G2. {rel}: describes `{HOOK}` without stating that it is "
                f"{', and '.join(missing)}. A guard's limits belong next to "
                f"the claim that it guards."
            )

    # --- H: GR-013 author on commits after the recorded baseline ----------
    authors = git("log", f"{GR013_BASELINE}..HEAD", "--format=%H%x1f%an <%ae>")
    if authors is None:
        pass  # baseline absent (shallow clone, or before it existed): nothing to check
    else:
        for line in authors.splitlines():
            if not line.strip():
                continue
            sha, _, who = line.partition("\x1f")
            if who.endswith("[bot]") or "users.noreply.github.com" in who:
                continue  # CI identities are not covered by GR-013
            if who != GR013_AUTHOR:
                failures.append(
                    f"H. commit {sha[:8]} is authored by '{who}', not "
                    f"'{GR013_AUTHOR}' (GR-013, from baseline {GR013_BASELINE})."
                )
    return failures


def report(failures: list[str]) -> int:
    if not failures:
        print("green: the repository's claims about itself match the repository.")
        print("  checked: block counters, status table, [NOT YET WRITTEN] markers,")
        print("           repo-local path references, corpus guide count,")
        print("           Co-Authored-By across the whole history (GR-013),")
        print("           the hook being executable and its limits stated where described,")
        print(f"           commit author since {GR013_BASELINE}.")
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
        injected_commit = (
            "Add a thing\n\nCo-Authored-By: Somebody <somebody@example.com>\n"
        )
        print("self-test: injecting two defects that actually occurred --")
        print(f"  (A) a stale counter: {injected.strip()}")
        print("  (F) a commit body carrying: Co-Authored-By: Somebody <...>\n")
        failures = check(injected=injected, injected_commit_body=injected_commit)
        missed = [
            letter for letter in ("A.", "F.")
            if not any(f.startswith(letter) for f in failures)
        ]
        if missed:
            print(f"SELF-TEST FAILED: {', '.join(missed)} passed. The check is decorative.")
            return 1
        report(failures)
        print("\nself-test passed: both injected defects were rejected.")
        print("now re-running without them --\n")
        return report(check())

    return report(check())


if __name__ == "__main__":
    sys.exit(main())
