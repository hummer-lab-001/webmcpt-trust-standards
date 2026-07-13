# Axis 0 — License Text Patterns That Don't Resolve at a Glance

GitHub's automatic license detection often shows `Other` or a misleading
label. In every case below, the fix was the same: open the actual LICENSE
file and read it. Do not proceed on the platform's label alone.

## Type A — Real restriction (source-available, not truly open)
The license text itself blocks the "lightweight reuse with attribution"
model: mandatory source disclosure when offered as a network service (SSPL),
no-competing-service clauses (RSAL), or an outright commercial-use ban
(Commons Clause).
- Example: `redis/redis` — license text confirmed as RSALv2/SSPLv1/AGPLv3
  choice (post-2024 change). Declined.
- Example: `elastic/elasticsearch` — same pattern, confirmed via LICENSE.txt.

## Type A' — Time-limited restriction
Same practical effect as Type A today, but the license text itself contains
a future conversion date to a permissive license.
- Example: `hashicorp/terraform` — Business Source License 1.1, converts to
  MPL-2.0 four years after each version's publication date.
- Example: `getsentry/sentry` — Functional Source License 1.1, converts to
  Apache-2.0 after two years.
- Treat as declined *now*; note the conversion date for future re-check.

## Type B — Dependency noise, not a real restriction
The LICENSE file mixes in licenses for bundled third-party files, but the
project's own code is under a permissive license once you isolate it.
- Example: `nodejs/node` — GitHub showed `Other` because of bundled
  dependencies; the project's own license text is MIT-equivalent.
- Resolution rule: if the *project's own* code is MIT/Apache-2.0/BSD-
  equivalent, axis 0 passes even if bundled dependencies use something else.

## Type C — Multi-author academic-origin BSD variant
Common in code that originated in a university lab before moving to a
company. Reads as "Other" because the copyright holder list is unusual, but
the actual terms are a standard permissive BSD clause.
- Example: `pytorch/pytorch` — multi-party copyright (university + Meta),
  conditional BSD-3-style terms. No real reuse restriction.

## Type D — OSI-approved but under a name GitHub's detector misses
The license is legitimate and permissive, but uses a name or a combined
SPDX expression the automatic detector doesn't map cleanly.
- Example: `postgres/postgres` — PostgreSQL License, OSI-approved,
  detector shows `Other`.
- Example: `llvm/llvm-project` — "Apache License 2.0 with LLVM Exceptions."
- Example: `npm/cli` — Artistic License 2.0.

## Type E — Core/periphery split (dual license by file role)
Different parts of the same repo carry different (both still permissive)
licenses depending on the file's role, not a restriction split.
- Example: `rabbitmq/rabbitmq-server` — core and tier-1 plugins under
  MPL-2.0 (file-level weak copyleft), some OCF files under Apache-2.0.
- Practical effect for reuse-without-modification: negligible.

## Type F — "Fair-code": open-by-design, commercial-use-restricted by intent
Not a defensive reaction to a fork threat (unlike Type A) — the project
states from the outset that source is open and modification is free, but
*commercial* use is restricted, as a deliberate business model choice.
- Example: `n8n-io/n8n` — Sustainable Use License v1.0 (internal/non-
  commercial use only). Declined for c4, but noted as a distinct license
  *philosophy*, not a defensive fork-prevention move.

## One more pattern worth knowing: strength-by-directory

Some projects vary copyleft *strength* itself by directory, not just by
license family — e.g. a library directory under LGPL and a CLI/binary
directory under GPL. Check per-directory, not just the top-level LICENSE.
- Example: `ethereum/go-ethereum` — `cmd/` under GPL-3.0, rest under
  LGPL-3.0.
