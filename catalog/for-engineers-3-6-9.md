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
| **6 — The empathy** | + three cross-stack lint collisions | **written below, source-checked both sides** |
| **9 — The tool** | nine paste-in reviewer prompts | **structure only — body NOT YET WRITTEN** |

The 9 section below is headings and intended content only. Where it says
**`[NOT YET WRITTEN]`**, it means exactly that — do not read the absence of a
body as "nothing to say there." The material exists (it is already verified in
the combination-packs file); it has simply not been composed into this file's
form yet. Sections 3 and 6 are written and source-checked.

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

Why this is the trust-step: a full-stack engineer has *lived* the moment a
repo-wide lint rule fires a false violation the instant a change touches a
second language. This section is the three hooks above (which are already
cross-stack collisions) **plus three more that bite in everyday review** —
quotes, indentation, naming. Each is framed as "the moment it fires on you."

The thesis, stated once, up front: **a reviewer (human or AI) that enforces
one house style across an entire stack will be wrong somewhere on every
multi-language change — and this section names exactly where.**

**Collisions 1–3 — the hooks, now read as lint failures:**

1. **Acronym casing.** An acronym-fold lint rule (`newCustomerId`) rewrites
   correct Go (`newCustomerID`) into a Go-guide violation; an acronym-preserve
   rule does the reverse to Java. Fires on any `.go` + `.java` change. (Hook 1.)
2. **Line length.** An 80-column rule flags nearly every `.java` file (its
   guide says 100); a 100-column rule under-enforces `.py` (its guide says
   80); and *no* fixed number is correct for `.go` (its guide sets none).
   (Hook 2.)
3. **Error handling.** A "never catch a broad exception" rule is enforceable
   in Python and Java, **meaningless in Go** (no exceptions to catch), and
   redundant in C++ (exceptions already banned). The rule can't even *parse*
   across the stack. (Hook 3.)

**Collision 4 — quote style: single everywhere, except where it's flatly wrong.**

- JavaScript / TypeScript / CSS → **single quotes** (verbatim, JS guide):
  *"...single quotes (`'`), rather than double quotes (`"`)."* CSS likewise
  uses single quotes for attribute selectors and property values.
- HTML attributes → **double quotes** (verbatim, HTML/CSS guide): *"When
  quoting attributes values, use double quotation marks."*
- And a twist the guide names on itself: the CSS **`@charset`** at-rule
  reverts to double quotes.

So a repo-wide "prefer single quotes" lint is *correct* for the `.js`/`.ts`/
`.css` in a change and *wrong* for the `.html` in the same change. This is not
taste — the HTML double-quote rule is about attribute-value parsing, so
normalizing everything to single quotes fights the HTML guide directly.

> Cross-ref: `combination-packs.md` L2.1 (Web pack).

**Collision 5 — indentation: 2 spaces, 4 spaces, or "the guide doesn't say."**

- **2 spaces, no tabs** (verbatim): JavaScript, HTML/CSS (*"Indent by 2
  spaces at a time."*), and **Java** (*"Tab characters are not used for
  indentation."*).
- **4 spaces, no tabs** (verbatim, Python guide): *"Indent your code blocks
  with 4 spaces. Never use tabs."*
- **Go — no quoted rule.** This is the honest part: the Go guide's Decisions
  page **states no indent width or tabs-vs-spaces rule at all**. "Go uses
  tabs" is true, but it is **`gofmt`'s behavior**, not a rule asserted in the
  guide text. So Go belongs here as a *silence with a tooling caveat*, not as
  a third quoted camp. Stating it as "the Go guide mandates tabs" would be the
  exact over-claim this whole file exists to avoid.

A single indent rule (say "2 spaces") is a verbatim violation of the Python
guide and, for Go, enforces something the guide never wrote (though `gofmt`
will fight you anyway).

> Cross-ref: `combination-packs.md` L1.4 (Web), L2.3 (Product) — including the
> recorded distinction that Go's tabs are gofmt behavior, not a quoted rule.

**Collision 6 — naming: `lowerCamelCase` vs `lower_with_under` at the boundary.**

Both sides confirmed verbatim from raw source (Python §3.16 and Java §5.2
were re-checked against the published guides for this file, in the same way
the Java §5.3 acronym quote in Hook 1 was independently confirmed — they were
not carried over from the earlier corpus, which does not record either
guide's naming table):

- **Java** (verbatim, Google Java Style Guide §5.2): *"Method names are
  written in lowerCamelCase."* / *"Local variable names are written in
  lowerCamelCase."*
- **Python** (verbatim, Google Python Style Guide §3.16): functions and
  variables use `lower_with_under()` — the guide's summary table gives
  `function_name`, `local_var_name`, and states *"Use CapWords for class
  names, but lower\_with\_under.py for module names."*

So the *same* function — say, one that parses a customer record — is
`parseCustomerRecord` in Java and `parse_customer_record` in Python. A
repo-wide "functions are camelCase" lint rule is a straight violation of the
Google Python guide on every `.py` file it touches. (A third guide, XML,
also mandates lowerCamelCase verbatim — *"All names MUST use
lowerCamelCase."* — so the camel side is not one language's quirk.)

> Sourcing note: Python §3.16 and Java §5.2 were verified by fetching the
> published guides directly while writing this section. The prior corpus
> (`language-style-guide-patterns.md`) did **not** contain a Python or Java
> naming-table quote; this entry does not lean on material it doesn't have.

**What an engineer feels reading this:** "I have hit every one of these." That
recognition is the trust the 9-section then converts into use.

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
  material on a new (engineer-facing) axis. The two *fresh* raw-source checks
  done for this file (Java §5.3 acronym-fold, Java §5.2 and Python §3.16
  naming) re-confirm rules from guides already among the eighteen — they add
  no nineteenth guide.
- Sections **3 and 6 are complete** and source-checked on every quoted side;
  where a claim was not already in the prior corpus (the naming tables), the
  guide was fetched and the quote confirmed, and that is stated inline.
- Section **9 is deliberately unfinished** and says `[NOT YET WRITTEN]` in its
  body; its sourcing is mapped but the prose is not written. Do not treat the
  heading as finished content.
- One honesty correction made while writing 6: **Go's indentation is recorded
  as a guide *silence* plus a `gofmt` tooling note — not as a quoted rule.**
  Presenting "Go mandates tabs" as a third quoted camp would over-claim.
- Counts (3 / 6 / 9) are a *presentation ladder*, not a claim of completeness
  — they are chosen for impact, not because the corpus contains exactly that
  many findings.
