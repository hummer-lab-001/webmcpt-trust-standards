# Catalog Index — Curated First Release

A curated subset of the full registry (130+ entries): the entries whose
evidence is strongest. Every license was confirmed against the LICENSE file
text; every production claim traces to the adopter's own published words.

Evidence: ★ primary-confirmed / ☆ secondary-confirmed / score = axes confirmed.

## Top tier (all six axes confirmed)

| Repository | Domain | License | Production evidence (example) |
|---|---|---|---|
| django/django | Web framework | BSD-3 | Instagram, official adopter statements |
| pytorch/pytorch | ML framework | BSD-style (Type C) | Meta + industry-wide, primary |
| nodejs/node | Runtime | MIT-equivalent (Type B) | Ubiquitous, foundation-governed |
| pytest-dev/pytest | Test framework | MIT | De-facto Python test standard |
| etcd-io/etcd | Distributed KV store | Apache-2.0 | Kubernetes' primary datastore (mutual in-catalog proof) |
| webpack/webpack | Build tool | MIT | Airbnb (incl. documented scale ceiling) |
| facebook/react | UI framework | MIT | Meta + industry-wide |
| prometheus/prometheus | Observability | Apache-2.0 | CNCF graduated |
| apache/kafka | Event streaming | Apache-2.0 | KIP process primary-verified; industry-wide |

## Strong candidates (4–5 axes confirmed)

| Repository | Domain | License | Notable evidence |
|---|---|---|---|
| kubernetes/kubernetes | Container orchestration | Apache-2.0 | CNCF flagship |
| golang/go | Language | BSD-3 | Official adopter page |
| psf/requests | HTTP client | Apache-2.0 | Ubiquitous |
| cli/cli | CLI tooling | MIT | GitHub official |
| aquasecurity/trivy | Security scanning | Apache-2.0 | Industry adoption, primary |
| flutter/flutter | Mobile framework | BSD-3 | Google + named adopters |
| apache/airflow | Data pipelines | Apache-2.0 | AIP process, ASF |
| prettier/prettier | Formatter | MIT | Ecosystem default |
| envoyproxy/envoy | Service proxy | Apache-2.0 | CNCF graduated; weighted-vote governance |
| godotengine/godot | Game engine | MIT | Sega title + academic citation |
| jenkinsci/jenkins | CI/CD | MIT | Elected-board governance |
| facebook/docusaurus | Docs generator | MIT | Meta in-house use, primary |
| apache/spark | Data processing | Apache-2.0 | MLlib acceptance criteria |
| gohugoio/hugo | Static site gen | Apache-2.0 | CGO boundary rule |
| npm/cli | Package manager | Artistic-2.0 (Type D) | 100% coverage gate |
| openssl/openssl | Cryptography | Apache-2.0 | CLA-level contribution governance |
| microsoft/TypeScript | Compiler | Apache-2.0 | Airbnb ts-migrate, primary |
| sqlalchemy/sqlalchemy | ORM | MIT | AOSA textbook chapter; Gerrit review |
| JanusGraph/janusgraph | Graph DB | Apache-2.0 | eBay, Target, Red Hat (official page) |
| open-telemetry/opentelemetry-collector | Observability | Apache-2.0 | CNCF "de-facto standard" statement, 2,800+ orgs |
| chartjs/Chart.js | Visualization | MIT | Image-baseline regression testing |
| memcached/memcached | Distributed cache | BSD-3 | USENIX NSDI'13 paper; MIT course material |
| temporalio/temporal | Durable workflows | MIT | Netflix, Stripe case studies (named pages) |
| timescale/timescaledb | Time-series DB | Apache-2.0 (+TSL dir) | Directory-split licensing, documented |
| goharbor/harbor | Container registry | Apache-2.0 | CNCF graduated; security built into core |
| colinhacks/zod | Schema validation | MIT | tRPC default validator (ecosystem default) |
| apollographql/apollo-server | GraphQL server | MIT | Expedia (adopter's own blog) + vendor case study |
| fluent/fluentd | Log collection | Apache-2.0 | CNCF graduated |
| torvalds/linux | OS kernel | GPL-2.0 + syscall-note | Bisectability rule; DCO origin |
| argoproj/argo-cd | GitOps CD | Apache-2.0 | CNCF graduated (Argo family) |
| argoproj/argo-workflows | Workflow engine | Apache-2.0 | Adobe, Bloomberg, NVIDIA (USERS.md) |
| apache/skywalking | APM | Apache-2.0 | Alibaba Cloud, Tencent, Huawei (official users) |
| astral-sh/ruff | Linter | MIT | In FastAPI's and pandas' own configs (in-catalog cross-reference) |
| grpc/grpc | RPC framework | Apache-2.0 | CNCF; industry-wide |
| curl/curl | Network transfer | curl license (MIT-style) | Everywhere; maintainer primary testimony |
| numpy/numpy | Numerical computing | BSD-3 | Nature paper |
| pandas-dev/pandas | Data analysis | BSD-3 | NumFOCUS-governed |
| git/git | Version control | GPL-2.0 only | Self-evident + version-pinning philosophy |

## Payments & fintech (added post-release — the provisional→verified cycle in action)

| Repository | Domain | License | Axes confirmed | Notes |
|---|---|---|---|---|
| juspay/hyperswitch | Payment orchestration | Apache-2.0 ★ | 5 of 6 (axis 5 ◇) | Quality gates primary-verified: mandatory `cargo clippy --all-features`, nightly rustfmt, coverage tooling, Cypress integration tests. Governance docs cover commit format, git workflow (no force-push to shared branches, no squash during review), style, and test policy. Maintainer activity current as of 2026-07. Production proof stays ☆: the vendor's own case-studies page names Recurly, Zurich, ShopLC and others, but the individual adopter statements have not yet been read first-hand — so ☆, not ★. Independent third-party citation (axis 5) not yet found: ◇. |
| medusajs/medusa | E-commerce platform | MIT ★ | 2 of 6 (production proof ☆) | Official docs cite Patyna (WooCommerce migration, 30% shorter purchase flow) and EKI (20M+ product configurations migrated from Magento); sources mix official docs with partner blogs, so ☆. Payment module is a clean provider-strategy pattern (`AbstractPaymentProvider` registry); no marketplace/split-payment support found in official docs — recorded as a limit, not assumed. |

## Considered and declined (recorded, not hidden)

redis, elasticsearch (Type A; both later re-added an AGPL-3.0 option — still
copyleft, conclusion unchanged) · terraform, sentry, consul, nomad (Type A′) ·
neo4j (current public repo is GPL-3.0 — strong copyleft; enterprise
AGPL+Commons Clause code withdrawn from GitHub since 3.5) · n8n (Type F) ·
mongodb (SSPL originator) — each with the specific disqualifying clause on
record.

*The full registry, per-entry axis scoring, and provisional entries pending
verification will follow in subsequent releases as their evidence is upgraded.*
