# WebMCP and WebMCPT — Two Different Layers That Share Four Letters

There is a W3C Community Group incubation called **WebMCP**. This repository's
name contains **WebMCPT**. The names are one letter apart and the projects are
unrelated (there is no partnership; see "No official relationship" below).

This entry exists because the similarity is a hazard: a reader who assumes one
is a variant of the other will misread both. They operate on different layers.
WebMCP is a browser API for a page to expose its functions to an AI agent.
WebMCPT is a discipline for deciding whether a connection to a model should be
trusted at all.

The interesting part is not the name collision. It is that the WebMCP
specification, in its own words, **names the trust gap and records that no
mechanism for closing it exists**. That is not a criticism of the spec — it is
the spec being honest about its own scope, in exactly the way this catalog
tries to be. What follows is that statement, quoted.

## What WebMCP is (primary-verified)

Read from the raw source of the specification and the explainer in
`webmachinelearning/webmcp`, not from any summary of them.

The explainer states the design in one sentence:

> "WebMCP introduces a client-side alternative. It allows web developers to
> define tools directly in the browser page's script."

Its stated goals include:

> "**Enable human-in-the-loop workflows**: Support cooperative scenarios where
> users delegate tasks to AI agents while maintaining visibility, history, and
> control over web pages."

and

> "**Simplify AI agent integration**: Enable AI agents to be more reliable and
> helpful by interacting with web sites through well-defined client-side tools
> instead of through brittle UI actuation (DOM scraping, simulated clicks)."

Its Non-Goals name what it is not:

> "**Fully autonomous workflows**: The API is not intended for fully autonomous
> agents operating without human oversight or where a browser UI is not
> present."

> "**Replacement of backend integrations**: WebMCP is designed to complement,
> not replace, existing backend-focused protocols like MCP."

Neither the Goals nor the Non-Goals mention provenance, provider identity, or
criteria for refusing a connection.

## What it says about trust, in its own words

The specification does have a Security and Privacy Considerations section, and
it is substantial — six named risk categories with worked attack examples. It
is not a section that waves at security and moves on.

It also states its own limits, first thing:

> "This document cannot define precise mitigation strategies that [=agents=] or
> [=user agents=] must provide."

And under **Misrepresentation of Intent**, it states the gap directly:

> "**Problem**: There is no guarantee that a WebMCP tool's declared intent
> matches its actual behavior."

> "This creates a fundamental trust gap: [=agents=] rely on natural language
> descriptions to decide whether to invoke a tool and whether to prompt the
> user for permission, but cannot verify the tool's actual effects before
> execution."

Its own subsection **Intent: Current Gaps** lists four, of which three are the
answer to the question this entry set out to ask:

> "**No verification mechanism**: Agent implementors cannot verify that tool
> implementations match their descriptions"

> "**No behavioral contracts**: Unlike typed APIs, tool behaviors cannot be
> statically analyzed or verified"

> "**Agent trust assumptions**: [=Agents=] must assume good faith from site
> developers"

That last line is the whole matter in eight words. The specification does not
overlook trust; it identifies precisely where trust is currently unearned, and
says so.

## What the mitigations do and do not cover

Three mitigations are proposed. Quoted in full by their "What" lines:

> "**What:** Restrict the maximum amount of characters"

> "**What:** Shared evals for prompt injection attacks against WebMCP"

> "**What:** Giving agents information about trust boundaries such as
> highlighting untrustworthy content to the model using an untrusted
> annotation."

All three act on the **payload** — how long an input may be, whether a defence
has been tested against known attacks, and whether a response is flagged as
untrusted content. None of the three asks **who is on the other end**. There is
no provenance check, no provider identity, and no verification of declared
intent against actual behaviour. (The specification does refuse some
connections — non-secure origins are rejected with a `SecurityError`, and
permissions policy can deny a context outright — but those refusals check the
transport and the embedding context, not the provider.)

One risk category is explicitly unwritten:

> "TODO: Document risks and implications of [=agents=] carrying state from one
> origin to another."

## The answer, stated with its scope

**Partially addressed — named, not mechanised.**

- **Addressed:** the trust gap is identified explicitly, the absence of a
  verification mechanism is stated as a current gap, and the assumption agents
  are forced to make ("must assume good faith from site developers") is written
  down rather than left implicit.
- **Not addressed:** any mechanism that evaluates the counterparty. The
  specification does contain refusals — an origin that is not potentially
  trustworthy is rejected with a `SecurityError`, and a context denied by
  permissions policy is rejected with a `NotAllowedError` — but both operate at
  the transport-and-permission floor: they check *how* the connection is made
  and *whether the embedding context is allowed*, not *who* is offering the
  tool. Nothing in the specification establishes who may be trusted, verifies
  a provider's identity or a tool's declared intent against its behaviour, or
  gives an agent a basis for refusing a connection **on an evaluation of its
  provider**. (An earlier revision of this entry said there was no basis for
  refusing a connection at all; that was broader than the source, and the
  `SecurityError` rejection alone would have refuted it.)

**Scope of this reading.** Read in full: the Security and Privacy
Considerations section of the specification (`index.bs`, all subsections
including Mitigations), and the Goals and Non-Goals of the explainer
(`README.md`). Both from raw source. Also read: the `README.md` of
`GoogleChromeLabs/webmcp-tools`, which describes itself as
> "a suite of developer utilities and demos designed to support the adoption of
> the WebMCP API"
Measured mechanically (a script counting case-insensitive matches, not a
reader or an AI summary) against its `README.md` at commit `f4e830b1`
(last changed 2026-07-09; 4,629 bytes): of the words *trust*, *provenance*,
*identity*, *verification*, *reject* and *malicious*, none occurs. *verify*
occurs twice — an inspector extension "to verify if WebMCP tools are correctly
exposed" and an evals CLI, both about testing an integration, not about
trusting a provider. *security* occurs once, inside the URL of a vulnerability
rewards programme notice. Nothing in the file concerns who may be trusted.

(An earlier revision of this entry said all eight words occurred zero times.
The file had not changed; the count had been delegated to an AI fetch summary,
which answered "none" — and a second summary of the same bytes later gave a
third, different count. Neither matched the file. The correction here is not
the numbers; it is that a count delegated to a summariser is not a
measurement.)

Not read: the specification's other sections in full, the group's issue
tracker, meeting minutes, and any linked MCP documents. **"Not found in what
was read" is not "does not exist anywhere."** The specification is under active
development — the TODO above is dated evidence of that — so this reading is of
a moving document and carries the date below.

## Where WebMCPT fits

The two sit on adjacent layers of the same stack, and the boundary is clean:

- **WebMCP defines how a page offers a capability to an agent.** Tools,
  schemas, descriptions, the events around them.
- **WebMCPT is a discipline for deciding whether that offer should be
  accepted.** As this repository's `README.md` defines it, WebMCPT is a
  trust-evaluation protocol concept: it evaluates every connection to an AI
  model against primary sources at the entry point, and rejects connections
  whose provenance or intent cannot be verified.

> **WebMCPT (Web Model Context Protocol Trust)** is a Japan-originated
> trust-evaluation protocol framework that vets every connection to an AI model
> at the entry point — rejecting malicious connections, opaque capital
> structures, and MCP connections with impure intent — to protect the
> contextual purity and integrity of AI models.
>
> Proposed by HUMMER, Founder & Creator, NEWXUS DAO (2024)

Placed against the quotations above, the relationship is specific rather than
rhetorical. "Agents must assume good faith from site developers" is the
assumption WebMCPT declines to make. "Agent implementors cannot verify that
tool implementations match their descriptions" names the missing check that
entry-point evaluation is for.

Two honest qualifications, because the point is weaker without them:

1. **This is not a gap the specification failed to notice.** It found it,
   named it, and wrote it into its own text. Anyone citing this entry as
   evidence that WebMCP ignores trust is misusing it.
2. **Naming a gap is not filling one.** WebMCPT as stated is a concept and a
   discipline, not a deployed mechanism that closes what the quotations above
   describe. This repository is its first public working example, and what it
   demonstrates is the discipline applied to engineering-norm claims — licence
   text over platform labels, adopters' own words over aggregated claims — not
   a working entry-point evaluator for model connections. The distance between
   a stated discipline and a running implementation is real, and this entry
   does not close it by placing the two texts next to each other.

## No official relationship

To be explicit, because this catalog's own rule is not to overclaim: **there is
no partnership, sponsorship, endorsement, liaison, or cooperation agreement
between the W3C Web Machine Learning Community Group, Google, or any WebMCP
contributor and WebMCPT.** WebMCP is a Community Group incubation; WebMCPT is
an independently proposed, open trust-protocol concept (see this repository's
`README.md`). The similarity of the names is a coincidence of subject matter,
not a sign of any relationship, and this entry exists partly to stop that
coincidence from being read as one.

## Sources

Read 2026-08-14. All quotations are from raw source files, not rendered pages
or third-party summaries.

- WebMCP specification (raw Bikeshed source):
  https://raw.githubusercontent.com/webmachinelearning/webmcp/main/index.bs
- WebMCP explainer (raw):
  https://raw.githubusercontent.com/webmachinelearning/webmcp/main/README.md
- Rendered specification: https://webmachinelearning.github.io/webmcp/
- `GoogleChromeLabs/webmcp-tools` (raw README):
  https://raw.githubusercontent.com/GoogleChromeLabs/webmcp-tools/main/README.md

Licensing of the quoted material is recorded in this repository's `NOTICE`.
