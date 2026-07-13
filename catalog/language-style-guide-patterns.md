# Language Style Guide Patterns — What "Reader Over Writer" Actually Means

Source: Google's official public style guides (google.github.io/styleguide),
read directly — not a summary of a summary. Google's guides are chosen as
the first entries here because they are unusually explicit about *why* each
rule exists, not just what it is; that stated rationale is what makes them
useful as a cross-language pattern set rather than a single company's taste.

## Python: restricting the dynamic parts of a dynamic language

Google's Python guide repeatedly narrows features the language itself allows,
each time naming a specific failure mode:

- **`staticmethod` is avoided, not banned outright** — "never use `staticmethod`
  unless forced to in order to integrate with an API." A module-level function
  is preferred: it is directly testable without a class fixture.
- **`assert` is barred from validation logic** — assertions can be stripped at
  runtime (`python -O`), so anything load-bearing must raise an explicit
  exception instead. This is a language-feature restriction driven by a
  deployment-mode fact, not a style preference.
- **Decorators require a "clear advantage" to justify use** — the guide's own
  words: they "can perform arbitrary operations on a function's arguments or
  return values, resulting in surprising implicit behavior." Power is treated
  as a cost to be justified, not a default good.
- **Properties are restricted to trivial computation** — matching what a plain
  attribute access would imply. Complex logic hidden behind property syntax
  is explicitly disallowed.
- **Bare `except:` is prohibited** — the guide's own justification: it "will
  really catch everything including misspelled names, `sys.exit()` calls,
  Ctrl+C interrupts."
- **String accumulation via `+=` in a loop is disallowed** — named reason:
  quadratic time complexity; list-join is required for "consistently
  amortized-linear run-time complexity." A performance rule stated as a
  style rule.

## C++: restricting a systems language for a 100M+-line codebase

Google's C++ guide is explicit that its restrictions are *not* about what the
language allows but about what a codebase of Google's stated scale can
sustain. Nearly every rule below carries an explicit scale-driven rationale
in the guide's own text:

- **Exceptions are banned entirely** — not a purity argument: "most existing
  C++ code at Google is not prepared to deal with exceptions," so the
  conversion cost outweighs the benefit at their existing scale.
- **RTTI (`dynamic_cast`/`typeid`) is discouraged** — "querying the type of an
  object at run-time frequently means a design problem"; virtual dispatch or
  the Visitor pattern is required instead.
- **`using namespace foo;` is banned** — explicit scale rationale: "with a
  codebase of 100+ million lines... name collisions... are difficult to work
  with and hard to avoid if everyone puts things into the global namespace."
- **Single-argument constructors must be `explicit`** — implicit conversions
  "can hide type-mismatch bugs."
- **Functions should stay under roughly 40 lines** — stated reason is reader
  cost over time: "someone modifying it in a few months may add new
  behavior... keeping functions short... makes it easier for other people to
  read and modify."
- **Virtual calls from constructors are prohibited** — a correctness rule:
  such calls "will not get dispatched to the subclass implementations,"
  a subtle inheritance bug class closed off by a blanket rule rather than
  left to reviewer vigilance.

The guide states its own unifying principle directly: it optimizes for
**reader experience over writer convenience**, on the explicit premise that
code spends far more of its lifetime being read and maintained than being
written — a philosophy that generalizes past these two languages.

## Cross-language pattern (relative to this catalog's other findings)

The same "restrict what the language allows, for a stated scale-driven or
correctness reason" pattern recurs independently outside Google's guides too
— see `catalog/governance-patterns.md`'s **module-boundary discipline**
convergence (Kong, prettier, hugo, npm/cli, Chart.js, apollo-server), which is
the *project-governance* form of the same instinct these *language* style
guides apply at the syntax level.

## Honesty note

Only Python and C++ have been read in full at time of writing; Google's other
public guides (Go, Java, Shell, TypeScript, etc.) are ◇ — not yet read
first-hand, not assumed to follow the same pattern.
