---
name: c4-selection-criteria
description: Evaluates whether a GitHub repository qualifies as "c4" — a production-proven exemplar codebase (as opposed to educational-only code) — using a 6-axis license/production/quality/governance/maintenance/reputation checklist. Use when the user asks to assess, vet, or register a repository as a reference-quality/exemplar codebase, when comparing a candidate repo's license risk before reuse, or when asked "is this repo good enough to use as a model implementation?"
license: MIT
metadata:
  version: "1.0"
---

# c4 Selection Criteria — Production-Grade Exemplar Codebase Check

## When to use this

Apply this when deciding whether a repository is trustworthy enough to cite
as a **model implementation** (not a tutorial/toy example). "c4" is this
catalog's shorthand for "code shaped by real production demands," as opposed
to educational-only or curated-list collections (which our internal taxonomy
files under other tiers). Star count alone never qualifies a repo — it
measures fame, not quality or maintainability.

## The 6 axes (all must be checked; not all must pass)

Each axis returns one of: **★ (confirmed, primary source)** / **☆ (confirmed,
secondary source)** / **◇ (unconfirmed — not "false", just not yet verified)**.
Never write "no evidence" as if it proves absence — see Pitfall 1 below.

### Axis 0 — License Check (gate; check this FIRST)
Question: Is the license one that permits lightweight reuse-with-attribution
(MIT / Apache-2.0 / BSD / similar)?
- If GitHub shows `Other` or an unfamiliar name, **read the LICENSE file
  text yourself** — do not trust the platform's auto-detected label.
- See `references/license-types.md` for the six known non-obvious patterns
  (dual license, multi-author academic BSD, core/periphery split, etc.)
  and how each resolves.
- **Real restrictions found (SSPL / RSAL / BSL / Commons Clause / AGPL-core
  paired with our reuse model) → stop here, do not proceed to axis 1.**
  Record as a considered-and-declined entry, not a silent skip.

### Axis 1 — Production Proof
Question: Does a named company/service publicly state, in its own words,
that it runs this in production (official blog, case-study page, conference
talk, or the project's own "who uses this" page)?
- A vendor's own case-study page counts as primary (★).
- An aggregator's summary of someone else's talk counts as secondary (☆) —
  go find the original before upgrading to ★.
- "Widely known to be popular" is NOT production proof. Investment/funding
  announcements are NOT adoption proof — they are a different claim.

### Axis 2 — Quality Gate Evidence
Question: Do CI, test coverage, and lint/static-analysis configs actually
exist in the repo, and is the default branch currently green?
- Prefer finding this in CONTRIBUTING.md or a workflows directory over
  inferring it from reputation.

### Axis 3 — Governance Document Depth
Question: Do CONTRIBUTING.md / GOVERNANCE.md / equivalent cover at least
4 of these 6: required commands, test policy, code structure, code style,
git workflow, explicit boundaries/prohibitions?
- If the docs point to a separate "detail lives elsewhere" repo, follow the
  link — but if that link chains to yet another pointer with no real
  content, score it as **weak**, not as "presumably fine because it says
  so." Do not grant the benefit of the doubt past what you actually read.

### Axis 4 — Maintenance Continuity
Question: Has a maintainer (not just outside contributors) committed or
merged within roughly the last 90 days? Is the issue/PR backlog proportional
to project size, not abandoned?

### Axis 5 — Reference Reputation
Question: Has an independent third party — a textbook, a university course,
a journal paper, another company's engineering blog — cited this as a model
implementation?
- A journal/peer-reviewed citation (Nature, Science Robotics, etc.) is the
  strongest form seen so far.
- High mention volume alone does not substitute for axes 1–4.

## Verdict

Score = count of axes at ★/☆ out of 6 (axis 0 is pass/fail, not counted
in the /5 or /6 score once passed).
- **5–6/6 confirmed** → register as a strong c4 candidate.
- **3–4/6, rest ◇** → register as a conditional/provisional candidate;
  name the specific axes still open, do not round up.
- **Axis 0 fails** → do not register; record as a considered-and-declined
  entry with the specific license clause that disqualified it.

## Two pitfalls this criteria set exists to prevent

1. **"I couldn't confirm it" is not "it doesn't exist."** Mark unconfirmed
   axes ◇ and revisit later — don't silently treat a gap as a negative
   finding. Re-checking has repeatedly turned ◇ into ★ within the same day.
2. **Don't trust a platform's own label at face value.** GitHub's license
   auto-detection and a page's rendered file list can both be wrong or
   incomplete — verify the underlying primary source (the LICENSE file
   text itself, the vendor's own case-study page) before scoring an axis.

## Further detail

- `references/license-types.md` — the six license patterns that don't
  resolve to a simple yes/no at a glance, with a worked example for each.
