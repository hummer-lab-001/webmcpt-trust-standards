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
> Proposed by HUMMER, Founder, NEWXUS DAO (2024)

## What's inside (first release)

| Path | What it gives you |
|---|---|
| `skills/c4-selection-criteria/` | A 6-axis checklist for judging whether a repository is a **production-proven exemplar** ("c4") rather than just famous. Includes the two failure modes the method exists to prevent. |
| `skills/c4-selection-criteria/references/license-types.md` | The non-obvious license patterns that GitHub's auto-detection gets wrong, with worked examples. |
| `catalog/license-strategy-patterns.md` | A field taxonomy of OSS license strategies observed first-hand: Type A (defensive relicensing: Redis, Elasticsearch) / A′ (time-delayed BSL/FSL: Terraform, Sentry) / B–F, the 5-level copyleft spectrum, and the complete relicense-and-fork lineage (MongoDB → Elastic → OpenSearch → Redis → Valkey). |
| `catalog/governance-patterns.md` | Seven governance lineages (CNCF, ASF, foundation-mandated, elected boards, …) plus recurring safeguards found to converge independently: pre-work gates, employer seat caps, module-boundary discipline. |
| `catalog/language-style-guide-patterns.md` | Google's Python, C++, Java, Go, TypeScript, Shell, JavaScript, JSON, HTML/CSS, Markdown, C#, Swift, Objective-C, R, Vim script, Common Lisp, XML, and AngularJS style guides read directly, with the guide's own stated rationale for each restriction — the "restrict the language for a stated scale/correctness reason" pattern, and how it echoes the project-governance module-boundary pattern above. Verbatim rules are separated from paraphrased ones, each entry records what was *not* read, and two cross-guide hypotheses that failed to replicate are recorded as negative results rather than dropped. |
| `catalog/combination-packs.md` | Combines the style guides above into review-ready packs (3/6/9). Each pack has three layers: the rules the guides *agree* on (with vote-counting — silence is not a vote), the rules they *split* on (both sides + a marked recommendation), and the *fossils* whose rationale has expired (IE8, pre-module). Ends with a paste-in AI-reviewer prompt block. The **Web pack** (3 guides) and **Product pack** (6 guides — its flagship: Go and Java's Google guides *contradict* each other on acronym casing) are written in full; the 9-guide pack is composition-only, explicitly marked not-yet-written. |
| `catalog/genai-and-webmcpt.md` | Reads Japan's GENAI (the Digital Agency's OSS government-AI release, 2026-04-24) alongside WebMCPT to make the case that open AI infrastructure needs a paired, independent verification discipline — including a worked example of this catalog's own primary-source rule declining an unverified adoption-count claim. No official relationship between the two. |
| `catalog/INDEX.md` | The curated registry: each entry names the repository, its domain, license (primary-verified), and the evidence level for its production use. |

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
