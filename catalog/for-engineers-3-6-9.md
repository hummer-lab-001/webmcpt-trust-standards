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
| **9 — The tool** | nine paste-in reviewer prompts | **in progress — 3 of 9 written (TypeScript, JavaScript, HTML/CSS); 6 remaining** |

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

**Status: 2 of 9 blocks written — TypeScript and JavaScript (below). The other
seven are marked `[NOT YET WRITTEN]` per block and will be added one at a time.**

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

### Block order and status

| # | Block | Applies to | Status |
|---|---|---|---|
| 1 | **TypeScript** | `.ts`, `.tsx` | **written below** |
| 2 | **JavaScript** | `.js` | **written below** |
| 3 | **HTML/CSS** | `.html`, `.css` | **written below** |
| 4 | Python | `.py` | `[NOT YET WRITTEN]` |
| 5 | Go | `.go` | `[NOT YET WRITTEN]` |
| 6 | Java | `.java` | `[NOT YET WRITTEN]` |
| 7 | C++ | `.cc`, `.h` | `[NOT YET WRITTEN]` (carry Hook 3's fossil honesty) |
| 8 | C# | `.cs` | `[NOT YET WRITTEN]` |
| 9 | Swift | `.swift` | `[NOT YET WRITTEN]` |

---

### Block 1 — TypeScript (`.ts`, `.tsx`)

Every rule here is drawn from the already-source-verified Web-pack Layer 1 in
`combination-packs.md` (the agreed frontend rules) — **no new verbatim quote
is introduced in this block**, so there is nothing here for the mothership to
re-source; it is a re-cut of quotes already confirmed. Rules are stated in
imperative reviewer form; the underlying wording was marked verbatim at its
first appearance in the packs file.

```text
You are reviewing TypeScript. Apply these rules ONLY to .ts and .tsx files.
Do not extend them to .js, .css, or any other file type. Do not invent rules
beyond this list.

- String literals use single quotes ('...'), not double quotes.
- Every statement ends with an explicit semicolon. Flag any reliance on
  automatic semicolon insertion (ASI).
- Ban `export default`. Require named exports.
- Do NOT enforce an 80-column line limit here: the 80-character limit is a
  JavaScript (.js) rule and Google's TypeScript guide does not state one.
  Flag a reviewer that imports the .js column limit into .ts.
- For any frontend code that could be written in either language, prefer the
  TypeScript rules: Google now directs new frontend code to TypeScript.
```

Scope notes (why each line is safe to enforce, and where it stops):

- **Single quotes / semicolons / named-exports** are the three rules the Web
  pack records as holding across the TS+JS family; they are enforceable
  (a reviewer can check each mechanically) and are not IE-era fossils.
- The **"no 80-column here"** line is included on purpose: the most common way
  this block gets misused is a reviewer carrying JavaScript's 80-column rule
  onto `.ts`. Naming the boundary is the whole point of surface-scoping.
- Nothing about acronym casing, indentation width, or naming case is asserted
  for TypeScript, because the Web pack does not record a *verbatim* TS rule
  for those — and this file does not assert what it cannot source.

> Source: `combination-packs.md` Web-pack Layer 1 and its paste-in block
> (the TS/JS agreed rules, and the L2.2 note that the 80-column limit is
> JavaScript-only). No guide was re-fetched for this block.

---

### Block 2 — JavaScript (`.js`)

JavaScript shares the TypeScript family's agreed rules (quotes, semicolons,
named exports) but — unlike TypeScript — its guide **does** legislate line
length and indentation in its own words. So this block carries two rules the
TypeScript block deliberately omitted, and it is the block that *owns* the
80-column limit the TS block warned against importing.

```text
You are reviewing JavaScript. Apply these rules ONLY to .js files. Do not
extend them to .ts or .tsx (TypeScript is scoped separately). Do not invent
rules beyond this list.

- String literals use single quotes ('...'), not double quotes.
- Every statement ends with an explicit semicolon. Flag any reliance on
  automatic semicolon insertion (ASI).
- Ban `export default`. Require named exports.
- Indent 2 spaces per block; never use tabs.
- Column limit is 80 characters. Any line over 80 must be line-wrapped,
  EXCEPT: module/import/export/require statements, and lines containing a
  URL. This 80-column limit is a JavaScript rule — do NOT apply it to .ts.
- For new frontend code, prefer TypeScript: Google now directs new code there.
```

Scope notes and sourcing:

- **Quotes / semicolons / named exports** are identical to the TypeScript
  block and come from the same already-verified Web-pack Layer 1 — **no new
  verbatim** for these three.
- **Two rules DO introduce verbatim quotes** the mothership should re-source
  (both were already recorded verbatim in `combination-packs.md`, cited here
  so they can be cross-checked against the raw Google JavaScript Style Guide):
  - **80-column limit** — verbatim: *"JavaScript code has a column limit of 80
    characters. Except as noted below, any line that would exceed this limit
    must be line-wrapped."* (exceptions: module/require/import/export lines and
    URLs). Google JavaScript Style Guide, **"Column limit: 80" (§4.4)**.
    Recorded at `combination-packs.md` L1.3 and L2.2.
  - **Indentation** — verbatim: *"Each time a new block or block-like
    construct is opened, the indent increases by two spaces."* and *"Tab
    characters are not used for indentation."* Google JavaScript Style Guide,
    **"Block indentation: +2" (§4.2)**. Recorded at `combination-packs.md` L1.4.
- **Honesty note on the indentation wording:** the *JavaScript* guide's own
  phrasing is *"...the indent increases by two spaces"* — **not** *"Indent by
  2 spaces at a time,"* which is the **HTML/CSS** guide's wording for the same
  practical rule. This block quotes JavaScript's own sentence, not the HTML/CSS
  one, so the attribution stays exact.
- The **§ numbers (§4.2, §4.4) are stated to help the mothership locate the
  passages** in the current Google JavaScript Style Guide; if the live guide's
  numbering differs, the verbatim sentence is the anchor, not the number.

> Source: `combination-packs.md` Web-pack Layer 1 (quotes/semicolons/exports,
> no new verbatim) + L1.3/L1.4/L2.2 (80-column and indentation verbatim).
> No guide was re-fetched by 021 for this block; the two verbatim quotes are
> flagged above for mothership raw-source re-confirmation.

---

### Block 3 — HTML/CSS (`.html`, `.css`)

HTML and CSS are grouped as one block because the Google guide covering them
is itself one document (the HTML/CSS Style Guide) and their quoting rules only
make sense stated against each other — this is the surface where "single
quotes everywhere" (correct for JS/TS/CSS) goes wrong the moment it touches
`.html`. Every rule here is drawn from the already-source-verified Web-pack
Layer 1/1.4 and L2.1 in `combination-packs.md` — **no new verbatim quote is
introduced in this block**.

```text
You are reviewing HTML or CSS. Apply these rules ONLY to .html and .css files.
Do not extend them to .js or .ts. Do not invent rules beyond this list.

- CSS values and attribute selectors use single quotes ('...'), not double.
- HTML attribute values use DOUBLE quotes ("..."). This is the one place in
  the whole stack where single quotes are WRONG — do not apply the JS/TS/CSS
  single-quote rule to HTML attributes.
- Exception inside CSS itself: the @charset at-rule reverts to double quotes,
  even though ordinary CSS values are single-quoted.
- Indent 2 spaces per block; never use tabs or mix tabs and spaces.
- Do NOT enforce a column limit here: the HTML/CSS guide states no line-length
  rule. Flag a reviewer that imports JavaScript's 80-column limit into .html
  or .css.
```

Scope notes and sourcing:

- **Quotes.** CSS values/attribute selectors single, HTML attributes double,
  `@charset` double-again is the exact three-way split recorded at Collision 4
  above and at `combination-packs.md` L2.1 (verbatim on both sides: HTML/CSS
  guide *"Use single ('') rather than double (\"\")..."* for CSS values, and
  *"When quoting attributes values, use double quotation marks."* for HTML
  attributes). No new fetch — this block re-cuts that quote.
- **Indentation.** *"Indent by 2 spaces at a time."* / *"Don't use tabs or mix
  tabs and spaces."* is the HTML/CSS guide's own wording, recorded at
  Collision 5 above and `combination-packs.md` L1.4. (Note the correction
  already logged in Collision 5: this exact sentence belongs to HTML/CSS, not
  JavaScript — the JavaScript block above deliberately quoted JavaScript's own
  §4.2 sentence instead of borrowing this one, to keep attribution exact. This
  block is the one place this sentence is correctly cited.)
- **No column limit.** The Web pack records HTML/CSS as silent on line length
  (`combination-packs.md` L2.2, L1.4) — silence, not a stated exception, so
  the block says "do not enforce" rather than naming a number.
- Nothing about acronym casing or naming case is asserted for HTML/CSS,
  because neither the Web pack nor Collision 1–6 records a verbatim HTML/CSS
  rule for those — this file does not assert what it cannot source.

> Source: `combination-packs.md` L1.4, L2.1, L2.2 (all verbatim already
> confirmed there). No guide was re-fetched by 021 for this block.

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
- Section **9 is in progress**: blocks 1–3 (TypeScript, JavaScript, HTML/CSS)
  are written; blocks 4–9 are each marked `[NOT YET WRITTEN]` in the
  block-status table and will be added one at a time. The TypeScript block
  introduces **no new verbatim**; the JavaScript block re-cuts the same shared
  rules **plus** two verbatim quotes (80-column §4.4, indentation §4.2) that
  were already source-verified in `combination-packs.md` and are flagged there
  for re-confirmation. The HTML/CSS block also introduces **no new verbatim**
  — it re-cuts the quoting (single/double/@charset) and indentation quotes
  already confirmed at Collisions 4–5 and `combination-packs.md` L1.4/L2.1.
  Do not treat the six pending blocks as finished.
- One honesty correction made while writing 6: **Go's indentation is recorded
  as a guide *silence* plus a `gofmt` tooling note — not as a quoted rule.**
  Presenting "Go mandates tabs" as a third quoted camp would over-claim.
- Counts (3 / 6 / 9) are a *presentation ladder*, not a claim of completeness
  — they are chosen for impact, not because the corpus contains exactly that
  many findings.
