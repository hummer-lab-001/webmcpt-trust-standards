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

## Java: compiler legality as a floor, not a target

Google's Java Style Guide treats what Java itself permits as a starting
point, not a target — several rules demand more than the compiler requires
(exhaustive switches, mandatory braces, near-unconditional `@Override`),
while at least one explicitly declines to add a requirement the language
doesn't need (horizontal alignment). In both directions, the stated
justification is reviewer cost or bug prevention, not compiler correctness:

- **A 100-character column limit** — "Java code has a column limit of 100
  characters." No justification for the specific number appears in the
  passage read; unlike several other rules in this section, this one is
  stated as a bare limit without an accompanying rationale in the text
  confirmed here.
- **Wildcard imports are banned outright** — "Wildcard ('on-demand') imports,
  static or otherwise, are not used." Stated as an unconditional prohibition,
  covering both static and non-static wildcard imports.
- **`@Override` is required whenever it is legal — with one named
  exception** — "A method is marked with the @Override annotation whenever
  it is legal." The guide immediately qualifies this: "@Override may be
  omitted when the parent method is @Deprecated." So a method overriding a
  `@Deprecated` superclass method is the one documented case where the
  annotation may be left off.
- **`switch` statements must be exhaustive, even where Java doesn't require
  it** — "Google Style requires every switch to be exhaustive, even those
  where the language itself does not require it." The rule is framed
  explicitly as going beyond the language's own requirement.
- **Horizontal alignment of code is not required** — the guide does not
  mandate lining up tokens across adjacent lines; its stated reason is that
  keeping such alignment intact through later edits costs reviewer time and
  creates further problems down the line.
- **Constants must be deeply immutable, not merely held in a `final`
  reference** — "Constants are static final fields whose contents are deeply
  immutable and whose methods have no detectable side effects." A mutable
  object referenced by a `static final` field does not qualify and should
  not be named in `UPPER_SNAKE_CASE`.
- **Swallowing an exception in a `catch` block requires a comment defending
  it** — "When it truly is appropriate to take no action whatsoever in a
  catch block, the reason this is justified is explained in a comment."
  Silence is permitted only when explicitly justified in writing.
- **Braces are always required for `if`/`else`/`for`/`do`/`while`** —
  mandatory even when the body is a single statement or empty.
- **Local variables are declared close to first use** — each local variable
  is declared near the point it is first used, rather than all declarations
  being grouped at the top of a block.
- **Array declarations take only the `String[] args` form** — the C-style
  placement of brackets after the variable name, as in `String args[]`, is
  disallowed.

This is Google's own style guide for Google's own codebases — one company's
stated preferences for one language, not a Java-wide standard.

## Go: naming, interface ownership, and concurrency decisions

Read directly from the Decisions page of Google's public Go Style Guide — not
the Guide or Best Practices companion pages Google also publishes for Go. The
rules below are Google's own stated conventions for its Go codebase, not a
general Go-community consensus; some carry an absoluteness of phrasing that
echoes the C++ guide above.

- **Avoid the `Get`/`get` prefix on functions and methods** — the guide's own
  words: "Function and method names should not use a Get or get prefix,
  unless the underlying concept uses the word 'get'." The exception is
  narrow and concept-driven, not a matter of brevity.
- **The interface consumer defines the interface, not the implementer** —
  stated directly: "The consumer of the interface should define it (not the
  package implementing the interface)." Because Go's interface satisfaction
  is implicit, nothing forces the implementing package to declare or depend
  on the interface at all.
- **Side-effect-only imports are confined to `main` or tests that need
  them** — verbatim: "Packages that are imported only for their side effects
  (using the syntax `import _ "package"`) may only be imported in a main
  package, or in tests that require them." A library package may not carry a
  hidden blank import for its own side effects, and even a test may only
  pull one in if the test itself requires it.
- **`context.Context` is always the first parameter** — "When passed to a
  function or method, context.Context is always the first parameter." A
  fixed positional convention rather than a case-by-case judgment.
- **No custom context types, with no stated exceptions** — the guide's
  strongest phrasing on this list: "Do not create custom context types or
  use interfaces other than context.Context in function signatures. There
  are no exceptions to this rule."
- **Prefer synchronous functions over asynchronous ones** — "Prefer
  synchronous functions over asynchronous functions." The guide's own
  verbatim rationale: synchronous functions "keep goroutines localized
  within a call," which "helps to reason about their lifetimes, and avoid
  leaks and data races," and are "easier to test... without the need for
  polling or synchronization." It adds that a caller can add concurrency
  later by wrapping the call in a goroutine, but warns the reverse is hard:
  "it is quite difficult (sometimes impossible) to remove unnecessary
  concurrency at the caller side."

## TypeScript: canonical exports, restrained any usage, and type-system-native visibility

Read directly from Google's public TypeScript Style Guide
(google.github.io/styleguide/tsguide.html) — this is Google's own style guide
for Google's own codebases, one company's stated preferences for one
language, not a TypeScript-community-wide standard. The first three rules
below were confirmed first-hand across two separate verbatim read-throughs
of the guide and are quoted directly; the remaining four come from a single
earlier summary pass over the same page and are paraphrased below without
quotation marks, rather than quoted verbatim.

- **No default exports** (Exports section) — "Do not use default exports.
  This ensures that all imports follow a uniform pattern." Stated reason:
  "Default exports provide no canonical name, which makes central
  maintenance difficult with relatively little benefit to code owners,
  including potentially decreased readability".
- **`any` is discouraged, not banned** (`any` Type section) — the guide's
  own words: "Consider _not_ to use `any`. In circumstances where you want
  to use `any`, consider one of:"
  - "Provide a more specific type"
  - "Use `unknown`"
  - "Suppress the lint warning and document why"

  Stated reason: "TypeScript's `any` type is a super and subtype of all
  other types, and allows dereferencing all properties. As such, `any` is
  dangerous - it can mask severe programming errors, and its use undermines
  the value of having static types in the first place."
- **No `#private` fields — use TypeScript's own `private` keyword**
  (Class Members — No #private fields section) — "Do not use private
  fields (also known as private identifiers)... Instead, use TypeScript's
  visibility annotations." Stated reason: "Private identifiers cause
  substantial emit size and performance regressions when down-leveled by
  TypeScript, and are unsupported before ES2015. They can only be
  downleveled to ES2015, not lower. At the same time, they do not offer
  substantial benefits when static type checking is used to enforce
  visibility."
- **`const enum` is prohibited outright, not merely discouraged** — the
  guide treats this as a hard rule rather than a preference. `const enum`
  is a separate, optimization-only language feature that strips the enum
  out of the emitted JavaScript entirely, making it invisible to plain
  JavaScript consumers at compile time; because that breaks
  interoperability for anything consumed outside the compiling project,
  plain `enum` is required instead.
- **Static methods must be called on the class that defines them — no
  dynamic dispatch** — the guide restricts static methods to being invoked
  through the declaring class itself, closing off calling them dynamically
  through a variable or reference that might actually hold a subclass.
- **`this` is disallowed inside static code — a separate rule from the one
  above** — because static members aren't inherited the way instance
  members are, a subclass can effectively override what a given static
  member resolves to; referencing `this` inside a static method body can
  therefore silently pick up a different value depending on which class
  actually invoked it, rather than behaving the way `this` does in
  instance code.
- **Prefer relative imports within a project** — for files inside the same
  logical project, the guide favors relative import paths (`./foo`,
  `../bar`) over absolute ones, so that relocating files or directories
  within the codebase doesn't force updates to import paths that point
  outside the moved tree.

## Cross-language pattern (relative to this catalog's other findings)

The same "restrict what the language allows, for a stated scale-driven or
correctness reason" pattern recurs independently outside Google's guides too
— see `catalog/governance-patterns.md`'s **module-boundary discipline**
convergence (Kong, prettier, hugo, npm/cli, Chart.js, apollo-server), which is
the *project-governance* form of the same instinct these *language* style
guides apply at the syntax level.

## Honesty note

Python and C++ have been read in full at time of writing. Ten specific Java
rules — 100-character column limit, wildcard-import ban, `@Override` policy
(including its `@Deprecated`-parent exception), exhaustive-switch
requirement, no mandatory horizontal alignment, deep constant immutability,
commented-exception-swallowing, mandatory braces, local-variable declaration
placement, and array-declaration form (see the Java section above) — have
been confirmed first-hand against
google.github.io/styleguide/javaguide.html; the rest of that guide (package
structure, Javadoc conventions, naming beyond constants, and more) has not
yet been read and is not assumed to follow the same pattern. Six specific Go
rules — the `Get`/`get`-prefix convention, interface-consumer-defines-it,
the side-effect-import restriction, `context.Context`-as-first-parameter,
the ban on custom context types, and the synchronous-over-asynchronous
preference (see the Go section above) — have been confirmed first-hand
against the Decisions page of google.github.io/styleguide/go/decisions; the
Guide and Best Practices companion pages Google also publishes for Go have
not yet been read and are not assumed to follow the same pattern.

Google's TypeScript Style Guide (google.github.io/styleguide/tsguide.html)
has since been read: three rules — the default-export ban, the
`any`-avoidance guidance, and the `#private`-fields ban (see the TypeScript
section above) — were confirmed first-hand across two separate verbatim
passes over that page and are quoted directly; four further rules — the
`const enum` prohibition, the no-dynamic-dispatch-on-statics rule, the
no-`this`-in-static-code rule, and the relative-import preference (see the
TypeScript section above) — come from a single earlier summary pass over the
same page and are recorded above as paraphrase, not verbatim quotation; the
rest of that guide has not yet been read and is not assumed to follow the
same pattern. Shell is not the only guide still unread, however: Google's
public style-guide catalog (google.github.io/styleguide/) lists well over a
dozen further guides — among them AngularJS, Common Lisp, C#, HTML/CSS,
JavaScript, JSON, Markdown, Objective-C, R, Swift, and Vim script, in
addition to Shell — none of which have been read first-hand and none of
which should be assumed to follow this pattern.
