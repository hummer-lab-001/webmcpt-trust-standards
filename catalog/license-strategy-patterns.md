# OSS License Strategy Patterns — A Field Taxonomy

All patterns below were confirmed by reading the LICENSE file text itself
(never GitHub's auto-detected label alone). Each pattern names at least one
worked example from the catalog.

## The seven types

| Type | Nature | Motive class | Examples (primary-verified) |
|---|---|---|---|
| A | Real restriction (SSPL / RSAL / Commons Clause) | Defensive relicense | redis, elasticsearch (both later re-added an AGPL-3.0 option — see lineage below); historically neo4j enterprise (AGPL + Commons Clause, code withdrawn from GitHub since 3.5 — the current public repo is GPL-3.0) |
| A′ | Time-limited restriction (BSL / FSL with auto-conversion date) | Defensive, time-boxed | terraform (BSL→MPL-2.0 in 4y), sentry (FSL→Apache-2.0 in 2y), consul, nomad |
| B | Dependency noise — project's own code is permissive | — (labeling artifact) | nodejs/node |
| C | Multi-author academic-origin BSD variant | — (labeling artifact) | pytorch |
| D | OSI-approved but under a name detectors miss | — (labeling artifact) | postgres, llvm (Apache-2.0 WITH LLVM-exception), npm/cli (Artistic 2.0), ImageMagick |
| E | Core/periphery split — different permissive licenses by file role | Engineering choice | rabbitmq (MPL-2.0 core + Apache-2.0 OCF) |
| F | "Fair-code" — commercial use restricted by design, from day one | Business-model philosophy | n8n (Sustainable Use License) |

Three distinct **motive classes** emerge: defensive (A), time-boxed defensive (A′),
and philosophical/by-design (F). They look similar in effect but differ in origin
and in how they should be re-evaluated over time (A′ entries carry a re-check date).

## The copyleft strength spectrum (5 levels + 2 refinements)

Observed in the wild, weakest to strongest:

1. **MPL-2.0** — file-level weak copyleft (rabbitmq, sops)
2. **LGPL-3.0** — library-boundary copyleft (sonarqube, odoo)
3. **GPL-2.0** — strong copyleft, distribution-triggered (git, linux)
4. **GPL-3.0** — strong copyleft + patent/anti-tivoization terms (ansible, typesense)
5. **AGPL-3.0** — network-service-triggered disclosure (grafana, loki, minio, unleash)

Refinements that require per-directory reading:

- **Strength-by-directory**: `ethereum/go-ethereum` — `cmd/` is GPL-3.0, the
  library remainder is LGPL-3.0. The copyleft *strength itself* varies inside
  one repository.
- **Explicit boundary engineering**: `torvalds/linux` — GPL-2.0 WITH
  Linux-syscall-note, an SPDX-formalized exception that explicitly stops
  propagation to userspace programs. Copyleft with an engineered perimeter.
- **Version-pinning as philosophy**: both `git` and `linux` are deliberately
  "GPLv2 only" — the license version choice itself is a governance statement.

## The relicense-and-fork lineage (2018–2024)

A complete cause-and-effect chain, each step primary-verified:

1. **2018** — MongoDB creates SSPL (the prototype defensive relicense).
2. **2021** — Elastic follows (Elasticsearch → SSPL/Elastic License).
   → **AWS forks OpenSearch** (Apache-2.0, now a foundation project).
3. **2024** — Redis follows (RSAL/SSPL choice).
   → **Linux Foundation forks Valkey** (BSD, with major-vendor backing).
4. **The partial reversals** — Elastic re-added an AGPL-3.0 option in 2024,
   and Redis added AGPL-3.0 as a choice with Redis 8 (2025). Copyleft-strength
   restrictions remain, so the Axis 0 conclusion (declined for lightweight
   reuse) is unchanged — but the lineage did not end at step 3.

Notable asymmetry: MongoDB — the originator — never faced a comparable
full-strength fork; competitors answered with API-compatible alternatives
instead. *Under what conditions a relicense provokes a fork* is an open
question this catalog keeps collecting evidence for.

A related post-acquisition observation: after IBM's acquisition of HashiCorp,
the BSL licensor line in terraform/consul/nomad reads "International Business
Machines Corporation" — the restrictive strategy survived the acquisition as
a unified corporate policy (verified in all three repositories).

## Two operational rules this taxonomy enforces

1. **Never score a license from the platform label.** GitHub's `Other` label
   alone spans at least Types B, C, D and E — opposite conclusions.
2. **A symlink can masquerade as a license.** postfix's root LICENSE is a
   15-byte symbolic link; raw fetch returns the link target path, not the
   license. If a raw fetch comes back suspiciously tiny, suspect a symlink
   and follow it.
