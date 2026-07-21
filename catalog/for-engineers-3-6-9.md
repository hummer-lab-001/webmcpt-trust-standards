# For Engineers — the 3 / 6 / 9 that a working programmer actually wants

This file is a **different axis** from `catalog/combination-packs.md`. The
packs there are organized by a *reviewer's surface* (a Web change, a Product
change, an Enterprise change). This file is organized by **what makes an
engineer stop scrolling** — the three things, then six, then nine, that a
person who writes code every day reads and thinks "I want this / I've felt
this / I can use this today."

Same eighteen guides. No new guides were read to build this file — it re-cuts
the material already read and already verified in
`catalog/language-style-guide-patterns.md` and `catalog/combination-packs.md`.
Every claim below is cross-referenced to where it was first established there,
so nothing here is a fresh unverified assertion.

## Design — a staircase of escalating impact

The mothership frame is **surprise → necessity → novelty**. This file maps
that onto an engineer's *behavior*:

- **3 = the hook (surprise → they share).** "Google contradicts itself" is
  the most screenshot-able thing in the whole corpus. It kills cargo-culting
  in one image. This is the step an engineer forwards.
- **6 = the empathy (necessity → they trust).** "One house lint rule can't
  hold across a stack" is a pain a full-stack engineer has actually felt. The
  three hooks plus three lived annoyances. This is the step that makes them
  believe the file understands their job.
- **9 = the tool (novelty → they adopt).** Nine paste-in reviewer prompt
  blocks, one per language, surface-scoped so they don't misfire. This is the
  step that turns a reader into a user.

Each step's reason for landing is *different from the one before it* and
*builds on it*: you share it, then you feel seen by it, then you use it.

**Build status of this file (stated honestly, up front):**

| Step | What it is | Status |
|---|---|---|
| **3 — The hook** | Google's three self-contradictions | **written below, source-checked both sides** |
| **6 — The empathy** | + three cross-stack lint collisions | **structure only — body NOT YET WRITTEN** |
| **9 — The tool** | nine paste-in reviewer prompts | **structure only — body NOT YET WRITTEN** |

The 6 and 9 sections below are headings and intended content only. Where a
section says **`[NOT YET WRITTEN]`**, it means exactly that — do not read the
absence of a body as "nothing to say there." The material exists (it is
already verified in the combination-packs file); it has simply not been
composed into this file's form yet.

---

## 3 — The hook: three places Google's own style guides contradict each other

Why this is the share-step: "Google says so" is a cargo-cult argument. The
fastest way to end that argument is Google's own published guides disagreeing
with each other, in writing. All three contradictions below were confirmed
**from raw source text on every side that is quoted** — the point of a
contradiction is lost if one side is a paraphrase the reader can't trust, so
these are verbatim on both sides. (First established in
`combination-packs.md`; see the cross-refs.)

### Hook 1 — The *same identifier* is spelled two opposite ways

An acronym inside a name. Two Google guides legislate it, in exactly opposite
directions.

- **Go — preserve the acronym's case** (verbatim): *"Words in names that are
  initialisms or acronyms (e.g., `URL` and `NATO`) should have the same
  case."* → "new customer ID" becomes **`newCustomerID`**.
- **Java — fold the acronym into an ordinary word** (verbatim): *"Now
  lowercase everything (including acronyms), then uppercase only the first
  character of:"* each word. → the same name becomes **`newCustomerId`**.

Same concept, same company's guides, opposite spelling: Go `newCustomerID`,
Java `newCustomerId`.

**The honest scope** (this is the part most roundups get wrong): this is not
"Go vs everyone symmetrically." Reading all eighteen, **Go is the lone
outlier** — it is the only guide that says *preserve* the initialism case;
Java, C++ (*"prefer to capitalize it as a single \"word\", e.g., `StartRpc()`
rather than `StartRPC()`"*), C#, and the XML guide (`informationUri`) all
**fold**. So the accurate headline is "Go alone preserves; every other guide
that states an acronym rule folds," not "the guides are evenly split." Stating
it the symmetric way would be a more dramatic tweet and a false one.

> Cross-ref: `combination-packs.md` L2.1 (Product pack) and L2.2 (Enterprise
> pack), where both sides are re-confirmed from raw source.

### Hook 2 — The maximum line length has three different answers

Not two camps — three.

- **80 camp** (verbatim): JavaScript *"JavaScript code has a column limit of
  80 characters."*; Python *"Maximum line length is 80 characters."*; C++
  *"Each line of text in your code should be at most 80 characters long."*
- **100 camp** (verbatim): Java *"Java code has a column limit of 100
  characters."*; C# *"Column limit: 100."*; Swift *"Swift code has a column
  limit of 100 characters."*; Objective-C also votes 100.
- **No-limit camp** (verbatim): Go *"There is no fixed line length for Go
  source code."*

So a reviewer literally cannot pick one column limit that is correct for a
change spanning `.py`, `.java`, and `.go`: 80 is wrong for Java, 100 is wrong
for Python, and any hard number is wrong for Go.

**The honest scope:** the 80-vs-100 split is not one guide's quirk — it lines
up cleanly (older/systems-leaning guides at 80, the Java-family at 100), and
that lineup is corroborated across the pack, not resting on any single guide.

> Cross-ref: `combination-packs.md` L1.3, L2.2 (Product) and L2.1 (Enterprise).

### Hook 3 — "How do you report an error" has four incompatible answers

- **C++ — no exceptions at all** (verbatim): *"We do not use C++
  exceptions."* Errors travel through return values.
- **Go — return values, explicitly** (no exceptions): an error is a value you
  must handle, returned alongside the result.
- **Java / C# / Swift — exceptions** are the mechanism.
- **Python — exceptions, but bare `except` is banned.**

These guides agree on the *goal* — do not let failures pass silently — and
reach it by **mutually incompatible means**. A house rule like "never catch a
broad exception" is meaningful in Python and Java, meaningless in Go (no
exceptions to catch), and forbidden-by-a-different-rule in C++.

**The honest scope — and a fossil flag:** the C++ ban is *not* a timeless
"exceptions are bad" claim. The guide's *"We do not use C++ exceptions"* is
justified by existing Google C++ code being exception-unsafe — a
legacy-consistency reason, not a universal one. Reported honestly, this is a
dated rationale, not eternal wisdom. (That is exactly the "obey the reason,
not the authority" layer.)

> Cross-ref: `combination-packs.md` L2.3 / Fossil note (Enterprise pack),
> lines around the "We do not use C++ exceptions" quote.

**Why an engineer shares this:** it's a single screenshot that ends a category
of pointless review arguments ("because Google does it"). It respects the
reader by showing the seams instead of averaging them away.

---

## 6 — The empathy: one house lint rule can't cross the stack — six times it breaks

**Status: `[NOT YET WRITTEN]` — structure and sourcing plan only.**

Why this is the trust-step: a full-stack engineer has *lived* the moment a
repo-wide lint rule fires a false violation the instant a change touches a
second language. This section = the three hooks above (which are also
cross-stack collisions) **plus three more lived annoyances**, each framed as
"the moment it bites you in review."

Intended six entries (all already verified in `combination-packs.md`; bodies
to be composed here):

1. **Acronym casing** — (Hook 1) `newCustomerID` vs `newCustomerId` across
   `.go`/`.java`.
2. **Line length** — (Hook 2) an 80-col lint rule flags every Java file; a Go
   file has no limit to enforce.
3. **Error mechanism** — (Hook 3) a "no broad catch" rule is meaningless in
   Go.
4. **Quote style** — `[NOT YET WRITTEN]` — JS/TS/CSS use **single** quotes
   (verbatim, JS: *"...single quotes (`'`), rather than double quotes
   (`"`)."*); **HTML attributes use double quotes**; and the CSS `@charset`
   at-rule reverts to double quotes. One repo-wide quote lint necessarily
   violates one surface. (Source: `combination-packs.md` L2.1 Web,
   lines ~109–178.)
5. **Indentation** — `[NOT YET WRITTEN]` — 2-space camp (JS/HTML/CSS/Java,
   verbatim *"Tab characters are not used..."*) vs **Python 4 spaces**
   (verbatim *"Indent your code blocks with 4 spaces. Never use tabs."*) vs
   **Go/gofmt tabs**. A single indent rule breaks at least one. (Source:
   `combination-packs.md` L1.4 Web, L2.3 Product.)
6. **Naming case** — `[NOT YET WRITTEN]` — `camelCase` (Java/JS/Go/…) vs
   `snake_case` (Python) at the language boundary. (Source:
   `language-style-guide-patterns.md` naming sections.)

**The one-line thesis this section will argue:** *a reviewer (human or AI) who
enforces one house style across an entire stack will be wrong somewhere on
every multi-language change — and can name exactly where.*

---

## 9 — The tool: nine paste-in reviewer prompt blocks, one per language

**Status: `[NOT YET WRITTEN]` — structure and constraints only.**

Why this is the adopt-step: it is the immediate, selfish payoff. Nine blocks,
each the single most important, least-ambiguous rules for that language,
written so an engineer can paste one straight into a Claude or Copilot system
prompt for their next review — *today*.

Planned nine (languages already read): **TypeScript · JavaScript · HTML/CSS ·
Python · Go · Java · C++ · C# · Swift.**

Hard constraints each block must satisfy when written:

- **Surface-scoped.** Every block must name the file types it applies to
  (e.g. "apply only to `.py`") so it is never misapplied to a sibling
  language — the failure mode this whole file is warning about.
- **Verbatim-or-marked.** Any rule stated as the guide's own wording is
  marked verbatim; anything condensed is marked paraphrase. No rule is
  asserted stronger than its source.
- **Only what is genuinely enforceable** goes in — no aspirational fluff that
  a reviewer can't check.
- Each block is derived from the already-verified Layer-1 material in
  `combination-packs.md`, not re-invented.

> Note on honest scope for the eventual C++ block: Google's C++ guide is
> reachable but its rationale is frequently dated (see Hook 3). The block will
> carry rules that still hold and flag the legacy-only ones — it will not
> pretend the 2019-era reasons are timeless.

---

## Honesty ledger for this file

- No new guides were read; still eighteen. This file re-cuts verified
  material on a new (engineer-facing) axis.
- Section **3 is complete** and source-checked on every quoted side.
- Sections **6 and 9 are deliberately unfinished** and say so at every body;
  their sourcing is mapped but the prose is not written. Do not treat the
  headings as finished content.
- Counts (3 / 6 / 9) are a *presentation ladder*, not a claim of completeness
  — they are chosen for impact, not because the corpus contains exactly that
  many findings.
