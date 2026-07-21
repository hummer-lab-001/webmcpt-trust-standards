# Combination Packs — from "eighteen guides read" to "what you can hand an agent"

`catalog/language-style-guide-patterns.md` reads eighteen Google style guides
one at a time. This file does the next thing: it **combines** them into
review-ready packs, so an engineer (or an AI code reviewer) can be handed one
bundle and told "review a frontend change against this."

A pack is not a summary. It is built to do three things a normal
"style-guide roundup" does not:

### 1. Surprise — contradictions are shown, not averaged away

The usual roundup keeps only the points everyone agrees on and quietly drops
the rest. That throws away the most useful information. These packs keep the
**splits** — the places where Google's own guides disagree — and show both
sides with each side's stated reason. "Google says so" is a cargo-cult
argument; the fastest way to kill it is with Google's own documents
disagreeing with each other. That is the part a working programmer most wants
to read.

### 2. Necessity — every rule is in reviewer form

Each rule is written at a grain you can paste straight into a code-review
checklist or an AI reviewer's system prompt. Not an essay about the rule — the
rule, as an instruction, with its source. The pack ends with a ready-to-paste
prompt block for exactly this.

### 3. Novelty — obey the reason, not the authority

Every rule carries **the reason the guide itself gave** (marked verbatim or
paraphrase, with the source guide named). When a rule's reason is dead — it
was written for IE8, or for a pre-module world — the pack says so plainly and
files it under "fossils." Reading eighteen guides in sequence, and dating
them, is what makes that layer possible.

---

## The three layers (every pack has these)

- **Layer 1 — The Law (convergence).** Rules the guides in the pack *agree*
  on. Each entry: the rule as an imperative, which guides vote for it (and
  which are *silent* — silence is not a vote), each guide's stated reason, and
  a verbatim/paraphrase marker. A small Law layer is an honest result, not a
  failure — the count is never padded, and the number of agreements is itself
  a finding.
- **Layer 2 — The Case Law (where they split).** Rules where the guides in
  the pack *conflict*, or where one legislates and another is silent in a way
  that matters. Both sides, both reasons, then a one-line **recommended
  default** clearly marked as a recommendation, not a fact.
- **Layer 3 — The Fossils (dead rationale).** Rules whose reason has expired.
  Why it was right then, why you need not follow it now, with the source.

Then: **an AI-reviewer prompt block** — Layer 1, rewritten as a paste-in
system prompt, surface-scoped so it is not misapplied.

---

## Pack index and expansion roadmap

| Pack | Guides | Status |
|---|---|---|
| **Web** (3) | TypeScript, JavaScript, HTML/CSS | **written below** |
| **Product** (6) | + Python, Go, Java | **written below** |
| **Enterprise + Mobile** (9) | + C++, C#, Swift | composition only (below) |

The remaining nine guides read (Shell, JSON, Markdown, R, Vim script, Common
Lisp, XML, AngularJS, Objective-C) are held as material for +3 expansions
(21 → 24 → 27 → 30 → 33 → 36). **AngularJS is a cross-pack fossil source** —
its 2013 IE8/Closure rationale is referenced from the Web pack's Layer 3 even
though it is not one of the Web pack's three guides.

**Verification discipline (same as the language-guide file):** a Layer 1
"all agree" claim is made only after checking each guide's own text, and each
such claim carries its source set. Verbatim quotes are marked; paraphrases are
marked; rules a guide is silent on are called silent, not made to agree.

---

## Web Pack — TypeScript · JavaScript · HTML/CSS

**Who it is for:** a reviewer (human or agent) looking at a frontend change —
`.ts`, `.js`, `.html`, `.css`.

**The headline finding, stated up front because it is the honest one:** across
these three guides, the set of rules *all three* state explicitly is
**essentially empty**. That is not a gap in the reading — it is the shape of
the material. TypeScript and JavaScript are one language family and converge
heavily *with each other*; HTML/CSS is a markup-plus-style pair that shares
almost no *language constructs* with them, so it joins only at the level of
foundational file formatting. This pack therefore records **pairwise**
convergence with explicit vote-counting, rather than inventing a three-way
consensus that the sources do not support.

Sources for this pack are the TypeScript, JavaScript, and HTML/CSS sections of
`catalog/language-style-guide-patterns.md`, plus two targeted raw-source
checks (TS and JS indentation / quotes / semicolons / column limit) done while
building this pack; those checks went through the page-summarizing fetch layer,
so sentence-level quotes are reliable but glyph-level identity between two
guides is noted as "returned identically," not proven character-by-character.

### Layer 1 — The Law (convergence)

> Read the vote count on each rule. "TS + JS" means those two state it and
> HTML/CSS is silent (no equivalent construct) — silence is not dissent. A
> reviewer applies each rule only to the surfaces that vote for it.

**L1.1 — Use single-quoted string literals.**
*Votes: TypeScript ✓, JavaScript ✓ (verbatim, returned identically in both).
CSS ✓ for values (see L2.1). HTML ✗ — attributes use double quotes (L2.1).*
- TypeScript (verbatim): "Ordinary string literals are delimited with single
  quotes (`'`), rather than double quotes (`"`)."
- JavaScript (verbatim): the JS guide's sentence was returned identically to
  the TS one. Recorded as sentence-level identical, not proven glyph-by-glyph.
- Reviewer form: **In `.ts` and `.js`, string literals use `'single'` quotes,
  not `"double"`.** (For `.css` values, also single — but this is a different
  guide's rule; see L2.1 for the HTML exception.)

**L1.2 — End every statement with a semicolon; do not rely on ASI.**
*Votes: TypeScript ✓, JavaScript ✓. HTML/CSS — not applicable (not an
ASI-bearing language).*
- JavaScript (verbatim): "Every statement must be terminated with a semicolon.
  Relying on automatic semicolon insertion is forbidden."
- TypeScript (verbatim): "Do not rely on Automatic Semicolon Insertion (ASI).
  Explicitly end all statements using a semicolon."
- Reviewer form: **In `.ts` and `.js`, every statement ends with an explicit
  `;`. Flag any reliance on automatic semicolon insertion.**

**L1.3 — Do not use default exports.**
*Votes: TypeScript ✓, JavaScript ✓ (opening prohibition word-for-word
identical; reasons worded differently). HTML/CSS — silent (no module system).*
- TypeScript (verbatim): "Do not use default exports. This ensures that all
  imports follow a uniform pattern."
- JavaScript (verbatim): "Do not use default exports. Importing modules must
  give a name to these values, which can lead to inconsistencies in naming
  across modules."
- Note: the *prohibition* is identical; the *reasons* differ (TS: "no canonical
  name / central maintenance"; JS: naming "inconsistencies"). Recorded as a
  real convergence with differently-worded rationale — not a claim of identical
  reasoning.
- Reviewer form: **In `.ts` and `.js`, ban `export default`; require named
  exports.**

**L1.4 — Indent by two spaces; never use tabs.**
*Votes: JavaScript ✓, HTML/CSS ✓ (both verbatim). TypeScript — **silent** in
the guide text checked (the TS guide states no indentation rule in the passages
read; likely delegated to its formatter, but that is not asserted here).*
- JavaScript (verbatim): "Each time a new block or block-like construct is
  opened, the indent increases by two spaces." / "Tab characters are not used
  for indentation."
- HTML/CSS (verbatim): "Indent by 2 spaces at a time." / "Don't use tabs or mix
  tabs and spaces for indentation."
- Reviewer form: **In `.js`, `.html`, and `.css`, indent 2 spaces, no tabs.**
  For `.ts`, this pack does not have a cited indentation rule — do not claim
  the TS guide requires it.

**Honest tally for L1.** There is no rule in this pack that all three guides
state. The pack's real spine is a **TS↔JS language-family convergence** (L1.1,
L1.2, L1.3) plus a **JS↔HTML/CSS foundational-formatting convergence** (L1.4).
The count is small on purpose; it is not padded to look like a consensus.

### Layer 2 — The Case Law (where they split)

**L2.1 — String quotes across the frontend surface: single everywhere *except
HTML attributes*.**
This is the split a frontend reviewer actually hits, because one change can
touch JS, CSS, and HTML in one file-set:
- JS strings → single (L1.1). TS strings → single (L1.1). **CSS** values →
  single: HTML/CSS guide (verbatim) "Use single ('') rather than double (\"\")
  quotation marks for attribute selectors and property values."
- **HTML attributes → double**: HTML/CSS guide (verbatim) "When quoting
  attributes values, use double quotation marks." And the guide names its own
  further twist: the CSS `@charset` at-rule reverts to double quotes.
- Why it is not mere taste: the HTML double-quote rule is about
  attribute-value parsing, not preference; normalizing everything to single
  quotes would fight the HTML guide directly.
- **Recommended default (recommendation, not fact):** do *not* apply one
  global quote style across a frontend change. Enforce single quotes in
  JS/TS/CSS and double quotes in HTML attributes — i.e. follow each surface's
  own guide rather than a repo-wide lint rule that flattens them.

**L2.2 — Line length: JavaScript legislates 80; TypeScript and CSS do not.**
- JavaScript (verbatim): "JavaScript code has a column limit of 80 characters.
  Except as noted below, any line that would exceed this limit must be
  line-wrapped." (with exceptions for module/require/import/export lines and
  URLs).
- TypeScript: **no column limit stated** in the guide text checked.
- HTML/CSS: **no column limit stated**.
- **Recommended default:** enforce 80 columns on `.js` only. Do not silently
  extend it to `.ts` or `.css` — the pack has no cited basis for that, and
  asserting it would be exactly the "Google says so" over-reach these packs
  exist to prevent.

### Layer 3 — The Fossils (dead or dying rationale)

**L3.1 — The JavaScript guide is a fossil-in-progress by its own admission.**
Google's own JavaScript guide page "now recommends TypeScript for new code and
points to the TypeScript guide" (recorded in the JavaScript section of the
language-guide file). So for *new* frontend code, the JS-specific rules are
being superseded by the TS guide.
- Why it was right then: the JS guide predates Google's TS-first posture.
- Why you need not treat it as primary now: for greenfield code the vendor
  itself redirects you to TypeScript.
- **Reviewer consequence:** for new code, weight the **TypeScript** guide over
  the JavaScript guide where they overlap; treat JS-only rules as legacy
  maintenance guidance. (The JS rules are not *wrong* — they still govern
  existing `.js` — they are simply no longer the recommended target.)

**L3.2 — AngularJS (cross-pack fossil): a whole guide dated to 2013.**
Not one of this pack's three guides, but the sharpest frontend fossil in the
whole catalog, so it is referenced here for context. Google's AngularJS guide
carries, on the page, "Last modified Feb 07 2013," contrasts pre- and
post-AngularJS-1.2 controller patterns, and notes that custom elements need
"IE8... html5shiv-like hacks." Its rules are justified by Closure-toolchain
compatibility.
- Why it was right then: IE8 support and the Closure compiler were real
  constraints for Google frontend code in 2013.
- Why you need not follow it now: IE8 is gone, the Closure-specific rationale
  does not generalize, and AngularJS 1.x is itself end-of-life.
- **Reviewer consequence:** if a rule's only stated reason is IE8 support,
  Closure presubmit behavior, or pre-ES6 module workarounds, it is a fossil —
  record it as historical, do not enforce it on modern code.

### AI-reviewer prompt block (paste-in)

> Copy the block below into an AI code reviewer's system prompt when reviewing a
> frontend change. It is Layer 1 only (the agreed rules), surface-scoped so it
> is not misapplied, plus the one split that a cross-file frontend change
> forces (L2.1). It deliberately omits rules the guides do not agree on.

```text
You are reviewing a frontend change (TypeScript, JavaScript, HTML, CSS)
against Google's published style guides. Apply each rule ONLY to the file
types listed for it. Do not invent rules; do not extend a rule to a file
type not listed.

TypeScript (.ts) and JavaScript (.js):
- String literals use single quotes ('...'), not double quotes.
- Every statement ends with an explicit semicolon; flag reliance on
  automatic semicolon insertion (ASI).
- Ban `export default`; require named exports.

JavaScript (.js) only:
- Indent 2 spaces, never tabs.
- Column limit is 80 characters (exceptions: import/export/require lines,
  URLs). Do NOT apply this limit to .ts or .css.

HTML and CSS (.html, .css):
- Indent 2 spaces, never tabs.
- CSS values and attribute selectors use single quotes.
- HTML attribute values use DOUBLE quotes (this is the one place single
  quotes are wrong). The CSS @charset rule also uses double quotes.

Do not globally normalize quote style across the change: single quotes in
JS/TS/CSS, double quotes in HTML attributes. This split is intentional and
follows each surface's own guide.

For NEW code, prefer the TypeScript rules over JavaScript rules where they
overlap: Google now directs new frontend code to TypeScript.

If a rule you are tempted to enforce rests only on IE8 support, Closure
toolchain behavior, or pre-ES6 workarounds, do not enforce it — flag it as
outdated instead.
```

---

## Product Pack — TypeScript · JavaScript · HTML/CSS · Python · Go · Java (6)

**Who it is for:** a product team reviewing a full-stack change — frontend
(`.ts`, `.js`, `.html`, `.css`) plus a backend in Python, Go, or Java.

**Why these six:** the Web three cover the client; Python, Go, and Java are the
three backend languages in this catalog with the richest cross-cutting rules.
Together they span the two halves of a typical product's codebase.

**The headline finding, up front:** this pack's most useful content is its
**splits**, not its agreements — and one of them is a *direct contradiction*
between two of the six guides. Adding three backend languages to the frontend
three does not grow the shared-rule set; it grows the number of places where a
reviewer must **not** normalize one rule across the whole stack. The pack's job
is to mark exactly where.

Sources: the Web pack above (TS/JS/HTML-CSS) plus a raw-source cross-check of
Python, Go, and Java (indentation, line length, string quotes, naming,
error handling) done while building this pack, against
`pyguide.md`, `go/decisions.md`, and `javaguide.html` in the `google/styleguide`
repo. Those checks are summarizer-mediated except where noted; the flagship
naming contradiction below was confirmed verbatim from raw text.

### Layer 1 — The Law (convergence)

**L1.1 — Restrict a language feature when its reader-cost outweighs its
power; state the reason.** *Votes: all six, at the level of a shared
philosophy rather than a shared mechanical rule.* This is the one thing all
six guides genuinely share — and it is a principle, not a line a linter can
check, so it is recorded as such.
- Python (verbatim, "Power Features"): "It's harder to read, understand, and
  debug code that's using unusual features underneath."
- Go (verbatim): "Do not use this feature in the Google codebase; it makes it
  harder to tell where the functionality is coming from."
- Java: "compiler legality as a floor, not a target" (language-guide file).
- TypeScript / JavaScript: "restrict what the language permits" (language-guide
  file — e.g. JS's ES-module-cycle ban naming the spec it overrides).
- HTML/CSS: the `id`-attribute rule justified by a JavaScript-namespace side
  effect (language-guide file).
- Reviewer form: **A rule that removes a working language feature should cite
  the reader/maintenance cost it prevents. If it cannot, question the rule.**

**L1.2 — Never silently discard an error or exception.** *Votes: the three
backend guides — Python ✓, Java ✓, Go ✓ — converge on the principle, each by
a different mechanism. Frontend three: silent (no cataloged error rule → not
votes).*
- Python (verbatim): "Never use catch-all except: statements, or catch
  Exception or StandardError" (except to re-raise or as a recorded, suppressed
  isolation point).
- Java (verbatim): "It is very rarely correct to do nothing in response to a
  caught exception."
- Go (verbatim): "By convention, error is the last result parameter." — and the
  guide requires the returned error be handled, not dropped (Go's mechanism is
  an explicit return value, not a caught exception).
- Note the shape: Python and Java forbid *ignoring a caught exception*; Go has
  no exceptions and instead requires *handling a returned error*. One
  principle — an error condition must not vanish silently — three
  language-specific mechanics. Recorded as a principle-level convergence, not
  a claim of identical rules.
- Reviewer form: **In Python/Java/Go, flag any error or exception that is
  caught-and-ignored (Python/Java) or returned-and-dropped (Go).**

**L1.3 — An 80-column line limit (JavaScript and Python only).** *Votes:
JavaScript ✓, Python ✓ (both verbatim). This is a real pairwise agreement —
and also one side of the split in L2.2, because Java says 100 and Go says
none.*
- JavaScript (verbatim): "JavaScript code has a column limit of 80 characters."
- Python (verbatim): "Maximum line length is 80 characters."
- Reviewer form: **Enforce 80 columns on `.js` and `.py`. Do not extend it to
  `.ts`, `.java`, `.go`, or `.css` — they disagree or are silent (see L2.2).**

**L1.4 — Frontend-subset rules carry over.** The TS↔JS convergences from the
Web pack (single quotes, explicit semicolons / no ASI, no default exports)
apply unchanged to this pack's frontend third. See Web pack L1.1–L1.3; not
repeated here.

### Layer 2 — The Case Law (where they split)

**L2.1 — FLAGSHIP CONTRADICTION: acronym casing. Go preserves it; Java folds
it. The two guides say opposite things.** This is the clearest case of Google's
own guides directly contradicting each other, and both sides are verbatim:
- **Go — preserve the acronym's case** (verbatim, re-confirmed from raw source
  on both sides of this contradiction): "Words in names that are initialisms or
  acronyms (e.g., `URL` and `NATO`) should have the same case." So an acronym
  keeps one consistent case — `URL` stays `URL` (or `url`), never `Url`
  (`userID`, `parseURL` illustrate the rule; these are derived from it, not
  quoted from the guide, whose own examples are `URL` and `NATO`).
- **Java — fold the acronym into an ordinary word** (verbatim): "Now lowercase
  everything (including acronyms), then uppercase only the first character of:"
  — the guide then continues with which characters to uppercase (each word for
  UpperCamelCase; each word except the first for lowerCamelCase). Its own
  examples table: "XML HTTP request" → `XmlHttpRequest` (not `XMLHTTPRequest`);
  "new customer ID" → `newCustomerId` (not `newCustomerID`).
- So the *same* identifier is spelled two *opposite* ways depending on the
  language: Go `newCustomerID`, Java `newCustomerId`. A reviewer who enforces
  one house acronym style across a full-stack change would be **wrong in one of
  the two languages by that language's own Google guide.**
- Cross-pack note: Java is not alone on the "fold" side — the C# guide (`MyRpc`
  not `MyRPC`) and the XML guide (`informationUri`) fold acronyms too (see the
  9-guide pack). Across the whole catalog, **Go is the outlier** that preserves
  initialism case; every other guide that states an acronym rule folds it.
- **Recommended default (recommendation, not fact):** do not normalize acronym
  casing across languages. Follow Go's preserve-case in `.go` and Java's
  fold-to-word in `.java`. This is not a style whim on either side — each is
  that language community's established convention, which is why the guides
  differ.

**L2.2 — Line length: three different answers across the pack.**
- JavaScript = **80** (verbatim, L1.3). Python = **80** (verbatim, L1.3).
- Java = **100** (verbatim): "Java code has a column limit of 100 characters."
- Go = **no hard limit** (verbatim): "There is no fixed line length for
  comments in Go." — the guide adds that 80 or 100 are common but "not a hard
  cut-off." (Nuance: this explicit statement is in the comment-length section
  and cross-references a companion page for source lines; the no-hard-limit
  stance is Go's, but the exact figure for code lines is deferred to gofmt.)
- TypeScript = silent. HTML/CSS = silent.
- **Recommended default:** three limits (80 / 100 / none) coexist in one
  product. Enforce each language's own; never impose a single column rule
  repo-wide.

**L2.3 — Indent width and character: 2 spaces, 4 spaces, or tabs.**
- JavaScript = 2 spaces, no tabs (verbatim). HTML/CSS = 2 spaces, no tabs
  (verbatim). Java = 2 spaces, no tabs (verbatim: "Tab characters are not used
  for indentation," +2 per block).
- Python = **4 spaces**, no tabs (verbatim): "Indent your code blocks with 4
  spaces. Never use tabs."
- Go = **tabs** — but this is a clean *silence* in the guide text: the Decisions
  page never states tabs-vs-spaces or a width; the well-known "Go uses tabs"
  fact is gofmt's behavior, not a rule asserted on the page read. Recorded as
  silence with the tooling caveat, not as a quoted rule.
- TypeScript = silent (Web pack).
- **Recommended default:** 2 spaces in JS/HTML/CSS/Java, 4 in Python, whatever
  gofmt emits (tabs) in Go. A single indent rule cannot span the stack.

**L2.4 — String quotes: five stances, no shared rule.**
- TS / JS strings → single (Web pack). CSS values → single; HTML attributes →
  double (Web pack L2.1).
- Python → **no fixed choice; consistency within a file** (verbatim): "Pick '
  or \" and stick with it." — a distinctive stance: consistency over a mandated
  character.
- Go → silent (no source-literal quote-style rule; a clean negative).
- Java → not a style choice: Java syntax mandates double-quoted strings, so the
  guide states no rule (clean negative).
- **Recommended default:** apply each surface's own rule; there is no coherent
  cross-stack quote convention to enforce.

### Layer 3 — The Fossils (dead or dying rationale)

**L3.1 — The frontend fossils carry over.** The JavaScript-guide-superseded-by-
TypeScript fact (Web pack L3.1) and the 2013 AngularJS/IE8/Closure guide (Web
pack L3.2) remain this pack's fossil references for the frontend third.

**L3.2 — No dated backend fossil surfaced in this pass — stated rather than
invented.** The Python, Go, and Java raw-source checks for this pack did not
surface a clearly dated, reason-expired rule of the AngularJS kind. Rather than
manufacture one (Python-2 residue would be a plausible candidate but was not
verified against the guide's current text in this pass), this layer is recorded
as **thin for the backend three, pending a dedicated fossil pass.** A small
verified note that *is* fossil-adjacent: the Java guide's current text uses the
term `UPPER_SNAKE_CASE` for constants, not the older `CONSTANT_CASE`; downstream
material still saying `CONSTANT_CASE` is citing a superseded revision.

### AI-reviewer prompt block (paste-in)

> For a full-stack change. Layer 1 (agreed rules) plus — critically — the
> "do not normalize across the stack" warnings, which are the practical payload
> of this pack.

```text
You are reviewing a full-stack change (TypeScript, JavaScript, HTML, CSS,
Python, Go, Java) against Google's published style guides. Apply each rule
ONLY to the languages listed for it. Several rules DIFFER by language — do
NOT normalize them across the change.

All languages:
- A rule that bans a working language feature should state the reader- or
  maintenance-cost it prevents; be skeptical of rules that cannot.

Python, Go, Java (backend):
- Never silently discard an error/exception. Flag a caught-and-ignored
  exception (Python/Java) or a returned-and-dropped error (Go).

DO NOT NORMALIZE THESE ACROSS LANGUAGES — each is correct per its own guide:
- Acronym casing: Go PRESERVES it (userID, parseURL). Java FOLDS it
  (newCustomerId, XmlHttpRequest). Enforcing one style across .go and .java
  is wrong in one of them. (C# and XML fold like Java; Go is the outlier.)
- Line length: JavaScript=80, Python=80, Java=100, Go=no hard limit,
  TypeScript/HTML/CSS=unspecified. Enforce each language's own; never one
  repo-wide column rule.
- Indentation: JS/HTML/CSS/Java=2 spaces, Python=4 spaces, Go=tabs (gofmt),
  TypeScript=unspecified. No single indent rule spans the stack.
- String quotes: JS/TS/CSS single; HTML attributes double; Python "pick one
  and be consistent per file"; Go and Java state no source-literal rule.

Frontend (.ts/.js): single-quote strings, explicit semicolons (no ASI),
no `export default`. Prefer the TypeScript guide over JavaScript for new code.

If a rule rests only on IE8, Closure, or pre-ES6 workarounds, flag it as
outdated rather than enforcing it.
```

## Enterprise + Mobile Pack — + C++ · C# · Swift (9)

**Composition and intent only — body not yet written.**

**Who it is for:** an organization reviewing across systems code (C++), a
managed enterprise stack (C#), and mobile (Swift/Objective-C).

**Why these nine:** they extend the Product six into the two remaining
large-surface domains — native/systems (C++) and the two platform-vendor
languages (C#→Microsoft, Swift→Apple). This is where the catalog's **external
deference gradient** becomes a first-class pack feature: C# *follows*
Microsoft's naming, Swift *incorporates* Apple's by reference — a split about
*whose* authority governs naming, which an enterprise picking conventions must
decide.

**Expected shape when written:** Layer 2 will be unusually rich here — the C#
guide's Unity-typed examples versus its silent prose, the contrast between that
silent-platform pattern (C#) and a guide that names its toolchain openly
(AngularJS naming Closure in its subtitle), and the 100-column agreement across
Java/C#/Swift/Objective-C are all already-recorded material in the language-guide
file. Layer 1 will lean on the RFC-2119-style graded-rule convergence if the
pack is later widened to Common Lisp/XML.

*Not yet written: all three layers and the prompt block. Only the composition
and rationale above exist.*

---

## What is written and what is not (self-honesty)

- **Written in full:** the design preamble, the pack index/roadmap, the
  **Web pack** (3 guides), and the **Product pack** (6 guides) — each with all
  three layers plus an AI-reviewer prompt block.
- **Composition only (no rule bodies):** the Enterprise+Mobile (9) pack —
  headings, who-it-is-for, why-these-guides, and expected shape, explicitly
  marked "not yet written."
- **Not started:** the +3 expansion packs (21 → 36) and any pack drawing on the
  remaining held-back guides beyond the AngularJS fossil reference.
- **Verification standing:** every Layer 1 convergence names its voting guides;
  every verbatim quote is marked; silences are recorded as silence, not made
  to agree (TypeScript on indentation/column limit; Go on tabs and
  string-literal quotes; Java and Go on string quotes). The Product pack's
  flagship acronym contradiction (Go preserves vs Java folds) was confirmed
  verbatim from raw source on both sides; the remaining Python/Go/Java
  cross-checks are summarizer-mediated (sentence-level reliable, not
  glyph-proven). Layer 3 for the backend three is stated as thin rather than
  filled with an unverified fossil.
