# OSS Governance Patterns — Seven Lineages and Three Convergent Safeguards

Extracted from primary governance documents (GOVERNANCE.md, CONTRIBUTING.md,
foundation charters) across the catalog. No secondary summaries.

## Seven governance lineages

| Lineage | Mechanism | Examples |
|---|---|---|
| CNCF-graduated | Foundation maturity gates + neutral ownership | kubernetes, etcd, prometheus, envoy, fluentd, argo (family), harbor, containerd, cert-manager |
| ASF (Apache) | PMC + formal improvement proposals (KIP/AIP/…) + foundation-wide commit rules | kafka, airflow, spark, flink, arrow, skywalking, zookeeper, james |
| GitHub-native | Maintainer team + CONTRIBUTING.md as the constitution | react, typescript (with corporate backing), most mid-size projects |
| Elected board | Periodic community elections | jenkins (5-seat Governance Board), wasmtime (Bytecode Alliance annual elections) |
| Corporate-single | One company owns direction; community contributes | flutter (Google), electron (OpenJS-hosted but GitHub-led) |
| Vendor consortium | Competing silicon/platform vendors co-govern | zephyr (silicon vendors), graphql-js (multi-org review requirement) |
| Foundation-mandated documentation | The umbrella foundation *requires* governance docs to exist | pandas / numpy (NumFOCUS) |

An eighth, transitional pattern — **founder-exit fork** — was verified once:
Netflix archived Conductor (announcement of 2023-12-13, primary), and the
project continued under Orkes, a company founded by the original Netflix
developers, with the LICENSE copyright line transferred to "Orkes, Inc."

## Organizational lifecycle patterns

- **Company → foundation donation**: sops (Mozilla → CNCF), drools (Red Hat →
  Apache KIE; the move also *cleaned* an 8-license notice into plain Apache-2.0).
- **Full 4-stage CNCF transfer**: cert-manager (the most completely documented
  corporate→foundation handover in the catalog).
- **Layoff → foundation rescue → revival**: servo (Mozilla layoffs → Linux
  Foundation Europe).
- **Individual → corporate**: nginx (copyright line lineage from individual
  author to F5).
- **Infrastructure retired by its own biggest user**: zookeeper — Kafka 4.0's
  KRaft mode fully replaced it (primary-confirmed). The inverse of the
  "foundation engine" pattern (RocksDB, which underlies Kafka/Flink/TiKV/Ceph
  and only grows more load-bearing).

## Three safeguards that converge independently

These recur across projects that share no organizational lineage —
which is what makes them signal rather than culture:

### 1. Pre-work gates
Agreement *before* code is written, not review after:
- ory/kratos — every PR requires prior maintainer consultation.
- turborepo, strapi, NATS — same principle, independently adopted.
- spark — MLlib has explicit 5-condition acceptance criteria for new
  algorithms (adoption evidence, scalability, full documentation, …).

### 2. Power-concentration limits
- Homebrew — its Project Leadership Committee bylaws forbid any single
  employer from holding more than 2 seats.
- pytorch — technical governance and business governance structurally separated.
- graphql-js — changes require review from multiple distinct organizations.

### 3. Module-boundary discipline
"Advanced features go in plugins; no 'while we're here' changes" — verified
independently in Kong, prettier, hugo, npm/cli, Chart.js, apollo-server.

## Quality-gate outliers worth knowing

- npm/cli — 100% test coverage required to merge (strictest gate found).
- linux — every commit must build independently ("bisectability"), extending
  the quality gate along the *time* axis; also the origin of the DCO
  (Signed-off-by) provenance mechanism.
- sqlalchemy — the only catalog entry where GitHub PRs are never merged
  directly: all review goes through Gerrit.
- Chart.js — pixel-level image-baseline regression testing for visual output.

## Known-limits honesty rule

Exemplar status is not permanence. The catalog records primary-verified
limits alongside strengths — e.g. Airbnb's own engineering blog documents
webpack production builds degrading past 30 minutes at scale, prompting a
migration. Recording an exemplar's documented ceiling is part of what makes
the record trustworthy.
