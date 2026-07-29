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
| **9 — The tool** | nine paste-in reviewer prompts | **in progress — 6 of 9 written (TypeScript, JavaScript, HTML/CSS, Python, Go, Java); 3 remaining** |

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
- **No-limit camp** (verbatim, with its scope stated): Go *"There is no fixed
  line length for comments in Go."* — the guide adds that 80 or 100 columns
  are common but *"not a hard cut-off."* **Read the scope honestly:** this
  sentence sits in the guide's *comment-length* section and cross-references a
  companion page for source lines. So the accurate claim is "the Go guide
  states no hard line-length rule, and the sentence available to quote is
  about comments" — **not** a verbatim rule about Go source lines. An earlier
  revision of this file ended that quote with `for Go source code`, which
  widened the guide's own wording; that was wrong and is corrected here.
  (Italic-quoted text in this file always means "the guide's own words," so a
  misquote must not be reproduced in that form even to describe it.)

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
| 4 | **Python** | `.py` | **written below** |
| 5 | **Go** | `.go` | **written below** (pairs with Block 6) |
| 6 | **Java** | `.java` | **written below** (pairs with Block 5: acronym boundary) |
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
- The **no-80-column-here** line is included on purpose: the most common way
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

### Block 4 — Python (`.py`)

Python is the block on the other side of every collision named so far: where
JavaScript and Java land on 80/100 columns and 2-space indent, Python's own
guide states the opposite numbers in its own words. This block also owns the
one *behavioral* (not formatting) rule sourced from Hook 3 — the bare-`except`
ban — which has no equivalent in the blocks written so far.

```text
You are reviewing Python. Apply these rules ONLY to .py files. Do not extend
them to .js, .ts, .java, or any other file type. Do not invent rules beyond
this list.

- Column limit is 80 characters. This is Python's OWN number — do not treat
  it as borrowed from JavaScript; Java's 100-column limit does NOT apply here.
- Indent 4 spaces per block; never use tabs. Do NOT apply the 2-space rule
  from JavaScript/HTML/CSS/Java to Python — 4 spaces is correct here and
  2 spaces is a violation.
- Functions and local variables use lower_with_under naming (e.g.
  parse_customer_record), NOT lowerCamelCase. Classes use CapWords. Modules
  use lower_with_under.py. Flag any camelCase introduced into .py by a
  cross-language lint rule.
- Never use a bare `except:` clause. Catch specific exception types.
```

Scope notes and sourcing:

- **80-column limit** — verbatim: *"Maximum line length is 80 characters."*
  Recorded at Hook 2 above and `combination-packs.md` L1.3. This is Python's
  own stated number, not an import from the JS block — the two guides happen
  to agree on 80, but for independent reasons, so this block states its own
  source rather than pointing at Block 2.
- **4-space indent** — verbatim: *"Indent your code blocks with 4 spaces.
  Never use tabs."* Recorded at Collision 5 above and `combination-packs.md`
  L2.3. This is the rule every other block written so far (2-space) is wrong
  for — the boundary is stated explicitly in the prompt block itself.
- **Naming** — verbatim, Google Python Style Guide §3.16 summary table:
  `function_name`, `local_var_name` (lower_with_under), *"Use CapWords for
  class names, but lower\_with\_under.py for module names."* Already source-
  verified at Collision 6 above (re-confirmed by direct fetch while writing
  that section, not carried from the original 18-guide corpus). **No new
  fetch for this block** — it re-cuts Collision 6.
- **Bare `except` ban** — this is a paraphrase of Hook 3's Python line
  ("Python — exceptions, but bare `except` is banned"), not a fresh verbatim
  quote; Hook 3 does not carry the guide's exact banning sentence, only the
  fact of the ban. Marked as paraphrase here, consistent with the
  verbatim-or-marked constraint — do not read this line as verbatim.
- Nothing about acronym casing is asserted for Python beyond what §3.16's
  naming table already covers, because Hook 1 does not record a Python-
  specific acronym rule.

> Source: `combination-packs.md` L1.3 (80-column), L2.3 (4-space indent);
> Collision 6 above for naming (already independently fetched and confirmed
> there); Hook 3 above for the bare-except fact (paraphrase, not verbatim).
> No guide was re-fetched by 021 for this block.

---

### Block 5 — Go (`.go`)

Go is the block that has to be written in the negative as much as the
positive. It is the **only** guide in the corpus that preserves acronym case,
so a repo-wide naming lint imported from the Java block will rewrite correct
Go into a Go-guide violation — and it is the guide that states **no** column
limit and says **nothing at all** about indentation, so two of the rules every
other block carries must be explicitly switched off here. This block is
designed as the pair to Block 6 (Java): the acronym boundary is closed from
both sides, so neither block can be pasted over the other's files.

Everything below comes from the Go Style Guide's **Decisions** page as
recorded in `language-style-guide-patterns.md`, plus Hook 1 / Hook 2 /
Collision 5 above — **no new verbatim quote is introduced in this block**.

```text
You are reviewing Go. Apply these rules ONLY to .go files. Do not extend them
to .java, .py, or any other file type. Do not invent rules beyond this list.

- Acronyms and initialisms KEEP their case: newCustomerID, parseURL, NATO.
  Do NOT fold them to newCustomerId / parseUrl. Go is the one language here
  that preserves acronym case — if a house rule says "fold acronyms," that
  rule comes from Java/C++/C#/XML and is WRONG in .go.
- Do NOT enforce any column limit. The Go guide sets no hard line length.
  Flag a reviewer that imports 80 (JavaScript/Python/C++) or 100 (Java/C#/
  Swift) into .go.
- Do NOT flag indentation. The Go guide states no indent-width or
  tabs-vs-spaces rule; gofmt already settles it. A tabs-vs-spaces comment on
  a .go file is enforcing a rule the guide never wrote.
- Function and method names must not use a Get or get prefix, unless the
  underlying concept itself uses the word "get".
- The CONSUMER of an interface defines it, not the package implementing it.
- Blank imports (import _ "package") may appear only in a main package, or
  in a test that requires them. Never in a library package.
- context.Context is always the FIRST parameter of a function or method.
- Never define a custom context type, and never use an interface other than
  context.Context in a signature. The guide states no exceptions to this.
- Prefer synchronous functions over asynchronous ones; let the caller add
  concurrency by wrapping the call in a goroutine.
- Errors are returned values, not exceptions. Do not port a "never catch a
  broad exception" rule here — there is nothing to catch.
```

Scope notes and sourcing:

- **Acronym case** — verbatim at Hook 1: *"Words in names that are initialisms
  or acronyms (e.g., `URL` and `NATO`) should have the same case."* Hook 1
  also records the honest scope: Go is the **lone outlier**, not one half of a
  symmetric split. Block 6 (Java) states the same boundary from the other
  side.
- **No column limit** — Hook 2, as corrected: the guide's quotable sentence
  (*"There is no fixed line length for comments in Go."*) is scoped to
  comments, with 80/100 described as common but *"not a hard cut-off."* So
  this block says "enforce no limit," which is what the guide supports, rather
  than quoting a source-line rule the guide does not state.
- **Indentation is a silence, not a rule** — Collision 5. `gofmt` uses tabs,
  but the guide's Decisions page states no indent rule, so the prompt tells a
  reviewer to stay off the topic entirely rather than to enforce tabs. Writing
  "the Go guide mandates tabs" would be the over-claim this file exists to
  avoid.
- **Get/get prefix, interface ownership, blank imports, context-first, no
  custom context types, prefer synchronous** — all six are verbatim in
  `language-style-guide-patterns.md`'s Go section (quoted there from the
  Decisions page). Condensed here into imperative reviewer form; the exact
  wording lives at the source. The "no exceptions to this rule" phrasing on
  custom context types is the guide's own and is the strongest absolute on
  that list — it is reproduced as an absolute deliberately, not softened.
- **Errors as returned values** — Hook 3 records this as a *fact about the
  mechanism*, not as a verbatim sentence. Marked **paraphrase**, same
  treatment as the Python block's bare-`except` line.
- **Scope of the source itself:** the Go rules were read from the Decisions
  page only — *not* the Guide or Best Practices companion pages Google also
  publishes for Go. Rules that live only on those companion pages are
  therefore absent from this block, and their absence is not evidence that Go
  has no opinion on them.

> Source: `language-style-guide-patterns.md` Go section (Decisions page, all
> six rules verbatim there); Hook 1 (acronym case), Hook 2 (no fixed length),
> Collision 5 (indentation silence), Hook 3 (errors as values, paraphrase).
> No guide was re-fetched by 021 for this block.

---

### Block 6 — Java (`.java`)

This is the mirror of Block 5. Go preserves acronym case; Java folds it. If
only one of the two blocks states that boundary, a reviewer holding the other
one will still "fix" files it has no business touching — so the rule is
written twice, once from each side, in the negative as well as the positive.
Java also sits in the **100**-column camp against Go's no-limit and
JavaScript/Python's 80, and it is the guide whose stated character is
*compiler legality is a floor, not a target*: several rules below demand more
than `javac` requires.

Everything is re-cut from the Java section of `language-style-guide-patterns.md`
and Hooks 1–2 / Collisions 5–6 above — **no new verbatim quote is introduced
in this block**.

```text
You are reviewing Java. Apply these rules ONLY to .java files. Do not extend
them to .go, .py, .js, or any other file type. Do not invent rules beyond
this list.

- Acronyms are FOLDED into ordinary words: newCustomerId, parseUrl, MyRpc —
  not newCustomerID or parseURL. If a house rule says "preserve acronym
  case," that rule comes from Go and is WRONG in .java.
- Methods and local variables are lowerCamelCase. Do NOT accept
  lower_with_under here; that is the Python rule.
- Column limit is 100 characters. Do NOT import the 80-column limit from
  JavaScript, Python, or C++.
- Indent 2 spaces; tab characters are not used for indentation.
- Wildcard imports are banned outright, static or otherwise.
- Mark a method @Override whenever it is legal to do so. The one documented
  exception: it may be omitted when the parent method is @Deprecated.
- Every switch must be exhaustive, even where the language does not require
  it.
- Braces are always required for if/else/for/do/while, even for a single
  statement or an empty body.
- A constant (static final, UPPER_SNAKE_CASE) must be DEEPLY immutable and
  its methods free of detectable side effects. A mutable object behind a
  static final reference is not a constant and must not be named like one.
- An empty catch block is acceptable ONLY when a comment explains why taking
  no action is justified. Flag any silent catch with no such comment.
- Declare local variables close to first use, not grouped at the top.
- Array declarations use the String[] args form; String args[] is
  disallowed.
- Do NOT require horizontal alignment of tokens across lines — the guide
  deliberately declines to mandate it.
```

Scope notes and sourcing:

- **Acronym fold** — verbatim at Hook 1: *"Now lowercase everything
  (including acronyms), then uppercase only the first character of:"* each
  word. Hook 1 records the honest scope from the other direction too: Java is
  **not** the outlier here — C++, C# and XML fold as well; **Go alone
  preserves.** So this block's "if a house rule says preserve, it came from
  Go" is accurate, and Block 5 states the same boundary in reverse. Between
  the two, neither block can be pasted over the other's files without the
  conflict being named.
- **lowerCamelCase naming** — verbatim at Collision 6 (Java SG 5.2):
  *"Method names are written in lowerCamelCase."* / *"Local variable names
  are written in lowerCamelCase."* These two are among the three quotes
  fetched directly from the published guide while writing Collision 6 — they
  are **not** in the earlier corpus, which records no Java naming table, and
  they are allowlisted with that reason in `tools/check_verbatim.py`.
- **100 columns** — verbatim at Hook 2: *"Java code has a column limit of 100
  characters."* The corpus notes no rationale accompanies the number in the
  passage read; this block therefore states the limit without inventing a
  reason for it.
- **2-space indent, no tabs** — verbatim at Collision 5: *"Tab characters are
  not used for indentation."* Note what this quote does and does not say: it
  bans tabs. The "2 spaces" half is recorded in Collision 5's grouping of
  Java with JavaScript and HTML/CSS, not carried by this sentence alone.
- **Wildcard imports, @Override, exhaustive switch, deep immutability of
  constants, justified empty catch** — all five are verbatim in the Java
  section of `language-style-guide-patterns.md` and are condensed here into
  imperative form; the exact wording lives there.
- **Braces, local-variable placement, array form, no horizontal alignment** —
  these four are recorded in the corpus as rules **without** an accompanying
  verbatim sentence (the corpus states them in its own words). They are
  therefore **paraphrase**, not verbatim, and are marked as such here — the
  same treatment as Python's bare-`except` and Go's errors-as-values lines.
- **Scope of the source itself:** these rules come from Google's Java Style
  Guide as read for the corpus. Google also publishes Java-adjacent material
  (for example the Android Java conventions) that was **not** read; a rule's
  absence from this block is not evidence that no such rule exists elsewhere.

> Source: `language-style-guide-patterns.md` Java section; Hook 1 (acronym
> fold), Hook 2 (100 columns), Collision 5 (tabs), Collision 6 (naming,
> allowlisted with its fetch reason). No guide was re-fetched by 021 for this
> block.

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
- Section **9 is in progress**: blocks 1–6 (TypeScript, JavaScript, HTML/CSS,
  Python, Go, Java) are written; blocks 7–9 are each marked `[NOT YET WRITTEN]`
  in the block-status table and will be added one at a time. The TypeScript block
  introduces **no new verbatim**; the JavaScript block re-cuts the same shared
  rules **plus** two verbatim quotes (80-column §4.4, indentation §4.2) that
  were already source-verified in `combination-packs.md` and are flagged there
  for re-confirmation. The HTML/CSS block also introduces **no new verbatim**
  — it re-cuts the quoting (single/double/@charset) and indentation quotes
  already confirmed at Collisions 4–5 and `combination-packs.md` L1.4/L2.1.
  The Python block introduces **no new verbatim** either — 80-column and
  4-space-indent re-cut Hook 2 / Collision 5, naming re-cuts Collision 6, and
  the bare-`except` line is explicitly marked as a **paraphrase**, not a
  verbatim quote, since Hook 3 does not carry the guide's exact sentence.
  The Go block introduces **no new verbatim** either — its six positive rules
  are already verbatim in `language-style-guide-patterns.md`'s Go section and
  are condensed here into imperative form, and its "errors are values" line is
  marked paraphrase for the same reason as Python's. The Go block also records
  that its source is the **Decisions page only** (not Google's Guide or Best
  Practices companion pages for Go), so a rule's absence there is not evidence
  that Go lacks one. The Java block introduces **no new verbatim** either: its
  five quoted rules are verbatim in the corpus, its naming quotes are the
  allowlisted Collision 6 fetches, and four rules the corpus states in its own
  words (braces, local-variable placement, array form, no horizontal
  alignment) are marked **paraphrase**. It also records that Java-adjacent
  material Google publishes elsewhere was not read. Blocks 5 and 6 close the
  acronym boundary from both sides — deliberately, so neither can be pasted
  over the other's files. Do not treat the three pending blocks as finished.
- One honesty correction made while writing 6: **Go's indentation is recorded
  as a guide *silence* plus a `gofmt` tooling note — not as a quoted rule.**
  Presenting "Go mandates tabs" as a third quoted camp would over-claim.
- **A widened quote was found and corrected in Hook 2.** This file previously
  presented Go's line-length rule as a verbatim sentence ending
  `...for Go source code` (not reproduced here in quote form, per the marking
  rule below). The corpus records the guide's actual sentence as
  *"There is no fixed line length for comments in Go."* — scoped to comments,
  with a companion page covering source lines. The quote had been broadened
  past its source while keeping the verbatim marking. Hook 2 now carries the
  guide's own wording plus its scope. The underlying claim (the Go guide
  states no hard limit) survives; the false precision did not.
- **The "no new verbatim" claim is now machine-checked**, because it was
  previously only checkable by a reader who thought to normalise whitespace
  first — Markdown wraps long quotes across lines, so a plain grep for one
  returns zero hits and looks like a failure. `tools/check_verbatim.py`
  normalises both sides and fails red when a quote here is absent from the
  corpus. It found the Hook 2 defect above on its first run. Three quotes are
  allowlisted with reasons (the Java 5.2 / Python 3.16 naming quotes, fetched
  directly while writing Collision 6 and stated inline). Run
  `python tools/check_verbatim.py --self-test` to watch it reject a fabricated
  quote before trusting a green run.
- **Italic-quoted text in this file always means the guide's own words.** Not
  emphasis, not a phrase this file coined. The marking is what the checker
  keys on, so overloading it would both mislead a reader and blind the check.
- Third-party licensing of the quoted material is recorded in the repository
  `NOTICE` (Google style guides: CC BY 3.0; the R guide additionally CC BY-SA
  2.0 as a Tidyverse fork), read from the upstream license text on 2026-07-29.
- Counts (3 / 6 / 9) are a *presentation ladder*, not a claim of completeness
  — they are chosen for impact, not because the corpus contains exactly that
  many findings.
