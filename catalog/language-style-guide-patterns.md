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

## Shell: readability floors, forbidden features, and structural discipline

Read directly from Google's public Shell Style Guide
(google.github.io/styleguide/shellguide.html) — this is Google's own style
guide for Google's own codebases, one company's stated preferences for shell
scripting conventions, not a shell-scripting-community-wide standard. The
first five rules below were confirmed first-hand across two separate
verbatim read-throughs of the guide and are quoted directly; the remaining
five come from a single earlier summary pass over the same page and are
paraphrased below without quotation marks, rather than quoted verbatim. One
narrow caveat on the five quoted below: independent re-checks of the page
have not consistently agreed on character-level typography — underscore vs.
asterisk emphasis, and three-dot vs. Unicode ellipsis inside the bracket
examples — so those specific glyphs, unlike the wording itself, should be
treated as provisional pending a direct browser view-source check.

- **A 100-line ceiling forces a rewrite in a more structured language** (When
  to use Shell section) — "If you are writing a script that is more than 100
  lines long, or that uses non-straightforward control flow logic, you
  should rewrite it in a more structured language _now_." Either
  condition — excess length or non-straightforward control flow — is stated
  as sufficient on its own to trigger the rewrite.
- **SUID and SGID are forbidden outright, with no exception offered**
  (SUID/SGID section) — the guide's own words, quoted here as the two
  separate sentences that appear together in that section rather than as
  one continuous passage: "SUID and SGID are _forbidden_ on shell scripts."
  "There are too many security issues with shell that make it nearly
  impossible to secure sufficiently to allow SUID/SGID."
- **`[[ ... ]]` is preferred over `[ ... ]`, `test`, and `/usr/bin/[`** (Test,
  `[ ... ]`, and `[[ ... ]]` section) — "`[[ ... ]]` is preferred over
  `[ ... ]`, `test` and `/usr/bin/[`. `[[ ... ]]` reduces errors as no
  pathname expansion or word splitting takes place between `[[` and `]]`."
  The stated reason is a correctness property of the syntax itself, not a
  stylistic preference.
- **`$(command)` is required over backticks** (Command Substitution
  section) — "Use `$(command)` instead of backticks. Nested backticks
  require escaping the inner ones with `\`. The `$(command)` format doesn't
  change when nested and is easier to read."
- **Variables should be quoted, brace form preferred — but the guide itself
  flags this as non-mandatory** (Variable expansion section) — the guide's
  own words: "Stay consistent with what you find; quote your variables;
  prefer `"${var}"` over `"$var"`." Elsewhere in that section the guide
  characterizes this kind of quoting guidance as a strong recommendation
  rather than a hard mandate — a materially weaker force than the
  forbidden-outright SUID/SGID rule above. Unlike the sentence just quoted,
  that specific characterization is this document's paraphrase, not a
  confirmed verbatim sentence.
- **Function-local variables should be marked `local`** — variables
  declared inside a function should carry the `local` keyword, so a
  function's working state doesn't leak into, or collide with, the global
  namespace.
- **Avoid piping into a `while` loop — prefer process substitution or
  `readarray`** — a pipe runs its right-hand side in a subshell, so
  variable assignments made inside the loop body do not survive back into
  the calling shell once the loop exits.
- **Arithmetic should use double parentheses exclusively — not `let`,
  square-bracket expressions, or `expr`** — the shell's own built-in
  arithmetic (`((...))`, `$((...))`) is faster and avoids the portability
  concerns the external or legacy forms (`let`, `$[...]`, `expr`) carry.
- **Functions belong together, just below constants, with no executable
  code between them** — grouping them at the top of the file this way is
  stated as a readability and debugging aid.
- **A script with more than one function needs a `main` function, called at
  the file's end** — this gives the program one explicit entry point, and
  lets the script itself use `local` the way its other functions do.

## JavaScript: restricting a dynamic language ahead of its own TypeScript successor

Read directly from Google's public JavaScript Style Guide
(google.github.io/styleguide/jsguide.html) — this is Google's own style guide
for Google's own codebases, one company's stated preferences for one
language, not a JavaScript-community-wide standard. Google's guide page
itself now recommends TypeScript for new code and points to the TypeScript
guide above; the JavaScript guide is read here for its own historical
pattern set, not as a claim that Google prefers it going forward. The seven
rules below were confirmed first-hand across two separate verbatim
read-throughs of the guide (both passes returned character-identical text)
and are quoted directly; the remaining three come from a single pass and are
paraphrased below without quotation marks, rather than quoted verbatim.

- **The variadic `Array` constructor is banned, a literal is required
  instead** — heading: "Do not use the variadic `Array` constructor."; body
  text directly beneath it: "The constructor is error-prone if arguments are
  added or removed. Use a literal instead." (quoted here as two separate
  verbatim fragments — the heading has no trailing period on the source
  page, unlike the body sentences, so the two are not one continuous
  quotation). A single-argument `new Array(length)` call is separately
  permitted, so the rule targets the ambiguous multi-argument form
  specifically, not `Array`-construction as such.
- **The `with` keyword is banned outright** — "Do not use the `with`
  keyword. It makes your code harder to understand and has been banned in
  strict mode since ES5." The stated reason combines a readability claim
  with a language-specification fact (its own strict-mode rejection).
- **`eval` and the `Function(...string)` constructor are banned, with one
  named exception** — "Do not use `eval` or the `Function(...string)`
  constructor (except for code loaders). These features are potentially
  dangerous and simply do not work in CSP environments." The stated
  rationale is dual: a security concern and a deployment-environment fact
  (Content Security Policy incompatibility), not a style preference alone.
- **Default exports are banned** — "Do not use default exports. Importing
  modules must give a name to these values, which can lead to
  inconsistencies in naming across modules." The opening prohibition
  ("Do not use default exports.") is identical, word for word, to the
  TypeScript guide's rule above; the stated rationale differs in wording
  between the two guides (this one names naming *inconsistency* directly,
  while the TypeScript guide's own quoted text names the lack of a
  "canonical name" and "central maintenance difficult"), though both stay
  on the same naming-related theme. Two separate Google language guides
  independently banning the same feature, even with differently worded
  reasoning, is still a convergence worth noting — just not a claim of
  identical wording throughout.
- **Identity operators are required over loose equality, with documented
  exceptions** — "Use identity operators (`===`/`!==`) except in the cases
  documented below." The guide frames this as a default with named carve-outs
  rather than an absolute ban on `==`/`!=`.
- **ES module cycles are banned even though the language permits them** —
  "Do not create cycles between ES modules, even though the ECMAScript
  specification allows this." The guide explicitly names the gap between
  what the specification allows and what Google's style requires — the same
  "restrict what the language permits" pattern seen throughout this file,
  stated here in its most self-aware form: the rule text itself names the
  permissiveness it is overriding.
- **`var` is banned outright; `const` is the default, `let` the fallback** —
  "Declare all local variables with either `const` or `let`. Use `const` by
  default, unless a variable needs to be reassigned. The `var` keyword must
  not be used." No stated rationale accompanies this specific sentence in
  the passage confirmed here (unlike several rules above); `var`'s
  function-scoping and hoisting behavior is the well-known reason in the
  wider JavaScript community, but that is not asserted as this guide's own
  stated words.
- **Built-in objects and their prototypes must never be modified** —
  paraphrased: extending or altering `Object`, `Array`, or other built-in
  types/prototypes is disallowed outright, protecting code that depends on
  standard built-in behavior remaining unchanged.
- **Primitive wrapper objects must never be constructed with `new`** —
  paraphrased: `Boolean`, `Number`, and `String` may be called as coercion
  functions but must never be instantiated as objects via `new`, since a
  wrapper object and its underlying primitive behave differently in ways the
  guide characterizes as surprising (e.g. a wrapped `Boolean(false)` is
  still truthy as an object).
- **Braces are mandatory for all control structures, with a narrow
  single-line exception** — paraphrased: `if`/`else`/`for`/`do`/`while`
  bodies must be braced even for a single statement, except that a short
  `if` with no `else` may stay unbraced on one line when it does not harm
  readability — the same brace-discipline pattern as Java's unconditional
  version above, but with an explicit carve-out Java's guide does not grant.

## JSON: a data-format style guide, not a language style guide

Read directly from Google's public JSON Style Guide
(google.github.io/styleguide/jsoncstyleguide.xml) — this is Google's own
style guide for JSON payloads used by its own APIs, one company's stated
preferences for a data-interchange format, not a JSON-industry-wide
standard. Unlike the seven guides above, this one does not govern a
programming language's syntax; it governs the shape of data that crosses
an API boundary, so several of its rules (reserved property names,
top-level envelope structure) have no analogue in the language guides
above. The five rules below were confirmed first-hand across two separate
verbatim read-throughs of the guide (both passes returned character-identical
text) and are quoted directly; the remaining rules come from a single pass
and are paraphrased below without quotation marks, rather than quoted
verbatim.

- **Property names must be camelCase ASCII, with a narrow character rule
  for the first letter** — "Property names must be camel-cased, ascii
  strings. The first character must be a letter, an underscore (_) or a
  dollar sign ($). Subsequent characters can be a letter, a digit, an
  underscore, or a dollar sign." Stated reason: this "mirror[s] the
  guidelines for naming JavaScript identifiers," so a JavaScript client can
  access a property using plain dot notation rather than bracket-and-string
  access.
- **`kind` must be the first property when present, `items` must be the
  last** — "If the kind object is present, it should be the first property
  in the object" and, separately, "If items exists, it should be the last
  property in the data object." The guide's stated reason for the `items`
  placement: this "allows all of the collection's properties to be read
  before reading each individual item," so a client with a large `items`
  array can read the surrounding metadata without first parsing the whole
  array.
- **A response carries `data` or `error`, never both — and `error` wins on
  conflict** — "A JSON response should contain either a data object or an
  error object, but not both. If both data and error are present, the error
  object takes precedence." A structural rule for the top-level envelope, not
  a naming convention — it fixes how a client should resolve an
  otherwise-ambiguous response shape rather than just naming a field.
- **A `deleted` marker must be `true` when present — `false` is explicitly
  disallowed, not merely discouraged** — "If deleted is present, its value
  must be true; a value of false can cause confusion and should be avoided."
  The guide treats the field's mere presence as the deletion signal, so a
  `"deleted": false` would create a value that contradicts its own field's
  reason for existing.
- **No comments in JSON objects** — "Comments should not be included in
  JSON objects." The guide immediately concedes its own examples break this
  rule for teaching purposes only: "Some of the examples in this style
  guide include comments. However this is only to clarify the examples" —
  the guide names the exception to its own rule in the same breath as the
  rule itself, the same self-aware carve-out pattern seen in the JavaScript
  guide's ES-module-cycle rule above.

Paraphrased (single-pass, not verbatim): enum values should be represented
as strings rather than numbers, so that a client can gracefully handle a
value it doesn't recognize instead of failing on an unmapped integer;
optional properties with an empty or `null` value should generally be
dropped from the payload rather than sent as `null`, unless there is a
specific semantic reason to assert the absence explicitly; array-typed
properties should carry plural names while all other properties should be
singular; and date values should follow RFC 3339 while time-duration
values should follow ISO 8601.

**Scope note**: this is a data-interchange convention for Google's own
APIs, not a JSON specification and not a claim about how the wider JSON
ecosystem names its fields — many widely used JSON APIs (including some
cataloged elsewhere in this repository) do not follow camelCase, the
`kind`/`items` ordering, or the reserved top-level property names above.

## HTML/CSS: one guide, two languages, and an internal quotation-mark contradiction the guide names itself

Read directly from Google's public HTML/CSS Style Guide
(google.github.io/styleguide/htmlcssguide.html) — this is Google's own
style guide for HTML and CSS in its own codebases, one company's stated
preferences, not an HTML/CSS-industry-wide standard. Unlike every other
guide in this catalog, this single page governs two markup/style
languages together: a "General" section states rules that apply to both
before the guide splits into HTML-specific and CSS-specific sections — a
structural choice not seen elsewhere here. Cross-checking method: two
independent full read-throughs were run blind to each other; most rules
below matched character-for-character between the two on first pass, and
the remainder — where one pass returned a shorter, truncated version of a
sentence the other pass returned in full, or where only one pass surfaced
the rule at all — were resolved with additional short, targeted re-fetches
asking only for that one rule's exact wording (the same short-fragment
workaround the JSON section above introduced for this page-summarizer's
character-count limit). Every rule quoted below reflects at least two
independent confirmations, whether that was two matching initial passes or
an initial pass plus a targeted re-fetch.

- **Quotation marks split by language, with one exception carved back
  across the split** — HTML requires double quotes, CSS requires single
  quotes, except for one CSS at-rule that reverts to double. HTML:
  "When quoting attributes values, use double quotation marks." / "Use
  double (\"\") rather than single quotation marks ('') around attribute
  values." CSS: "Use single ('') rather than double (\"\") quotation marks
  for attribute selectors and property values." / "Do not use quotation
  marks in URI values (url())." — then the guide names its own exception:
  "Exception: If you do need to use the `@charset` rule, use double
  quotation marks—single quotation marks are not permitted." The guide
  does not merely differ by language; it states a rule, then a
  contradicting exception to that same rule, entirely in its own words.
- **Avoiding `id` attributes is a correctness rule about a JavaScript
  side effect, not a naming-style preference** — "Avoid unnecessary id
  attributes." / "Prefer class attributes for styling and data attributes
  for scripting." Stated reason: "When an element has an id attribute,
  browsers will make that available as a named property on the global
  `window` prototype, which may cause unexpected behavior." Where an `id`
  is unavoidable: "Where id attributes are strictly required, always
  include a hyphen in the value to ensure it does not match the JavaScript
  identifier syntax, e.g. use `user-profile` rather than just `profile` or
  `userProfile`." This is a second, independent instance — in a completely
  different artifact type (HTML markup, not a JSON payload) — of a Google
  guide shaping a naming convention specifically to protect JavaScript's
  implicit global/property namespace; see the JSON section's camelCase
  rule above, whose own stated reason is that it "mirror[s] the guidelines
  for naming JavaScript identifiers." The two guides reach the same
  underlying concern (JavaScript's implicit property/namespace behavior)
  from opposite directions — one naming data fields, one naming markup
  attributes — independently confirmed against each guide's own text
  rather than assumed from the resemblance alone.
- **Class names must be hyphen-delimited; underscores and bare
  concatenation are both disallowed** — "Use meaningful or generic class
  names." / "Instead of presentational or cryptic names, always use class
  names that reflect the purpose of the element in question, or that are
  otherwise generic." Stated reason: "Using functional or generic names
  reduces the probability of unnecessary document or template changes."
  The delimiter is a separate, explicit rule: "Separate words in class
  names by a hyphen." / "Do not concatenate words and abbreviations in
  selectors by any characters (including none at all) other than hyphens,
  in order to improve understanding and scannability."
- **ID selectors are avoided entirely in CSS, not merely discouraged in
  favor of classes** — "Avoid ID selectors." Stated reason: "ID attributes
  are expected to be unique across an entire page, which is difficult to
  guarantee when a page contains many components worked on by many
  different engineers. Class selectors should be preferred in all
  situations." A page-scale correctness argument (uniqueness is hard to
  guarantee across many contributors), not a stylistic taste.
- **`type` attributes on stylesheet and script elements are prohibited,
  not merely optional** — "Omit type attributes for style sheets and
  scripts." / "Do not use type attributes for style sheets (unless not
  using CSS) and scripts (unless not using JavaScript)." Stated reason:
  "Specifying type attributes in these contexts is not necessary as HTML5
  implies text/css and text/javascript as defaults." A rule justified by
  what the spec already guarantees by default, rather than by a
  readability or scale argument.
- **Capitalization is lowercase-only, across both languages, with one
  named exception** — "Use only lowercase." / "All code has to be
  lowercase: This applies to HTML element names, attributes, attribute
  values (unless text/CDATA), CSS selectors, properties, and property
  values (with the exception of strings)." No further rationale is stated
  in the passage confirmed here beyond the rule itself.
- **Trailing whitespace is banned for a stated diff-hygiene reason** —
  "Remove trailing white spaces." Stated reason: "Trailing white spaces
  are unnecessary and can complicate diffs." — a justification distinct
  from the readability, performance, and correctness arguments that carry
  most rules in this file. It is not unique: the Swift section below
  records a trailing-comma rule resting on the same "cleaner diffs"
  reasoning, in an otherwise unrelated area of syntax.
- **Shorthand CSS properties are required even when only one value is
  being set** — "Use shorthand properties where possible." / "CSS offers a
  variety of shorthand properties (like font) that should be used whenever
  possible, even in cases where only one value is explicitly set." Stated
  reason: "Using shorthand properties is useful for code efficiency and
  understandability."
- **Units are omitted after a zero value unless the specific property
  requires one** — "Omit unit specification after \"0\" values, unless
  required." / "Do not use units after 0 values unless they are required."
  No further elaboration was found on which specific properties fall
  under the "required" exception.
- **Three-character hexadecimal color notation is preferred where the
  color value permits it** — "Use 3 character hexadecimal notation where
  possible." Stated reason: "For color values that permit it, 3 character
  hexadecimal notation is shorter and more succinct." — a compression
  argument, not a correctness one.
- **Indentation is 2 spaces, uniformly, with no stated rationale** —
  "Indent by 2 spaces at a time." / "Don't use tabs or mix tabs and spaces
  for indentation." Applies identically across HTML and CSS in this single
  guide; unlike several rules above, no justification accompanies this
  specific pair of sentences in the passage confirmed here.

**A closing observation worth flagging as a hedge, not a claim**: the
guide's own closing "Parting Words" section reads, in part: "*Be
consistent.* If you're editing code, take a few minutes to look at the
code around you and determine its style... The point of having style
guidelines is to have a common vocabulary of coding so people can
concentrate on what you're saying rather than on how you're saying it...
If code you add to a file looks drastically different from the existing
code around it, it throws readers out of their rhythm." This closing
sentiment strongly resembles the well-known "a foolish consistency" theme
associated with PEP 8 and Google's own Python guide — but that specific
resemblance has not been re-verified word-for-word against either of
those documents here, so it is recorded as a noted similarity in spirit,
not a claim of shared or copied wording.

**Scope note**: this is Google's own convention for Google's own HTML/CSS
codebases, not an HTML or CSS specification and not a claim about how the
wider web-development community formats markup or stylesheets — many
widely used frontend codebases (including projects cataloged elsewhere in
this repository) use double-quoted CSS, `id`-heavy markup, or 4-space
indentation, all of which this guide argues against.

## Markdown: a documentation-writing convention, not a syntax-restriction guide

Read directly from Google's public Markdown Style Guide
(google.github.io/styleguide/docguide/style.html) — canonical URL
independently confirmed two ways before quoting began: by reading the page
itself (title "Markdown style guide," a GitHub "Improve this page" link
pointing at `docguide/style.md` in the same `google/styleguide` repo) and
by re-finding the same URL from the link text "Markdown Style Guide" on
Google's own style-guide index page, rather than trusting the URL as
handed down secondhand. This is Google's own convention for its
documentation corpus, one company's stated preferences, not a
Markdown-industry-wide or CommonMark-spec-level standard. Unlike every
programming-language guide above, this one is not primarily about
restricting what a language allows — Markdown barely has restrictable
syntax — it is about how a large, multi-author documentation corpus stays
searchable, scannable, and maintainable over time, closer in spirit to a
writing style guide than a syntax guide. Cross-checking method: two
independent full read-throughs were run blind to each other, followed by
targeted re-fetches for wording gaps or single-pass-only findings — the
same method used in the JSON and HTML/CSS sections above. Two rules below
(the anchor-link rationale for unique heading names, and the short-list
numbering rationale) surfaced the same interesting case of this method
actually helping: the two initial passes each quoted a different half of
what turned out to be one continuous sentence, and only a targeted
re-fetch revealed they were fragments of the same sentence rather than
two competing or partial rationales.

- **A recommended document skeleton, ending in a dedicated
  "miscellaneous links" section** — "In general, documents benefit from
  some variation of the following layout:" — "The first heading should be
  a level-one heading, ideally the same or nearly the same as the
  filename." / "The first level-one heading is used as the page `<title>`."
  The skeleton's last piece: "`## See also`: Put miscellaneous links at
  the bottom for the user who wants to know more or didn't find what they
  needed." — an explicit "put the noise at the end, not the top" ordering
  rule.
- **An 80-character line-length convention, justified by habit rather
  than a technical constraint, with named exceptions** — "Markdown content
  follows the residual convention of an 80-character line limit." Stated
  reason, informal in tone compared to most rationales in this catalog:
  "Why? Because it's what most of us do for code." "Exceptions to the
  80-character rule include:" links, tables, headings, and code blocks —
  content where forcing a wrap would break the content itself rather than
  just the prose around it.
- **Trailing whitespace is banned for two distinct reasons — a spec-level
  correctness risk and a mundane tooling reality** — "Don't use trailing
  whitespace. Use a trailing backslash to break lines." The correctness
  risk: "The CommonMark spec decrees that two spaces at the end of a line
  should insert a `<br />` tag." — meaning trailing whitespace is not just
  untidy, it can silently change rendered output under the CommonMark
  spec. The tooling reality, a separate and more mundane reason: "many
  directories have a presubmit check for trailing whitespace, and many
  IDEs will clean it up anyway."
- **ATX-style headings (`#`, `##`) are required; Setext-style underline
  headings (`===`, `---`) are rejected as ambiguous** — "Headings with `=`
  or `-` underlines can be annoying to maintain and don't fit with the
  rest of the heading syntax." The guide then illustrates the ambiguity
  concern with a rhetorical question rather than leaving it as an
  abstract claim: "An editor has to ask: Does `---` mean H1 or H2?" The
  guide's own in-page example is annotated
  "DO NOT DO THIS." directly beneath a Setext-style heading shown as a
  counter-example.
- **Every heading, including sub-sections, needs a unique and fully
  descriptive name — the rationale is about anchor links, not
  readability** — "Use unique and fully descriptive names for each
  heading, even for sub-sections." Full stated reason (see the
  cross-check note above on how this sentence was reconstructed): "Since
  link anchors are constructed from headings, this helps ensure that the
  automatically-constructed anchor links are intuitive and clear." A
  vague heading like "Overview" repeated across sections would collide or
  produce unintuitive anchor URLs; the rule is a namespacing concern
  wearing a readability rule's clothing.
- **Exactly one H1 per document, functioning as the title; everything
  else is H2 or deeper** — "Use one H1 heading as the title of your
  document. Subsequent headings should be H2 or deeper." No further
  rationale is given beyond the rule itself in the passage confirmed here.
- **Ordered lists get one of two opposite numbering conventions depending
  on whether the list is expected to change** — long or frequently-edited
  lists: "For longer lists that may change, especially long nested lists,
  use \"lazy\" numbering:" (every item literally marked `1.`), justified
  because "Markdown is smart enough to let the resulting HTML render your
  numbered lists correctly" regardless of the literal digits used in
  source. Short, stable lists get the opposite treatment: "However, if the
  list is small and you don't anticipate changing it, prefer fully
  numbered lists, because it's nicer to read in source." Two different
  rules for the same syntax feature, each with its own distinct
  rationale — and, like the anchor-link rationale above, this second
  sentence was also reconstructed from two initial passes that had each
  quoted only half of it, then confirmed whole on a third, targeted pass.
- **Nested list items take a 4-space indent, for both numbered and
  bulleted lists** — "When nesting lists, use a 4-space indent for both
  numbered and bulleted lists:" — a single indent width applied uniformly
  regardless of which list-marker style is nested.
- **Inline code backticks are for literal rendering, not just
  decoration** — "`Backticks` designate `inline code` that will be
  rendered literally. Use them for short code quotations, field names,
  and more:" — confirmed as one continuous two-sentence passage on direct
  re-verification, after two independent passes each surfaced only one of
  the two sentences.
- **Fenced code blocks are strongly recommended over 4-space-indented
  ones, for three separately stated reasons** — "Four-space indenting is
  also interpreted as a code block," but "we strongly recommend fencing
  for all code blocks" because: "You cannot specify the language. Some
  Markdown features are tied to language specifiers." / "The beginning
  and end of the code block are ambiguous." / "Indented code blocks are
  harder to search for in Code Search." Three independently stated
  reasons — a missing capability, an ambiguity/correctness concern, and a
  tooling-specific searchability concern — stacked behind one
  recommendation rather than a single justification.
- **The language must be declared explicitly on a fenced code block** —
  "It is best practice to explicitly declare the language, so that
  neither the syntax highlighter nor the next editor must guess." A rule
  justified for two different readers at once: the automated tool
  (syntax highlighter) and the next human editor.
- **Link text must be written for scanning readers, not linear ones —
  with a concrete rewriting instruction, not just a prohibition** —
  stated reason first: "Users often do not read documents; they scan
  them." Then the prohibition: titling a link "here," "link," or simply
  duplicating the target URL "tells the hasty reader precisely nothing
  and is a waste of space." Then the guide gives an actual rewriting
  procedure rather than leaving the fix to the reader's judgment:
  "Instead, write the sentence naturally, then go back and wrap the most
  appropriate phrase with the link:"
- **Reference-style links trade source-scannability for prose
  readability — the guide states the cost of its own recommendation** —
  "Use reference links where the length of the link would detract from
  the readability of the surrounding text if it were inlined." The guide
  does not pretend this is free: "Reference links make it harder to see
  the destination of a link in source text, and add additional syntax."
  Placement rule for the reference definition itself: "We recommend
  putting reference link definitions just before the next heading, at the
  end of the section in which they're first used."
- **Tables are reserved for data that is genuinely tabular and scannable;
  lists are the stated default otherwise** — "Use tables when they make
  sense: for the presentation of tabular data that needs to be scanned
  quickly." / "Avoid using tables when your data could easily be
  presented in a list." Stated reason: "Lists are much easier to write
  and read in Markdown."
- **The guide's closing rule pushes the opposite direction of the
  HTML/CSS guide catalogued above it in this same file** — "Please prefer
  standard Markdown syntax wherever possible and avoid HTML hacks."
  Stated reason: "Every bit of HTML hacking reduces the readability and
  portability of our Markdown corpus." Where the HTML/CSS guide above
  spends its entire page prescribing how to write HTML and CSS well, this
  guide's final rule is to avoid writing HTML at all inside a Markdown
  document — the two guides, read together, describe adjacent territories
  with a policed border between them rather than a shared one.

**Scope note**: this is Google's own documentation convention for its own
corpus, not a Markdown or CommonMark specification and not a claim about
how the wider open-source or technical-writing community formats
Markdown — many widely used README and documentation corpora (including
projects cataloged elsewhere in this repository) do not enforce an
80-character line limit, lazy numbering, or a hard ban on embedded HTML,
all of which this guide recommends.

## C#: a guide that names its own borrowed lineage, and an unnamed one its examples give away

Read directly from Google's public C# Style Guide
(google.github.io/styleguide/csharp-style.html) — canonical URL
independently confirmed two ways before quoting began: by the link text
"C# Style Guide" on Google's own style-guide index page, and by the
page's own GitHub "Improve this page" edit link, which points at
`csharp-style.md` in the same `google/styleguide` repository. This is
Google's own convention for its own C# codebases, one company's stated
preferences, not a C#-community-wide or Microsoft-specification-level
standard — though this one explicitly defers to another company's
standard for its core naming convention rather than inventing its own
(see below). The Swift section further down does the same thing more
strongly, and the two together are discussed in the Cross-language
pattern section. Cross-checking
method: two independent full read-throughs, followed by targeted
re-fetches for wording gaps and single-pass-only findings — the same
method used throughout this file. One specific claim was checked before
being written up here at all: a suggestion (from outside this
cross-check process) that this guide carries Unity-game-engine-specific
content. A full-page search for the literal words "Unity" and "game"
found neither anywhere on the page; the only trace is discussed below,
and it turned out to be more interesting, and more precisely stated, than
the original suggestion.

- **The naming convention explicitly defers to Microsoft's own C#
  guidelines rather than being Google-invented** — "Names of classes,
  methods, enumerations, public fields, public properties, namespaces:
  PascalCase." / "Names of local variables, parameters: camelCase." /
  "Names of private, protected, internal and protected internal fields
  and properties: `_camelCase`." Stated reason, confirmed identically
  across both independent passes: "Naming rules follow Microsoft's C#
  naming guidelines." This catalog's JSON section above cites RFC 3339
  and ISO 8601 for narrow date and duration formatting, but this rule
  defers an entire naming-convention system — not just one formatting
  detail — to another organization's published standard, by name, as the
  stated rationale. The Swift section below records a second, stronger
  instance of the same move; the two are compared in the Cross-language
  pattern section.
- **Interfaces get an `I` prefix; acronyms count as one word for casing
  purposes, not letter-by-letter** — "Names of interfaces start with `I`,
  e.g. `IInterface`." / "For casing, a \"word\" is anything written
  without internal spaces, including acronyms. For example, `MyRpc`
  instead of `MyRPC`." A specific, machine-checkable definition of what
  counts as a single "word" for casing purposes — closing off the
  otherwise-ambiguous question of whether an acronym like RPC should stay
  all-caps inside a PascalCase or camelCase identifier.
- **Filenames are PascalCase and should match their main class; one core
  class per file is the stated default** — "Filenames and directory
  names are `PascalCase`, e.g. `MyFile.cs`." / "Where possible the file
  name should be the same as the name of the main class in the file, e.g.
  `MyClass.cs`." / "In general, prefer one core class per file."
- **A single, fixed, fifteen-keyword modifier order, with no stated
  exceptions** — "Modifiers occur in the following order: `public
  protected internal private new abstract virtual override sealed static
  readonly extern unsafe volatile async`." No rationale accompanies this
  sentence in the passage confirmed here; the rule is stated as a bare,
  total ordering.
- **`using` declarations are alphabetical, with one named exception for
  `System`** — "Namespace `using` declarations go at the top, before any
  namespaces." / "`using` import order is alphabetical, apart from
  `System` imports which always go first." A single, unconditional
  carve-out inside an otherwise mechanical alphabetical rule.
- **Class members are ordered on two independent axes at once — by kind,
  then by access level within each kind** — first axis: "Group class
  members in the following order:" nested types/enums/delegates/events,
  then static/const/readonly fields, then fields and properties, then
  constructors and finalizers, then methods. Second axis, applied inside
  each of those groups: "Within each group, elements should be in the
  following order:" Public, Internal, Protected internal, Protected,
  Private. A closing preference layered on top of both: "Where possible,
  group interface implementations together."
- **Whitespace and brace rules are stated as directly inherited from
  Google's own Java guide, not independently derived** — "A maximum of
  one statement per line." / "A maximum of one assignment per statement."
  / "Indentation of 2 spaces, no tabs." / "Column limit: 100." / "Braces
  used even when optional." / "No line break before opening brace." / "No
  line break between closing brace and `else`." Stated origin, confirmed
  identically across both independent passes: "Developed from Google Java
  style." This catalog's own Java section above independently confirmed
  a 100-character column limit and mandatory braces as Java's own rules —
  the C# guide names Java as its source for the same pair of rules here,
  rather than this catalog inferring the resemblance from the outside.
- **`const` first, `readonly` as fallback, named constants over magic
  numbers** — "Variables and fields that can be made `const` should
  always be made `const`." / "If `const` isn't possible, `readonly` can
  be a suitable alternative." / "Prefer named constants to magic
  numbers."
- **Expression-bodied properties are preferred for single-line read-only
  properties, and the guide dates its own rule as provisional** — "For
  single line read-only properties, prefer expression body properties
  (`=>`) when possible." / "For everything else, use the older `{ get;
  set; }` syntax." / "Don't use on method definitions." The guide then
  attaches a self-dated commitment to revisit the rule: "This will be
  reviewed when C# 7 is live, which uses this syntax heavily." C# 7 has
  since shipped (in 2017, per Microsoft's own release history rather than
  anything stated on this page), so the future-tense sentence now reads
  as a fossil of the guide's own drafting period, left in place rather
  than updated or removed. It is not an isolated slip: see the
  struct-defaults rule below, where the guide again defers a decision to
  a stated future condition. Two such sentences in one guide look less
  like an oversight than like a house habit of committing open questions
  to the text rather than resolving or hiding them.
- **Struct return values prefer a success-flag-plus-`out` shape over
  nullables — and the guide openly leaves the better answer unbuilt** —
  "Prefer returning a 'success' boolean value and a struct `out` value."
  Nullables are permitted only under a stated two-part condition: "Where
  performance isn't a concern and the resulting code significantly more
  readable (e.g. chained null conditional operators vs deeply nested if
  statements) nullable structs are acceptable." The guide then names its
  own discomfort with the concession it just made: "Nullable structs are
  convenient, but reinforce the general 'null is failure' pattern Google
  prefers to avoid." And then defers the fix: "We will investigate a
  `StatusOr` equivalent in the future, if there is enough demand." This
  is the second future-deferred commitment in the same guide (the
  expression-bodied-properties C#-7 note above is the first), and the
  more revealing of the two — the guide states a house-wide principle
  ("null is failure" is to be avoided), admits its own current rule
  partially violates that principle, allows the violation anyway on
  pragmatic grounds, and records the unbuilt alternative in the open,
  conditional on demand that may never materialize.
- **"Almost always use a class"; structs are reserved for small,
  short-lived, value-like data — illustrated with three real Unity
  engine type names, though the guide never names Unity itself** —
  "Structs are always passed and returned by value." / "Almost always
  use a class." / "Consider struct when the type can be treated like
  other value types" — stated reason: "if instances of the type are
  small and commonly short-lived or are commonly embedded in other
  objects." The guide's own example list: "Good examples include
  Vector3, Quaternion and Bounds." `Vector3`, `Quaternion`, and `Bounds`
  are not generic C# or .NET types — they are specific, well-known types
  from Unity's own scripting API (`UnityEngine.Vector3`,
  `UnityEngine.Quaternion`, `UnityEngine.Bounds`). Despite this, a
  full-page search found "Unity" nowhere as a standalone capitalized
  word, and "game" nowhere at all; the string "unity" occurs exactly once
  on the page, lowercased inside an example project name in an unrelated
  namespace-naming rule — "For leaf 'application' code, such as
  `unity_app`, namespaces are not necessary." — which is an incidental
  example identifier, not a game-development guidance point.
  The guide's example choices reveal a likely origin or audience the
  guide's own text never states outright — a pattern worth recording
  precisely as "the examples say Unity, the prose never does," rather
  than as a claim that this is officially a Unity or game-development
  style guide, which it does not present itself as.
- **Extension methods are discouraged by default, not merely
  situational** — "Only use an extension method when the source of the
  original class is not available" / "or else when changing the source
  is not feasible." Stated reason: "Be aware that using extension
  methods always obfuscates the code, so err on the side of not adding
  them." An unconditional claim ("always obfuscates") used to justify a
  default-off stance rather than case-by-case judgment.
- **`ref` and `out` carry several independent, narrowly scoped
  restrictions — and one uses British rather than American spelling** —
  "Use `out` for returns that are not also inputs." / "Place `out`
  parameters after all other parameters in the method definition." /
  "`ref` should be used rarely, when mutating an input is necessary." /
  "Do not use `ref` as an `optimisation` for passing structs." / "Do not
  use `ref` to pass a modifiable container into a method. `ref` is only
  required when the supplied container needs be replaced with an
  entirely different container instance." The spelling "optimisation"
  (rather than "optimization") is confirmed as written on the page — a
  minor textual detail, noted here rather than silently normalized to
  American spelling, in keeping with this catalog's practice of quoting
  exactly what a source says rather than what a reader might expect it to
  say.
- **LINQ: single-line calls preferred over long chains; member syntax
  preferred over SQL-style query keywords** — "In general, prefer single
  line LINQ calls and imperative code, rather than long chains of LINQ."
  Stated reason: "Mixing imperative code and heavily chained LINQ is
  often hard to read." A second, narrower preference in the same
  section: prefer member extension methods over SQL-style LINQ keywords,
  e.g. `myList.Where(x)` over `myList where x`. A third: avoid
  `Container.ForEach(...)` for anything longer than a single statement.
- **`var` is encouraged or discouraged by a stated readability test, not
  a blanket rule either way** — "Use of `var` is encouraged if it aids
  readability by avoiding type names that are noisy, obvious, or
  unimportant." Encouraged specifically: when the type is obvious, or for
  transient variables passed directly to other methods. Discouraged
  specifically: when working with basic types, or with compiler-resolved
  built-in numeric types. The same "restrict a permissive language
  feature along a stated readability axis rather than ban or allow it
  outright" shape seen in this catalog's TypeScript `any`-avoidance rule
  above, applied here to type inference rather than to a loose type.

Several further narrowly scoped rules were confirmed but are compressed
here rather than given full entries: calling a delegate should use
`Invoke()` with the null-conditional operator (`SomeDelegate?.Invoke()`),
justified as both more readable at the call site and "concise and robust
against threading race conditions"; Object Initializer syntax is
reserved for "plain old data" types and avoided for classes or structs
with constructors; string concatenation should default to whatever reads
most easily, with a stated performance caveat that chained `operator+`
"will be slower and cause significant memory churn" and that
`StringBuilder` is faster for multiple concatenations; and a named class
type is preferred over `Tuple<>` as a return type, particularly for
complex return shapes.

**Scope note**: this is Google's own convention for Google's own C#
codebases, not a C# language specification and not a claim about how the
wider .NET or Unity-development community writes C# — many widely used
C# codebases (including Unity projects themselves, and projects cataloged
elsewhere in this repository) use `PascalCase` for private fields, embrace
`var` more broadly, or follow Microsoft's own .NET naming conventions
directly rather than this guide's `_camelCase` private-field convention.

## Swift: a guide hosted outside its own repository, which absorbs another company's document by reference

Read directly from Google's public Swift Style Guide
(google.github.io/swift/) — canonical URL independently confirmed two
ways before quoting began: by the link text "Swift Style Guide" on
Google's own style-guide index page, and by the README of the `gh-pages`
branch of `github.com/google/swift`, which states it is the source for
this site. This is Google's own convention for its own Swift code, one
company's stated preferences, not a Swift-community-wide standard —
though it defers to Apple more completely than any guide in this catalog
defers to anyone (see the first rule below).

**A structural anomaly worth recording**: of the guides read in this
file, this is the only one that does not live under
`google.github.io/styleguide/`. It is
published from the `gh-pages` branch of `google/swift` — a repository
whose main branch is a fork of the Swift language itself, archived
read-only in January 2023. The style guide's branch outlived the
repository's stated purpose. Nothing in the guide's content depends on
this, but a reader trying to locate or contribute to the guide from the
`google/styleguide` repo alone would not find it.

**A methodological upgrade, and an honest note about what it implies for
the sections above**: for this guide the raw Markdown source is directly
retrievable (`raw.githubusercontent.com/google/swift/gh-pages/index.md`),
so every load-bearing quotation below was checked against literal source
text rather than against a rendered page mediated by a summarizing
fetch layer. That is a stronger guarantee than any earlier section in
this file had available, and it is stated here rather than quietly
enjoyed: the character-level caveats recorded in the Shell and JavaScript
sections above exist precisely because those guides offered no such raw
route. Where the raw source carries Markdown emphasis markup (for
instance the semicolon rule is written with `**not used**` and the
trailing-comma rule with `_required_`), the rendered wording is quoted
below and the emphasis is described rather than reproduced.

- **Apple's naming guidelines are not merely followed — they are declared
  to be part of this document** — "Apple's [official Swift naming and API
  design guidelines](https://swift.org/documentation/api-design-guidelines/)
  hosted on swift.org are considered part of this style guide and are
  followed as if they were repeated here in their entirety." This is
  incorporation by reference, and it is materially stronger than the
  closest parallel in this catalog: the C# section above records "Naming
  rules follow Microsoft's C# naming guidelines," which commits to
  obeying an external document; this one declares the external document
  to *be* inside Google's own. The guide's opening sentence sets up the
  same lineage more softly — "This style guide is based on Apple's
  excellent Swift standard library style and also incorporates feedback
  from usage across multiple Swift projects within Google." Note the two
  registers are doing different work: "is based on" describes provenance,
  "are followed as if they were repeated here in their entirety" creates
  an obligation. Both were confirmed against the raw Markdown source.
- **Semicolons are banned outright, with the permitted remainder stated
  as a closed set** — "Semicolons (`;`) are not used, either to terminate
  or separate statements." (the source emphasizes "not used"). Rather
  than leave the exception surface implicit, the guide closes it
  explicitly: "In other words, the only location where a semicolon may
  appear is inside a string literal or a comment." A prohibition plus an
  exhaustive statement of where the character may still legally occur.
- **A 100-character column limit, matching the Java and C# guides above** —
  "Swift code has a column limit of 100 characters." This is the third
  guide in this catalog to land on 100 specifically — Java's own limit and
  the C# guide's "Column limit: 100" (which the C# guide attributes to
  "Developed from Google Java style"). The Swift guide does not state
  where its own number came from, so the three-way agreement is recorded
  here as an observation, not as a claimed inheritance chain.
- **Trailing commas are required in vertically laid-out literals, for a
  diff-hygiene reason** — "Trailing commas in array and dictionary
  literals are required when each element is placed on its own line."
  (the source emphasizes "required"). Stated reason: "Doing so produces
  cleaner diffs when items are added to those literals later." This is
  the second rule in this catalog whose stated justification is diff
  cleanliness — the HTML/CSS section's trailing-whitespace rule was the
  first, and was noted there as the only such case at the time. Two
  independent guides reaching for the same justification, in rules that
  are otherwise unrelated (whitespace hygiene vs. literal syntax), makes
  "keep the diff readable" a genuine recurring rationale in this corpus
  rather than a one-off.
- **Force-unwrapping and force-casting are named as code smells, and a
  comment is required where they survive** — "Force-unwrapping and
  force-casting are often code smells and are strongly discouraged."
  / "Unless it is extremely clear from surrounding code why such an
  operation is safe, a comment should be present that describes the
  invariant that ensures that the operation is safe." The rule does not
  ban the construct; it prices it, requiring the author to write down the
  invariant that makes it safe.
- **Implicitly unwrapped optionals are called inherently unsafe** —
  "Implicitly unwrapped optionals are inherently unsafe and should be
  avoided whenever possible in favor of non-optional declarations or
  regular `Optional` types." The guide then carves out named exceptions
  rather than leaving the rule absolute.
- **Sentinel values are rejected in favour of `Optional`** — "Sentinel
  values are avoided when designing algorithms (for example, an "index"
  of −1 when an element was not found in a collection)." Stated reason:
  sentinel values "can easily and accidentally propagate through other
  layers of logic" because the type system does not distinguish them from
  valid data. (The raw source writes the −1 with a Unicode minus sign
  rather than an ASCII hyphen — recorded because this catalog quotes what
  a source says rather than what a reader expects.)
- **Errors are thrown rather than folded into the return type** — "Error
  types are used when there are multiple possible error states." /
  "Throwing errors instead of merging them with the return type cleanly
  separates concerns in the API." A separation-of-concerns argument about
  API shape, not a stylistic one.
- **`guard` is preferred for early exits, on a stated readability
  argument** — "A guard statement, compared to an `if` statement with an
  inverted condition, provides visual emphasis that the condition being
  tested is a special case that causes early exit from the enclosing
  scope." The guide's fuller rationale names the failure mode it is
  avoiding: with `guard`, "failure conditions are closely coupled to the
  conditions that trigger them and the main logic remains flush left
  within its scope," whereas without it "the main logic is buried at an
  arbitrary nesting level and the thrown errors are separated from their
  conditions by a great distance." (Both independent passes also reported
  the phrase "pyramid of doom" in this section, but disagreed on whether
  the surrounding quotation marks are straight or curly; the phrase is
  therefore described rather than quoted with glyph-level precision.)
- **Naming conventions are explicitly not a substitute for access
  control** — "Restricted access control (`internal`, `fileprivate`, or
  `private`) is preferred for the purposes of hiding information from
  clients, rather than naming conventions." Underscore-prefix conventions
  are confined to "rare situations" where a declaration must be given
  higher visibility than wanted in order to work around a language
  limitation. A rule that tells the reader which of two available
  mechanisms is load-bearing, rather than merely styling one of them.
- **Imports name exactly what is used, and never rely on transitive
  availability** — "A source file imports exactly the top-level modules
  that it needs; nothing more and nothing less." / "Imports of whole
  modules are preferred to imports of individual declarations or
  submodules." / "Import statements are not line-wrapped." The rule is
  illustrated with the platform the guide openly targets: "If a source
  file uses definitions from both `UIKit` and `Foundation`, it imports
  both explicitly; it does not rely on the fact that some Apple
  frameworks transitively import others as an implementation detail."
- **Documentation comments use `///`, and Javadoc-style blocks are
  prohibited** — "Documentation comments are written using the format
  where each line is preceded by a triple slash (`///`)." /
  "Javadoc-style block comments (`/** ... */`) are not permitted." A
  syntax available in the language is closed off in favour of a single
  house form — the same shape as the language-restriction pattern running
  through this file, applied to comments rather than to code.
- **At most one statement per line, with a single-statement-block
  exception** — "There is at most one statement per line, and each
  statement is followed by a line break, except when the line ends with a
  block that also contains zero or one statements." The guide adds an
  always-available escape hatch: "Wrapping the body of a single-statement
  block onto its own line is always allowed."
- **Line-wrapping is governed by cardinal rules, one of which forbids
  mixed orientation** — "If the entire declaration, statement, or
  expression fits on one line, then do that." / "Comma-delimited lists are
  only laid out in one direction: horizontally or vertically." /
  "In other words, all elements must fit on the same line, or each element
  must be on its own line." The +2-indent convention is justified by the
  visual artefact it avoids: it "prevents the zig-zag effect that would be
  present if the arguments are indented based on opening" delimiters.

**Two hypotheses were tested against this guide and both came back
negative — recorded because a negative result is a result.** Both came
from patterns observed in the C# section above, and checking a second
guide is what distinguishes "a characteristic of that guide" from "a
characteristic of Google's guides":

1. *Does this guide flag its own rules as provisional, as the C# guide
   twice does?* **No.** A full-text scan for deferral language ("will be
   reviewed", "for now", "subject to change", "we will investigate",
   "revisit", "not yet", "under review", and roughly thirty further
   variants) returned no instance of the guide deferring one of its own
   rules. Two apparent hits were the substring "pending" inside
   "depending"; other uses of "future" and "currently" refer to user code
   or to the Swift language, not to the guide's rules. The closest thing
   is a blanket meta-statement in the introduction — "It is a living
   document and the basis upon which the formatter is implemented" —
   which says the document evolves without marking any specific rule as
   unsettled. The C# guide's habit of recording open questions inline
   therefore stands, on present evidence, as a characteristic of that
   guide rather than a house style across Google's guides.
2. *Do this guide's examples reveal a platform its prose never names, as
   the C# guide's Unity-typed struct examples do?* **No — the opposite.**
   The examples are heavily Apple-platform (`UIViewController`,
   `UITableView`, `UIScrollView`, `UIView`, `UIColor`, `URLSession`,
   `CGFloat`, `NSCoder`, `NSRegularExpression`, `@IBOutlet`), but the
   prose names the platform openly: "Apple" appears in the introduction
   and again in the delegate-methods section, and `UIKit`, `Foundation`
   and Xcode are all named in running prose. There is no gap between what
   the examples assume and what the text admits. ("macOS", "SwiftUI" and
   "AppKit" are absent; "Cocoa" appears only inside a `developer.apple.com`
   link URL, not in prose — an earlier pass asserted a prose phrase
   containing "Cocoa" that a targeted re-check could not reproduce, so it
   is excluded here as unconfirmed.) The C# guide's silent-platform
   pattern is thus *not* general; it is specific to that guide, which
   makes it more interesting, not less.

**Scope note**: this is Google's own convention for Google's own Swift
code, not a Swift language specification, not Apple's own guidance
(though it incorporates Apple's naming document by reference), and not a
claim about how the wider Swift community writes Swift — many widely used
Swift codebases permit semicolon-free-but-differently-wrapped styles, use
a 120-column or unlimited line budget, or adopt SwiftLint defaults that
differ from the rules above.

## Objective-C: a guide with a named "Principles" section — including a rule about which rules to have

Read directly from Google's public Objective-C Style Guide
(google.github.io/styleguide/objcguide.html) — canonical URL confirmed
two ways: the link on Google's style-guide index page, and the page's own
GitHub edit link pointing at `objcguide.md` in `google/styleguide`. Like
the Swift section above, every load-bearing quotation below was verified
against the raw Markdown source
(`raw.githubusercontent.com/google/styleguide/gh-pages/objcguide.md`)
rather than a summarizer-mediated rendering, across two independent
passes plus targeted re-checks. This is Google's own convention for its
own Objective-C and Objective-C++ code, one company's stated preferences,
not an Objective-C-community-wide standard.

- **The only guide read in this file with a section literally titled
  "Principles"** — four named principles stated before any concrete
  rule. (The Markdown guide above also opens with philosophy-flavored
  sections — "Minimum viable documentation", "Better is better than
  best" — but those were recorded there as unread, so the comparison
  stops at the section titles.) The four: "Optimize for the reader, not the writer"
  ("Codebases often have extended lifetimes and more time is spent
  reading the code than writing it."), "Be consistent" ("Using one style
  consistently throughout a codebase lets engineers focus on other (more
  important) issues."), "Be consistent with Apple SDKs" ("Consistency
  with the way Apple SDKs use Objective-C has value for the same reasons
  as consistency within our code base."), and the remarkable fourth one
  below. The C++ section above records the reader-over-writer principle
  as something that guide states; here it is elevated to a named,
  numbered principle. (A fifth subsection, "Inclusive Language", appears
  in the same Principles block but was not read closely.)
- **"Style rules should pull their weight" — a meta-rule governing which
  rules the guide itself is allowed to contain** — "The benefit of a
  style rule must be large enough to justify asking engineers to
  remember it." The guide then explains that this principle "mostly
  explains the rules we don't have, rather than the rules we do: for
  example, goto contravenes many of the following principles, but is not
  discussed due to its extreme rarity." None of the sections read so far
  in this file state a cost-benefit test for the guide's own rule set, or
  explain an *absence* of rules (unread sections elsewhere may — see each
  section's unread list). The guide is reasoning in public about its own
  scope, the same self-aware register as the C# guide's provisional-rule
  notes, but aimed at the rulebook itself rather than at any one rule.
- **A third deference to the platform vendor — and the weakest of the
  three, completing a gradient** — "Apple has already written a very
  good, and widely accepted, Cocoa Coding Guidelines for Objective-C.
  Please read it in addition to this guide." And in the Naming section:
  "Names should be as descriptive as possible, within reason. Follow
  standard Objective-C naming rules." — the latter linking to Apple's
  same Coding Guidelines document. Three guides in this file now defer to
  the platform vendor's published standard, at three distinct strengths:
  Objective-C says *read it alongside* this guide; C# says naming rules
  *follow* Microsoft's; Swift *incorporates* Apple's document as if
  repeated in its entirety. Once again the strongest deference sits in
  the naming section — see the Cross-language pattern section below.
- **The platform vendor's namespace reservation shapes the prefix
  rule** — "Classes and protocols in code shared across multiple
  applications must have an appropriate prefix (e.g. GTMSendMessage)."
  followed by: "WARNING: Apple reserves two-letter prefixes—see
  Conventions in Programming with Objective-C—so prefixes with a minimum
  of three characters are considered best practice." A naming rule whose
  boundary is drawn by another company's reservation of part of the
  namespace — not a style preference at all, but a collision-avoidance
  rule against the platform owner.
- **A 100-column line limit** — "The maximum line length for Objective-C
  files is 100 columns." The fourth guide in this file to land on 100
  (after Java, C#, and Swift). As with Swift, no origin for the number is
  stated, so the four-way agreement remains an observation rather than a
  claimed inheritance chain.
- **Objective-C exceptions are not thrown but must still be caught** —
  "Don't `@throw` Objective-C exceptions, but you should be prepared to
  catch them from third-party or OS calls." An asymmetric rule: the
  feature is banned on the producing side while remaining mandatory to
  handle on the consuming side, because the surrounding ecosystem still
  uses it — a shape none of the outright bans elsewhere in this file
  (C++ exceptions, `with`, `eval`, semicolons) have needed.
- **`BOOL`'s platform-dependent definition drives a correctness rule,
  with the platforms named openly in prose** — "`BOOL` on some Apple
  platforms (notably Intel macOS, watchOS, and 32-bit iOS) is defined as
  a signed `char`, so it may have values other than `YES` (`1`) and `NO`
  (`0`)." / "When converting a general integral value to a BOOL, use
  conditional operators to return a YES or NO value." Like the Swift
  guide and unlike the C# guide, the prose names its platforms outright —
  further evidence that the C# guide's silent-platform pattern is
  specific to that guide.
- **Sending a message to `nil` is defined behavior, and the guide says
  exactly what it returns** — "Sending a message to nil reliably returns
  nil as a pointer, zero as an integer or floating-point value, structs
  initialized to 0, and _Complex values equal to {0, 0}." A
  language-semantics statement recorded as the factual basis for the
  guide's nil-handling rules rather than as a rule itself.
- **Two-space indentation, spaces only** — "Use only spaces, and indent
  2 spaces at a time." / "Do not use tabs in your code." The same
  2-space convention recorded in the HTML/CSS and C# sections above (the
  Swift section above records a +2 continuation-line rule but not the
  guide's base indentation, so Swift is not cited as a confirmed parallel
  here); as with the column limit, recorded as recurrence, not lineage.
- **Small functions preferred, stated without a numeric ceiling** —
  "Prefer small and focused functions." Unlike the C++ guide's ~40-line
  figure or the Shell guide's 100-line rewrite trigger, no number is
  attached in the sentence confirmed here.

**Scope note**: this is Google's own convention for Google's own
Objective-C code, not an Objective-C language specification and not
Apple's own guidance (though it points to Apple's twice), and not a claim
about how the wider iOS/macOS community writes Objective-C — and given
that Apple itself has directed new development toward Swift for years,
this guide governs an aging surface, which the guide itself does not
discuss.

## R: a style guide that is literally a patch against someone else's

Read directly from Google's public R Style Guide
(google.github.io/styleguide/Rguide.html) — canonical URL confirmed via
Google's style-guide index page and the page's own GitHub edit link
(`Rguide.md` in `google/styleguide`). Every quotation below was verified
against the raw Markdown source
(`raw.githubusercontent.com/google/styleguide/gh-pages/Rguide.md`) across
two passes. This guide is by far the shortest read in this file — short
enough that, unusually, the two passes between them covered essentially
every rule sentence it contains.

- **The entire guide is declared to be a fork of a community document —
  not a platform vendor's** — "The Google R Style Guide is a fork of the
  [Tidyverse Style Guide](https://style.tidyverse.org/) by Hadley Wickham
  [license](https://creativecommons.org/licenses/by-sa/2.0/)." /
  "Google modifications were developed in collaboration with the internal
  R user community." This is a fourth instance of a Google guide building
  on an external standard, and it breaks the pattern the first three
  suggested in two ways at once. First, the external authority is not a
  platform vendor: the Tidyverse Style Guide is a community standard
  associated with an individual author, not the owner of the language or
  platform. Second, the mechanism differs in kind from all three earlier
  instances: a *fork* starts from a copy of the external document and
  diverges from it, whereas Swift's incorporation-by-reference keeps the
  external document live and authoritative inside the guide. A fork can
  contradict its upstream; an incorporation cannot. See the revised
  Cross-language pattern section below.
- **What remains, once the upstream is subtracted, is mostly a list of
  disagreements** — the guide's own sections are largely the points where
  Google departs from what it forked: function naming
  ("Google prefers identifying functions with `BigCamelCase` to clearly
  distinguish them from other objects."), private-function naming ("The
  names of private functions should begin with a dot. This helps
  communicate both the origin of the function and its intended use."),
  and the rules below. Structurally this is a new type in this file: not
  a self-contained rulebook but a diff against another organization's.
- **The guide narrates a reversal of its own former rule, in the open** —
  "We previously recommended naming objects with `dot.case`. We're moving
  away from that, as it creates confusion with S3 methods." Where the C#
  guide's two future-deferred notes commit *forward* to reconsidering a
  rule, this sentence records a reconsideration already carried out —
  the past-tense counterpart of the same habit of leaving the guide's
  decision history visible in its text rather than silently rewriting it.
- **`attach()` is rejected in a single sentence** — "The possibilities
  for creating errors when using `attach()` are numerous." The entire
  section consists of that one sentence — the shortest complete rule
  section read anywhere in this file, a prohibition justified by one
  unelaborated risk claim.
- **Right-hand assignment is not supported, with a searchability
  rationale** — "We do not support using right-hand assignment." / "This
  convention differs substantially from practices in other languages and
  makes it harder to see in code where an object is defined." /
  "E.g. searching for `foo <-` is easier than searching for `foo <-` and
  `-> foo` (possibly split over lines)." A rule justified by grep-ability
  — the first rule in this file whose stated reason is literally about
  text search over the codebase.
- **Explicit `return()` is required, against R's implicit-return
  feature** — "Do not rely on R's implicit return feature. It is better
  to be clear about your intent to `return()` an object." The same
  "restrict what the language permits" shape as the rest of this file —
  notable here because the guide's own upstream is widely associated with
  the opposite convention, though that upstream position has not been
  re-verified here and is not asserted.
- **External functions must be namespace-qualified, and the guide prices
  its own rule** — "Users should explicitly qualify namespaces for all
  external functions." / "We discourage using the `@import` Roxygen tag
  to bring in all functions into a NAMESPACE." Stated tradeoff, admitted
  in the rule's own text: "While there is a small performance penalty for
  using `::`, it makes it easier to understand dependencies in your
  code." — the same name-the-cost honesty as the Swift guide's
  reference-links rule above.

**Scope note**: this is Google's own convention for Google's own R code,
one company's patch against one community standard — not an R language
specification, not the Tidyverse Style Guide itself (which should be read
separately and is not summarized here), and not a claim about how the
wider R community writes R — much of which follows the unforked tidyverse
conventions, including `snake_case` function names, that this guide
explicitly departs from.

## Vim script: a guide whose threat model is the user's own configuration

Read directly from Google's public Vimscript Style Guide
(google.github.io/styleguide/vimscriptguide.xml) — canonical URL
confirmed via Google's style-guide index page; quotations were checked
across two passes, one against the rendered page and one against the raw
XML source
(`raw.githubusercontent.com/google/styleguide/gh-pages/vimscriptguide.xml`),
which returned matching text. This is Google's own convention for its own
Vim plugin code, one company's stated preferences, not a
Vim-community-wide standard.

- **The guide names its own register, and splits itself into a casual
  and a heavy half** — "This is a casual version of the vimscript style
  guide, because vimscript is a casual language." Immediately followed by
  the binding clause: "When submitting vim plugin code, you must adhere
  to these rules." — casual tone, mandatory force. A companion document
  carries the reasoning: "For clarifications, justifications, and
  explanations about the finer points of vimscript, please refer to the
  heavy guide." The Go section above records a multi-document split too
  (Decisions vs. Guide vs. Best Practices), but that split is by topic;
  this one is by *formality register* — the binding rules in the light
  document, the justifications exiled to the heavy one.
- **The organizing threat model is the user's own configuration — an
  adversary no other guide in this file defends against** — "It's hard
  to get vimscript right. Many commands depend upon the user's settings.
  By following these guidelines, you can hope to make your scripts
  portable." The concrete rules below are all instances of this one
  concern: a Vim plugin runs inside an environment the *end user* has
  already customized, so the guide's rules armor the script against its
  own host. Other guides in this file defend against future maintainers,
  reviewers, or scale; this one defends against the person the code is
  running for.
- **`normal!` is required over `normal`, because the unbanged form
  executes through the user's key mappings** — "Always use normal!
  instead of normal. The latter depends upon the user's key mappings and
  could do anything." The stated failure mode — "could do anything" — is
  the user's-configuration threat model at its starkest.
- **All regexes are force-prefixed to neutralize the user's matching
  settings** — "Prefix all regexes with \m\C" so that they "act like
  nomagic and noignorecase are set" regardless of the user's actual
  settings. The same armor-the-script move as `normal!`, applied to
  pattern matching.
- **Single-quoted strings are preferred for a semantic reason, not a
  stylistic one** — "Prefer single quoted strings": "Double quoted
  strings are semantically different in vimscript, and you probably
  don't want them (they break regexes)."
- **`:substitute` is avoided in scripts because of its side effects** —
  "Avoid using :s[ubstitute] as it moves the cursor and prints error
  messages." — with functions such as `search()` preferred as
  script-suited alternatives. A command perfectly acceptable
  interactively is rejected in scripts because its interactive
  conveniences (cursor movement, messages) become side effects.
- **Scope prefixes are split into a mandatory tier and a
  consistency tier** — "g:, s:, and a: must always be used," while
  "l: and v: should be used for consistency, future proofing, and to
  avoid subtle bugs." A two-tier rule that separates what is required
  from what is merely wise, in its own text.
- **The guide documents the language's own unsafe comparisons as the
  reason for its type rules** — "Vimscript has unsafe, unintuitive
  behavior when dealing with some types. For instance, 0 == 'foo'
  evaluates to true." The language's permissiveness is quoted as the
  hazard, the same restrict-what-the-language-allows shape as the rest
  of this file.
- **Errors are matched by code, not by message text — for a
  localization reason** — "Match error codes, not error text. Error text
  may be locale dependent." The only rule read anywhere in this file so
  far whose stated rationale is internationalization — checked against
  the other fourteen sections before writing "only" (the standing lesson
  from the C# review applied: search for the counterexample first).

**Scope note**: this is Google's own convention for Google's own Vim
plugin code, not a Vim or Vimscript specification and not a claim about
how the wider Vim community writes plugins — and the guide's companion
"heavy guide" has not been read for this file; none of its content is
assumed.

## Cross-language pattern (relative to this catalog's other findings)

The same "restrict what the language allows, for a stated scale-driven or
correctness reason" pattern recurs independently outside Google's guides too
— see `catalog/governance-patterns.md`'s **module-boundary discipline**
convergence (Kong, prettier, hugo, npm/cli, Chart.js, apollo-server), which is
the *project-governance* form of the same instinct these *language* style
guides apply at the syntax level.

**Where an external standard dominates, Google builds on it rather than
against it — and the vendor hypothesis had to be revised.** Four of the
guides read here explicitly build on an outside organization's published
document, by name, at four distinct strengths: Google's Objective-C
guide asks the reader to *consult* Apple's document ("Please read it in
addition to this guide", plus a Naming section that says "Follow
standard Objective-C naming rules" with a link to the same Apple
document); the C# guide *obeys* Microsoft's ("Naming rules follow
Microsoft's C# naming guidelines"); the Swift guide *absorbs* Apple's —
its naming guidelines "are considered part of this style guide and are
followed as if they were repeated here in their entirety"; and the R
guide is *forked from* the Tidyverse Style Guide outright, existing
mainly as a record of departures from it. The first three cases
suggested a common cause of "dominant platform vendor with a published
naming standard" — and an earlier revision of this paragraph said
exactly that. The R case falsifies the vendor half of that hypothesis:
the Tidyverse Style Guide is a community standard, not a platform
owner's. What survives all four cases is the weaker, better statement:
where a language already has one dominant published style authority —
vendor or community — Google does not compete with it, and writes its
own rules only in the space that remains. In the three vendor cases the
deference anchors to naming specifically; the R fork is global, so the
naming-concentration observation holds at n=3, not n=4. Recorded as an
observed pattern, not a claim about guides not read here — the Python,
C++, Java, Go, TypeScript, Shell, JavaScript, JSON, HTML/CSS and
Markdown sections above state their conventions without citing an
external owner.

**Two negative results are recorded in the Swift section above**, and
they matter to how the rest of this file should be read: patterns first
observed in a single guide (the C# guide's habit of flagging its own
rules as provisional, and its examples silently revealing a platform its
prose never names) were tested against a second guide and did *not*
recur. Single-guide observations in this file should therefore be read as
characteristics of that guide until a second instance is actually found —
which is why each such observation names the guide it came from rather
than being generalized to "Google's guides."

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
same pattern.

Google's Shell Style Guide (google.github.io/styleguide/shellguide.html) has
since been read: five rules — the 100-line-or-non-straightforward-control-flow
rewrite trigger, the SUID/SGID prohibition, the `[[ ... ]]`-over-`[ ... ]`/
`test`/`/usr/bin/[` preference, the `$(command)`-over-backticks rule, and the
variable-quoting/brace-form guidance (see the Shell section above) — were
confirmed first-hand across two separate verbatim passes over that page and
are quoted directly; note that the guide's own text characterizes the last of
those five — variable quoting — as a strong recommendation rather than a hard
mandate, a materially weaker force than the forbidden-outright SUID/SGID rule
beside it, though that specific characterization is this document's
paraphrase rather than a confirmed verbatim sentence. Five further rules — the
mandatory-`local`-in-functions convention, the avoid-piping-into-`while`
convention, the double-parenthesis-only arithmetic convention, the
functions-grouped-below-constants convention, and the mandatory-`main`-
function convention (see the Shell section above) — come from a single
earlier summary pass over the same page and are recorded above as paraphrase,
not verbatim quotation; the rest of that guide has not yet been read and is
not assumed to follow the same pattern.

Google's JavaScript Style Guide (google.github.io/styleguide/jsguide.html)
has since been read: seven rules — the variadic-`Array`-constructor ban, the
`with`-keyword ban, the `eval`/`Function(...string)` ban, the
default-exports ban, the identity-operator requirement, the ES-module-cycle
ban, and the `var`-ban/`const`-default rule (see the JavaScript section
above) — were confirmed first-hand across two separate verbatim passes over
that page (both passes returned character-identical text) and are quoted
directly; three further rules — the no-modifying-built-ins rule, the
no-`new`-on-primitive-wrappers rule, and the braces-mandatory-with-a-narrow-
exception rule (see the JavaScript section above) — come from a single pass
and are recorded above as paraphrase, not verbatim quotation; the rest of
that guide (JSDoc conventions beyond the two rules noted, naming rules
beyond constants, and more) has not yet been read and is not assumed to
follow the same pattern. Note also that Google's own JavaScript guide page
now recommends TypeScript for new code — it was read here for its own
pattern set, not as a claim that Google currently prefers it.

Google's JSON Style Guide (google.github.io/styleguide/jsoncstyleguide.xml)
has since been read: five rules — the camelCase-property-name rule, the
`kind`-first/`items`-last ordering rules, the `data`-xor-`error` envelope
rule, the `deleted`-marker-must-be-`true` rule, and the no-comments rule
(see the JSON section above) — were confirmed first-hand across two separate
verbatim passes over that page (both passes returned character-identical
text) and are quoted directly; the remaining rules — enum-values-as-strings,
drop-empty-or-null-properties, plural-for-arrays/singular-otherwise, and the
RFC 3339 / ISO 8601 date and duration formats (see the JSON section above) —
come from a single pass and are recorded above as paraphrase, not verbatim
quotation; the full list of reserved top-level and `data`-object property
names (`apiVersion`, `context`, `id`, `method`, `params`, `etag`, `lang`,
paging properties, link properties, and the `error` object's sub-properties)
has not been individually re-verified beyond that single pass and is not
repeated in the section above. Note also that this guide governs a data
format, not a programming language, and is scoped accordingly (see the
Scope note in the JSON section above).

Google's HTML/CSS Style Guide (google.github.io/styleguide/htmlcssguide.html)
has since been read: eleven rules — the HTML-double/CSS-single quotation-mark
split with its `@charset` exception, the `id`-attribute avoidance rule and its
`window`-prototype rationale, the class-naming rule, the class-name hyphen
delimiter rule, the ID-selector avoidance rule, the `type`-attribute omission
rule, the lowercase-only capitalization rule, the trailing-whitespace rule,
the shorthand-properties rule, the zero-value-units rule, and the
three-character hex-notation rule (see the HTML/CSS section above) — were
each confirmed by at least two independent sources: either two blind
full read-throughs that matched character-for-character on first pass, or
one read-through plus a short targeted re-fetch used to resolve a wording
gap or single-pass-only finding (the same short-fragment technique
introduced in the JSON section above, used here because several sentences
ran past this page-summarizer's per-quote character limit); all are quoted
directly. The 2-space-indentation rule is recorded as confirmed but with
no rationale found in the passage read. The "Parting Words" closing section was read and quoted, but its
resemblance to PEP 8's "foolish consistency" passage is noted as an
unverified similarity in spirit, not a confirmed textual match — that
specific cross-check has not been performed. Several sections of the guide
have not been read at all and are not assumed to follow the same pattern:
Comments, Action Items, Document Type, HTML Validity, Semantics, Multimedia
Fallback, Separation of Concerns, Entity References, Optional Tags, HTML
Line-Wrapping, CSS Validity, Class Name Style, Prefixes, Type Selectors,
Important Declarations, Hacks, Declaration Order, Block Content Indentation,
Declaration Stops, Property Name Stops, Declaration Block Separation,
Selector and Declaration Separation, Rule Separation, and Section Comments.

Google's Markdown Style Guide (google.github.io/styleguide/docguide/style.html)
has since been read: fifteen rules — the document-layout skeleton and its
"See also" closing section, the 80-character line limit and its stated
exceptions, the trailing-whitespace ban and both of its distinct reasons
(the CommonMark `<br />`-insertion risk and the presubmit/IDE tooling
reason), the ATX-vs-Setext heading rule, the unique-heading-names rule and
its anchor-link rationale, the single-H1 rule, both branches of the
ordered-list numbering rule (lazy vs. fully numbered) with their separate
rationales, the nested-list 4-space-indent rule, the inline-code-backticks
rule, the fenced-vs-indented code block rule with all three of its stated
reasons, the declare-the-language rule, the informative-link-titles rule
and its rewriting instruction, the reference-links rule with its stated
readability tradeoff and placement sub-rule, the tables-vs-lists rule, and
the closing prefer-Markdown-over-HTML rule (see the Markdown section
above) — were each confirmed by at least two independent sources: two
blind full read-throughs that matched or reconciled into one sentence
between them, or one read-through plus a short targeted re-fetch; all are
quoted directly. Two rationales (the anchor-link reason for unique heading
names, and the short-list numbering reason) each required a third
confirming pass specifically because the two initial passes had each
quoted a different half of the same sentence — see the cross-check notes
in the Markdown section above. Two additional
single-pass findings from the initial extraction — a rule about using
explicit root-relative paths for internal Markdown links, and a rule
about avoiding relative paths (`../`) across directories — were not
independently re-confirmed and are not included above; they are recorded
here only as leads for a future pass. Several sections of the guide have
not been read at all and are not assumed to follow the same pattern:
Minimum viable documentation, Better is better than best, Capitalization
(both the top-level section and the titles/headers sub-rule), the
add-spacing-to-headings sub-rule, escape-newlines-in-code-blocks, nesting
code blocks within lists, and the Images section.

Google's C# Style Guide (google.github.io/styleguide/csharp-style.html)
has since been read: fifteen rules — the Microsoft-deferred naming
convention, the interface-`I`-prefix and acronym-casing rules, the
file-naming rules, the fixed modifier order, the `using`-declaration
ordering rule, the two-axis class-member-ordering rule, the
Java-inherited whitespace/brace rules, the `const`/`readonly`/magic-number
rule, the expression-bodied-properties rule and its self-dated C#-7
review note, the structs-vs-classes rule with its Unity-adjacent example
list, the struct-defaults rule and its deferred `StatusOr` commitment,
the extension-methods rule, the `ref`/`out` rules (including the
British-spelling observation), the LINQ preferences, and the `var`
readability test (see the C# section above) — were each confirmed by at
least two independent sources: two blind full read-throughs that matched
on shared sentences, one read-through plus a short targeted re-fetch, or
in a few cases a single pass plus one dedicated targeted re-fetch aimed
at that exact sentence; all are quoted directly. Four further,
narrower-scope rules — calling delegates via `Invoke()` with the
null-conditional operator, Object Initializer syntax being reserved for
plain-data types, the string-concatenation performance caveat, and the
named-class-over-`Tuple<>` return-type preference (see the C# section
above) — were each confirmed by at least one full pass plus one targeted
re-fetch and are compressed into a single paragraph rather than given
full entries, for length rather than confidence reasons. The claim that
this guide contains Unity-game-engine-specific content was checked before
being incorporated at all, not assumed: a full-page search found "Unity"
nowhere as a standalone capitalized word and "game" nowhere at all, with
the string "unity" occurring exactly once, lowercased inside the example
project name `unity_app`. That occurrence and the
Vector3/Quaternion/Bounds example list are the only Unity-adjacent traces
in the document, and are presented in the C# section above as exactly
that — traces, not a claim that this is a Unity-branded guide. One
observation in that section rests on knowledge from outside this page and
is flagged as such in the text: that C# 7 has since shipped, which is
what makes the guide's future-tense "when C# 7 is live" sentence readable
as a fossil; the page itself carries no dates. Several sections of the
guide have not been read at all and are not assumed to follow the same
pattern: `IEnumerable` vs `IList` vs `IReadOnlyList`, Generators vs
containers, Field initializers, Array vs List, Folders and file
locations, Namespace naming (beyond the `unity_app` example noted above),
Removing from containers while iterating, and Attributes.

Google's Swift Style Guide (google.github.io/swift/) has since been read,
and is the first guide in this file whose quotations were verified against
literal raw Markdown source
(`raw.githubusercontent.com/google/swift/gh-pages/index.md`) rather than a
rendered page mediated by a summarizing fetch layer. Fourteen rules — the
incorporation-by-reference of Apple's naming guidelines, the semicolon
ban, the 100-column limit, the trailing-comma requirement and its
diff-hygiene reason, the force-unwrap/force-cast rule, the
implicitly-unwrapped-optionals rule, the sentinel-values rule, the
error-types rule, the `guard` early-exit rule, the
naming-is-not-access-control rule, the import rules, the `///`
documentation-comment rule, the one-statement-per-line rule, and the
line-wrapping cardinal rules (see the Swift section above) — are quoted
directly, with the load-bearing quotations among them checked against
that raw source. Where the raw source carries Markdown emphasis markup,
the rendered wording is quoted and the emphasis described rather than
reproduced. One phrase is deliberately *not* quoted at glyph level: the
two independent passes disagreed on whether the quotation marks around
"pyramid of doom" in the `guard` section are straight or curly, so it is
described instead. Two hypotheses carried over from the C# section were
tested and both returned negative; the negatives are recorded in full in
the Swift section above rather than omitted. Several sections of the
guide have not been read closely and are not assumed to follow the same
pattern: Special Escape Sequences, Invisible Characters and Modifiers,
String Literals, File Comments, Overloaded Declarations, Horizontal
Alignment, Vertical Whitespace, Parentheses, Switch Statements, Enum
Cases, Numeric Literals, Attributes, Initializers, Types with Shorthand
Names, Nesting and Namespacing, `for-where` Loops, `fallthrough`, Pattern
Matching, Tuple Patterns, Playground Literals, Trapping vs. Overflowing
Arithmetic, Defining New Operators, and Overloading Existing Operators.

Google's Objective-C Style Guide (google.github.io/styleguide/objcguide.html)
has since been read, with every load-bearing quotation verified against
the raw Markdown source
(`raw.githubusercontent.com/google/styleguide/gh-pages/objcguide.md`)
across two independent passes plus targeted re-checks — the same raw-source
method introduced for Swift above. Ten rules and principles — the four
named Principles (including the "pull their weight" meta-rule and its
`goto` absence-explanation), the Cocoa Coding Guidelines deference and the
Naming section's "Follow standard Objective-C naming rules" link, the
two/three-letter prefix rule with Apple's reservation warning, the
100-column limit, the asymmetric exceptions rule, the `BOOL` pitfalls rule
with its named platforms, the message-to-`nil` semantics statement, the
spaces/2-space indentation rule, and the small-functions preference (see
the Objective-C section above) — are quoted directly. The "Inclusive
Language" principle subsection was noted but not read closely. Most of the
guide's long tail has not been read and is not assumed to follow the same
pattern — among the unread sections: File Names, Category Names, Function
Names, Variable Names, Instance Variables, Constants, Method Declarations,
Unsigned Integers, Types with Inconsistent Sizes, Floating Point
Constants, all three Comments subsections, Object Ownership, Manual and
Automatic Reference Counting, Macros, Nonstandard Extensions, Designated
Initializers, `#import`/`#include` and Order of Includes, Umbrella
Headers, Mutables and Copies, Lightweight Generics, Nullability,
Containers Without Instance Variables, Delegate Pattern, Objective-C++,
and most of Spacing and Formatting.

Google's R Style Guide (google.github.io/styleguide/Rguide.html) has
since been read, verified against the raw Markdown source
(`raw.githubusercontent.com/google/styleguide/gh-pages/Rguide.md`) across
two passes. The guide is short enough that the two passes between them
covered essentially every rule sentence it contains — the fork
declaration and its CC BY-SA license credit, the `BigCamelCase` and
private-dot-prefix naming rules, the recorded reversal of the former
`dot.case` recommendation, the one-sentence `attach()` rejection, the
right-hand-assignment rule with its searchability rationale, the
explicit-`return()` rule, and the namespace-qualification rule with its
admitted `::` performance cost (see the R section above); all are quoted
directly. One deliberate omission: the claim that the explicit-`return()`
rule contradicts the forked upstream's own convention is widely assumed
but was *not* re-verified against the Tidyverse Style Guide's text here,
and the R section states it only as an unasserted association. The
Tidyverse Style Guide itself — the upstream of this fork — has not been
read for this file and none of its content is assumed. The R case also
forced a revision of the Cross-language pattern section's causal
hypothesis (from "platform vendor" to "dominant published style
authority"), and the superseded wording is acknowledged there rather
than silently replaced. The "by far the shortest" claim in the R section
was later re-verified by measurement rather than impression: the source
file is 2,982 bytes against, for example, 14,234 bytes for the
Vimscript guide's source (GitHub API `size` fields, checked when the
Vimscript section was added).

Google's Vimscript Style Guide
(google.github.io/styleguide/vimscriptguide.xml) has since been read,
with quotations checked across two passes — one against the rendered
page, one against the raw XML source — which returned matching text.
Nine rules and framing statements — the casual/heavy split and its
binding clause, the portability framing, the `normal!` rule, the `\m\C`
regex prefix rule, the single-quoted-strings rule, the `:substitute`
avoidance rule, the two-tier scope-prefix rule, the unsafe-comparisons
statement, and the match-error-codes-not-text rule (see the Vim script
section above) — are quoted directly. The companion "heavy guide"
(vimscriptfull) has not been read and none of its content is assumed;
the guide's General Guidelines and Style sections were read only in
part, and messaging/mapping/settings rules in them are not covered
above. The "only i18n rationale in this file" claim was checked by
searching the other fourteen sections for locale/localization
counterexamples before being written (one false positive — Go's
"goroutines localized" — was inspected and excluded).

With Vim script now read, Google's public style-guide catalog
(google.github.io/styleguide/) still lists two further guides that
remain unread first-hand — AngularJS and Common Lisp — neither of which
should be assumed to follow this pattern.
