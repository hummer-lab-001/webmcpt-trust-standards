#!/usr/bin/env python3
"""Check that every verbatim quote in a derived catalog file is already
present, character-for-character, in the source-verified corpus files.

Why this exists
---------------
Files like `catalog/for-engineers-3-6-9.md` claim, in their own honesty
ledger, to introduce "no new verbatim" — they only re-cut quotes that were
already confirmed against raw sources in the corpus files. That claim used to
be checkable only by hand, and only if the person checking happened to
normalise whitespace first: Markdown wraps long quotes across lines, so a
plain grep for a quoted sentence returns zero matches and looks like a
failure, or (worse) a slightly *widened* quote looks like a pass because
nobody compared it to the original.

This script removes the need to be clever. It normalises whitespace on both
sides and fails loudly when a quote in the derived file cannot be found in the
corpus.

It caught a real defect on its first run: Hook 2 quoted Go's line-length rule
as "There is no fixed line length for Go source code," where the corpus
records "There is no fixed line length for comments in Go." The quote had been
silently widened past the guide's own scope.

What it does NOT do
-------------------
It does not re-fetch the upstream style guides. It verifies the *internal*
chain (derived file -> corpus), not the *external* one (corpus -> Google).
Re-confirming the corpus against raw sources is still a human step.

Usage
-----
    python tools/check_verbatim.py            # check the default targets
    python tools/check_verbatim.py --self-test  # prove it goes red

Exit code 0 = green, 1 = a quote is unsourced or has drifted.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent

# The files whose quotes were confirmed against raw upstream sources.
CORPUS = [
    "catalog/language-style-guide-patterns.md",
    "catalog/combination-packs.md",
]

# The derived files that claim to only re-cut corpus material.
TARGETS = [
    "catalog/for-engineers-3-6-9.md",
]

# Quotes that legitimately do not appear in the corpus. Every entry needs a
# reason, and the reason has to be a fact about sourcing -- not "this one is
# annoying." An empty allowlist is the ideal; each entry is a small debt.
ALLOWLIST = {
    "Method names are written in lowerCamelCase.":
        "Java SG 5.2. Fetched from the published guide while writing "
        "Collision 6; the prior corpus records no Java naming table. Stated "
        "inline in the file.",
    "Local variable names are written in lowerCamelCase.":
        "Java SG 5.2, same fetch as above.",
    "Use CapWords for class names, but lower_with_under.py for module names.":
        "Python SG 3.16, same fetch as above; the prior corpus records no "
        "Python naming table either.",
}

# Verbatim quotes are written as *"..."* -- italicised and in quotation marks.
QUOTE_RE = re.compile(r'\*"([^"]+)"\*')


def normalise(text: str) -> str:
    """Collapse Markdown's line wrapping and escaping so two spellings of the
    same sentence compare equal."""
    for escaped, plain in (("\\_", "_"), ("\\*", "*"), ('\\"', '"')):
        text = text.replace(escaped, plain)
    return re.sub(r"\s+", " ", text).strip()


def comparable(quote: str) -> str:
    """A quote may be cut mid-sentence for grammar (leading ellipsis, trailing
    comma). Strip only that framing -- never interior words."""
    return normalise(quote).strip(".,").lstrip(".").strip()


def load(paths: list[str]) -> str:
    return " ".join(normalise(( REPO / p).read_text(encoding="utf-8")) for p in paths)


def check(targets: list[str], extra_quotes: list[str] | None = None) -> list[tuple[str, str]]:
    corpus = load(CORPUS)
    failures: list[tuple[str, str]] = []
    for target in targets:
        text = normalise((REPO / target).read_text(encoding="utf-8"))
        quotes = QUOTE_RE.findall(text)
        if extra_quotes:
            quotes = quotes + extra_quotes
        for quote in sorted(set(quotes)):
            if comparable(quote) in corpus:
                continue
            if normalise(quote).strip('.,') in {normalise(k).strip('.,') for k in ALLOWLIST}:
                continue
            failures.append((target, quote))
    return failures


def report(failures: list[tuple[str, str]]) -> int:
    if not failures:
        print("green: every verbatim quote is present in the corpus.")
        print(f"  corpus: {', '.join(CORPUS)}")
        print(f"  allowlisted (sourced by direct fetch, stated inline): {len(ALLOWLIST)}")
        return 0
    print("RED: verbatim quote not found in the source-verified corpus.\n")
    for target, quote in failures:
        print(f"  {target}")
        print(f'    *"{quote}"*')
        print("    -> either it is a new verbatim (source it and record it in the")
        print("       corpus first), or the wording has drifted from the original.\n")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="inject a fabricated quote and confirm the check goes red",
    )
    args = parser.parse_args()

    if args.self_test:
        fake = "Every line of Go code must be exactly 73 characters long."
        print("self-test: injecting a fabricated verbatim quote --")
        print(f'  *"{fake}"*\n')
        failures = check(TARGETS, extra_quotes=[fake])
        code = report(failures)
        if code == 0:
            print("SELF-TEST FAILED: the fabricated quote passed. The check is decorative.")
            return 1
        print("self-test passed: the fabricated quote was rejected.")
        print("now re-running without it, to confirm the tree is otherwise green --\n")
        return report(check(TARGETS))

    return report(check(TARGETS))


if __name__ == "__main__":
    sys.exit(main())
