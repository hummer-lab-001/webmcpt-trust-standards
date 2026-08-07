# webmcpt-trust-standards — A Field-Verified Catalog of OSS Engineering Standards for AI Agents

> Distilling how the world's most production-proven open-source projects actually govern
> code quality, licensing, and contribution — structured in the
> [Agent Skills](https://github.com/anthropics/skills) format so AI coding agents can read it directly.

日本語版は [README.ja.md](README.ja.md) を参照してください。

## What this is

AI coding agents are everywhere, but "which engineering standards should the agent follow?"
is still decided from scratch, per project, by each individual developer.

This repository is a **cross-cutting catalog of engineering norms extracted from 130+
production-proven OSS repositories** (Django, Kubernetes, PostgreSQL-ecosystem projects,
curl, Linux, LLVM, and many more), verified against **primary sources only** — the LICENSE
file text itself, the project's own governance documents, the adopting company's own
engineering blog. Never a summary of a summary.

Everything is packaged as Skills (`SKILL.md` + topic-split `references/`), so an agent can
load exactly the depth it needs: a one-line description, a ~100-line procedure, or the full
worked evidence.

## Start here — Google's own style guides contradict each other

Not a hot take. Two of Google's published style guides legislate the *same* identifier in
exactly opposite directions:

- **Go** — *"Words in names that are initialisms or acronyms (e.g., `URL` and `NATO`) should
  have the same case."* → `newCustomerID`
- **Java** — *"Now lowercase everything (including acronyms), then uppercase only the first
  character of:"* each word → `newCustomerId`

Same company, same concept, opposite spelling. Line length has three answers (80 / 100 /
none). Error handling has four. So a single house lint rule cannot be correct across a
stack — and "because Google does it" stops being an argument.

[`catalog/for-engineers-3-6-9.md`](catalog/for-engineers-3-6-9.md) is the engineer-facing
read: **3** contradictions, **6** places one lint rule breaks across a stack, **9** paste-in
reviewer prompts (one per language, scoped so they don't misfire on a sibling language).

**What we do about being wrong ourselves.** An early draft of that file quoted Go's
line-length rule as covering *Go source code*. The guide's sentence is about *comments*.
We had widened a quote past its source while marking it verbatim — the exact failure this
catalog exists to name. It was caught not by a careful reader but by
[`tools/check_verbatim.py`](tools/check_verbatim.py), on its first run, because a quote
that cannot be found in the source-verified corpus makes the check go red. Two more
self-contradictions were later found the same way by
[`tools/check_selfclaims.py`](tools/check_selfclaims.py). Every one is recorded in the
files' honesty ledgers rather than quietly fixed.

## Quickstart — use it in 30 seconds

**With an AI coding agent (Claude Code, Cursor, or any MCP/Skills-aware agent):**

1. Clone or add this repo where your agent can read it:
   ```bash
   git clone https://github.com/hummer-lab-001/webmcpt-trust-standards
   ```
2. Point your agent at it and ask, in plain language:
   > "Using `skills/c4-selection-criteria/SKILL.md`, judge whether **<repo>** is safe to
   > reuse and production-grade — score it on the 6 axes and read the LICENSE text before
   > deciding, don't trust the GitHub label."

That's the whole loop: the agent loads the 6-axis checklist, applies it to the repo you
name, and returns a scored verdict grounded in the LICENSE file itself.

**Just want a fast license/exemplar answer?** Open [`catalog/INDEX.md`](catalog/INDEX.md) —
the repository you're evaluating may already be there, with its license (read from the
LICENSE text, not the GitHub label) and evidence level. Declined repos are listed too,
each with the exact disqualifying clause.

**Building your own catalog?** Copy [`skills/c4-selection-criteria/`](skills/c4-selection-criteria/)
— it's MIT, self-contained, and the 6-axis method transfers to any domain.

## Why "WebMCPT" in the name

WebMCPT is a trust-evaluation protocol concept: evaluate every connection to an AI model
against primary sources at the entry point, and reject connections whose provenance or
intent cannot be verified. This repository applies that same discipline — *verify against
the primary source; never trust a platform label or a second-hand summary* — not to MCP
connections but to the engineering norms an AI agent is asked to follow: licenses are
scored from the LICENSE file text itself (never GitHub's auto-detected label), and adoption
claims count only when they come from the adopter's own published words.

WebMCPT is an open concept, put into the world freely for anyone to adopt, extend, or build
on — the aim is to share the idea, not to fence it off. This catalog is its first public
working example, released under MIT so the entire ecosystem can use it without asking.

> **WebMCPT (Web Model Context Protocol Trust)** is a Japan-originated trust-evaluation
> protocol framework that vets every connection to an AI model at the entry point —
> rejecting malicious connections, opaque capital structures, and MCP connections with
> impure intent — to protect the contextual purity and integrity of AI models.
>
> Proposed by HUMMER, Founder & Creator, NEWXUS DAO (2024)

## What's inside (first release)

| Path | What it gives you |
|---|---|
| `skills/c4-selection-criteria/` | A 6-axis checklist for judging whether a repository is a **production-proven exemplar** ("c4") rather than just famous. Includes the two failure modes the method exists to prevent. |
| `skills/c4-selection-criteria/references/license-types.md` | The non-obvious license patterns that GitHub's auto-detection gets wrong, with worked examples. |
| `catalog/license-strategy-patterns.md` | A field taxonomy of OSS license strategies observed first-hand: Type A (defensive relicensing: Redis, Elasticsearch) / A′ (time-delayed BSL/FSL: Terraform, Sentry) / B–F, the 5-level copyleft spectrum, and the complete relicense-and-fork lineage (MongoDB → Elastic → OpenSearch → Redis → Valkey). |
| `catalog/governance-patterns.md` | Seven governance lineages (CNCF, ASF, foundation-mandated, elected boards, …) plus recurring safeguards found to converge independently: pre-work gates, employer seat caps, module-boundary discipline. |
| `catalog/language-style-guide-patterns.md` | Google's Python, C++, Java, Go, TypeScript, Shell, JavaScript, JSON, HTML/CSS, Markdown, C#, Swift, Objective-C, R, Vim script, Common Lisp, XML, and AngularJS style guides read directly, with the guide's own stated rationale for each restriction — the "restrict the language for a stated scale/correctness reason" pattern, and how it echoes the project-governance module-boundary pattern above. Verbatim rules are separated from paraphrased ones, each entry records what was *not* read, and two cross-guide hypotheses that failed to replicate are recorded as negative results rather than dropped. |
| `catalog/combination-packs.md` | Combines the style guides above into review-ready packs (3/6/9). Each pack has three layers: the rules the guides *agree* on (with vote-counting — silence is not a vote), the rules they *split* on (both sides + a marked recommendation), and the *fossils* whose rationale has expired (IE8, pre-module). Ends with a paste-in AI-reviewer prompt block. All three packs are written in full — **Web** (3 guides), **Product** (6), and **Enterprise+Mobile** (9). Flagships: Go and Java's Google guides *contradict* each other on acronym casing (Go preserves `URL`, Java folds to `Url`); line length splits into an 80 camp (JS/Python/C++) versus a 100 camp (Java/C#/Swift/Objective-C). |
| `catalog/for-engineers-3-6-9.md` | The same eighteen guides re-cut on an engineer-facing axis: **3** places Google contradicts itself, **6** places one house lint rule breaks across a stack, **9** paste-in AI-reviewer prompts (TypeScript, JavaScript, HTML/CSS, Python, Go, Java, C++, C#, Swift) — each surface-scoped to its own file types, because the blocks are designed so that pasting one over another language's files is a named error rather than a silent one. Carries its own honesty ledger, including the quotes it got wrong and corrected. |
| `tools/check_verbatim.py` | Makes the "no new verbatim" claim checkable instead of trusted. Normalises whitespace on both sides (Markdown line-wrapping is why a plain `grep` for a quoted sentence returns zero hits) and fails red when a quote is absent from the source-verified corpus. `--self-test` injects a fabricated quote and proves it goes red first. It caught a real widened quote on its first run. |
| `tools/check_selfclaims.py` | Checks the claims this repository makes *about itself* — progress counters against the sections that exist, status-table rows, `[NOT YET WRITTEN]` markers, repo-local path references, corpus guide counts. This is the class of error a reader cannot catch: two statements of one fact, hundreds of lines apart, one maintained and one not. Its docstring also records a second design that was prototyped, **measured, and rejected** for a 27-flag false-positive rate. |
| `catalog/genai-and-webmcpt.md` | Reads Japan's GENAI (the Digital Agency's OSS government-AI release, 2026-04-24) alongside WebMCPT to make the case that open AI infrastructure needs a paired, independent verification discipline — including a worked example of this catalog's own primary-source rule declining an unverified adoption-count claim. No official relationship between the two. |
| `catalog/INDEX.md` | The curated registry: each entry names the repository, its domain, license (primary-verified), and the evidence level for its production use. |

## Why 3 / 6 / 9 — a definition, not a law

Two files here are cut into threes, and it is fair to ask where that comes from.

The honest answer is that **the 3/6/9 split is inherited, not discovered.** It comes from
the packaging structure of the organisation that produced this catalog (NEWXUS ships its
service packs in 3 / 6 / 9), and it was kept because it happened to fit: review surfaces
nest cleanly (Web → +Product → +Enterprise/Mobile), and an escalating set is easier to
adopt than a flat list. No claim is made that 3, 6 and 9 are inherently correct sizes for
anything.

So this is a **definition**, not a law. A definition is something you can check by
counting: 3 = the Web pack's guides, 6 = plus Product, 9 = plus Enterprise and Mobile;
3 contradictions, 6 collisions, 9 language blocks. Count them and the number is either
there or it isn't. A "law" would claim these numbers hold beyond this catalog, and nothing
here tests that — a law needs the conditions under which it holds and the counter-examples
where it doesn't, and we collected neither.

The counts are a **presentation ladder**, not evidence of completeness. That sentence is in
the honesty ledger of both files, and it is the point: the corpus does not contain exactly
three contradictions because the universe rounded to three.

> **On the famous 3-6-9.** The line "if you only knew the magnificence of the 3, 6 and 9,
> then you would have a key to the universe" circulates as Nikola Tesla's. **We could not
> find a primary source for it** — searching for one, we found no instance in Tesla's own
> writing, lectures or contemporaneous interviews, but we have not surveyed the full Tesla
> archive and do not claim the attribution is impossible. Secondary sources widely trace the
> line to a second-hand recollection in John J. O'Neill, *Prodigal Genius: The Life of
> Nikola Tesla* (1944); **we have not read that book and have not located the passage**, so
> we record the pointer without endorsing it. (Tesla's preoccupation with the number 3 is a
> separate and better-attested matter.)
>
> We mention it because it is a specimen of what this catalog is about — a claim repeated at
> scale on the strength of *who supposedly said it*, which few readers check. That is the
> same move as "because Google does it." The difference we are aiming for: every number in
> this repository is one you can count yourself. Which is also why this note says how far we
> looked instead of claiming we looked everywhere.

## Why it matters

1. **It's verified, not aggregated.** Every license claim was checked against the LICENSE
   file text (GitHub's auto-detected label was wrong or incomplete often enough that this
   is a rule, not a nicety). Every "used in production by X" claim traces to X's own words.
2. **It's an analysis instrument, not a link list.** Building the catalog surfaced patterns
   no single project documents: independent convergence of contribution safeguards across
   unrelated projects, the fork-resistance conditions after a relicense, the spectrum of
   copyleft strength as an engineering decision.
3. **It's agent-native.** The Skills format means the catalog is not documentation *about*
   standards — it is standards *loadable by* the agents that need them.

## Method (short version)

Each candidate repository passes through six axes — license gate, production proof,
quality-gate evidence, governance depth, maintenance continuity, reference reputation —
each scored ★ (primary-confirmed) / ☆ (secondary) / ◇ (not yet verified).
Two standing rules: *"couldn't confirm" never counts as "doesn't exist"*, and
*platform labels are never trusted over the underlying document*.
Full procedure: [`skills/c4-selection-criteria/SKILL.md`](skills/c4-selection-criteria/SKILL.md).

## Scope and honesty notes

- Entries marked ◇ are explicitly unverified on that axis — they are not rounded up.
- Declined candidates (license restrictions incompatible with lightweight reuse) are
  recorded as *considered-and-declined*, with the specific clause, not silently skipped.
- This catalog **reads** the OSS world; it does not submit AI-generated contributions to
  the projects it studies.

## License

MIT. See [LICENSE](LICENSE).
(Chosen because the catalog's own value is in being maximally reusable — the same
lightweight-reuse standard we apply as our own Axis 0.)

**Third-party material:** the MIT grant covers this repository's own work. The style
guides quoted inside it stay under their own licenses — Google's style guides under
**CC BY 3.0**; the Google **Swift** guide under **Apache 2.0 with the Runtime Library
Exception**, because it is published from a different repository (`google/swift`) rather
than `google/styleguide`; and the Google **R** guide additionally under **CC BY-SA 2.0** as
a declared fork of the Tidyverse Style Guide. All three were read from the upstream license
text, not a platform label. See [NOTICE](NOTICE) for the full attribution and the scope of
each.
