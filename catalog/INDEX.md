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
| JanusGraph/janusgraph | Graph DB | Apache-2.0 | eBay, Target, Red Hat (official page); peer-reviewed survey listing + vendor-benchmark subject (Database/OUP, 2021) |
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
| SigNoz/signoz | APM | MIT (ee/ dir: Enterprise License) | Mailmodo case study (VP Eng, named): ~200GB/day logs (peak 500-600GB), 200+ microservices |

## Payments & fintech (added post-release — the provisional→verified cycle in action)

| Repository | Domain | License | Axes confirmed | Notes |
|---|---|---|---|---|
| juspay/hyperswitch | Payment orchestration | Apache-2.0 ★ | 5 of 6 (axis 5 ◇) | Quality gates primary-verified: mandatory `cargo clippy --all-features`, nightly rustfmt, coverage tooling, Cypress integration tests. Governance docs cover commit format, git workflow (no force-push to shared branches, no squash during review), style, and test policy. Maintainer activity current as of 2026-07. Production proof now ★ for the Flowbird case study specifically: originally published on hyperswitch.io/case-studies (now returning S3 AccessDenied on the live URL), it was read first-hand via a Wayback Machine archive, confirming vendor-published transaction-volume, UX (click-count reduction), uptime, and throughput figures — see "Evidence notes" below for verbatim quotes, source-version caveats, and the newer juspay.io/customer-stories/flowbird page's more conservative figures. This ★ covers Flowbird only: the same case-studies page also names other adopters (Recurly, Zurich, ShopLC, Narvar, and others) whose individual case studies have not been read first-hand and remain unverified (☆) — this entry does not claim production proof for adopters other than Flowbird. Independent third-party citation (axis 5) not yet found: ◇. |
| medusajs/medusa | E-commerce platform | MIT ★ | 5 of 6 (axis 1 ☆, axis 5 ◇) | Quality gates confirmed via CONTRIBUTING.md (develop branch, raw.githubusercontent.com, first-party): "All PRs should include tests for the changes that are included," with test-file locations specified (e.g. `packages/*/src/services/__tests__`); GitHub API confirms multiple CI workflows exist (`docs-test.yml`, `oas-test.yml`, `test-cli-with-database.yml`, `validate-http-types.yml`, among others) — existence only, current green/red status of the default branch not checked (the same scope limit was applied for SigNoz's quality-gate entry above; hyperswitch's own CONTRIBUTING.md-based quality-gate check did not record this explicit caveat, so it is not cited as a like-for-like precedent here). Governance docs, from the same CONTRIBUTING.md, cover 5 of 6 core areas: required commands, test policy, code structure (fork + test-project + storefront layout), code style ("All methods and endpoints should be documented using TSDoc."), and git workflow (fix/feat/docs branch prefixes, PRs to develop/v1.x, "All pull requests are squashed and merged."); explicit AI-generated-code boundaries are absent from this document and stay unconfirmed. Maintainer activity reconfirmed via GitHub API on 2026-07-15 (pushed_at 2026-07-15T10:40:15Z, not archived, 35,175 stars, 122 open issues — low ratio relative to star count); an earlier same-day check had recorded 35,172/114, an expected intra-day drift rather than a factual error. Production proof stays ☆, not upgraded: medusajs.com/blog/patyna/ (Medusa's own first-party case-study page, 2024-01-11) was read directly and, in the article's own narration, credits a 34% traffic increase and a 30% reduction in time-to-market for new features — this 30% figure is about feature time-to-market, correcting this row's prior wording ("30% shorter purchase flow"), which mischaracterized the same figure; separately, Patyna's own team is directly credited with estimating that Medusa "roughly halved" ongoing maintenance/debugging time. The article's only verbatim named quotes are from Jakub Zbąski, Co-founder/CEO of Rigby — a Medusa implementation partner/agency also listed on medusajs.com/experts/rigby — not from Patyna (the adopter) or from Medusa itself. Per this catalog's own stated principle that "every production claim traces to the adopter's own published words," a partner-agency's verbatim quote is held to a stricter standard than an adopter's own words even on a vendor's first-party page; this is a deliberate, stricter-than-literal policy choice — a literal reading of "a vendor's own case-study page counts as primary (★)" could arguably already support ★ per the hyperswitch precedent, but that reading is not adopted here. The EKI reference (20M+ product configurations migrated from Magento) dates to a 2026-07-10 review; the payment-module findings (clean `AbstractPaymentProvider` provider-strategy registry; no marketplace/split-payment support found in official docs) date to a separate 2026-07-12 review; both unchanged. Axis 5 (independent/third-party citation) remains ◇, unconfirmed. |
| killbill/killbill | Subscription billing | Apache-2.0 ★ | 5 of 6 (axis 1 ☆, axis 5 ◇) | License read first-hand (raw LICENSE, master): the standard Apache License 2.0 text — note it carries no project-specific copyright-holder line at the top (the Apache 2.0 template itself has none); GitHub API's detected license agrees (Apache-2.0); no NOTICE/COPYRIGHT/COPYING file and no dual-license or enterprise-edition split found at the repo root (top level only checked; per-module exceptions deeper in subdirectories were not exhaustively ruled out). Production proof ☆, deliberately not ★: every circulating adopter name — Groupon, Carfax, HP, Square, Rakuten, among others — originates from killbill.io's own logo wall and use-cases page, i.e. vendor-published. The vendor's scale claims ("billions processed annually", "15+ years in production", "100K+ subscriptions managed") were relayed via fetch-summarization, not copied glyph-for-glyph, and are treated as paraphrase. A testimonial naming Matt Cervarich (Director of Application Services, Carfax, "customer since 2015") is a real named-executive quote but is hosted on killbill.io — vendor-hosted, not an independent Carfax publication (same distinction as the Rigby-quote rule in the medusa row). The one adopter-published primary source located — Groupon's own 2014 engineering-blog post "Groupon adopts Kill Bill, the open-source Payments Platform" (engineering.groupon.com, 2014-11-03) — could not be read first-hand (HTTP 522 on three attempts; archive routes unavailable in this environment), so it remains indicated-but-unverified; Rakuten, HP, and Square have no adopter-published source located at all. Per the Flowbird rule ("★ only after the source is read first-hand"), axis 1 stays ☆ until an adopter's own page is actually read. Quality gates primary-verified: five workflow files confirmed via the GitHub contents API (ci.yml ≈7.3KB, codeql-analysis.yml, release.yml, snapshot.yml, sync.yml); ci.yml raw-read verbatim — triggers on push to master / pull_request / workflow_dispatch, delegates the build-and-test job to the reusable killbill/gh-actions-shared@java21 workflow (matrix: H2 "travis" / MySQL / PostgreSQL profiles on Java 21 temurin, Maven `test verify`), plus an e2e job that stands up MySQL 8.0 and runs the killbill-integration-tests suite via rake. Current green/red status of the default branch not checked (same scope limit as the SigNoz and medusa entries). Governance docs cover 4 of 6 core areas: build/test commands and code-structure guidance in the vendor development guide (docs.killbill.io/latest/development.html — Maven 3.5.2+/JDK 11+, multi-repository layout section); test policy in CONTRIBUTING.md, verbatim: "When submitting code, make sure to add [new tests]."; git workflow partially (fork + pull request, and a mailing-list-first gate, verbatim: "Do not open an issue or pull request on GitHub until you have collected positive feedback about the change on the Mailing-List."); code-style rules and any AI-generated-code policy are confirmed absent. Location caveat, recorded as a reconciled review discrepancy: the root path CONTRIBUTING.md returns 404 and one review pass initially concluded "no CONTRIBUTING.md, no test mandate" from that 404; a parallel pass located the actual file at .github/CONTRIBUTING.md (confirmed via the contents API and a raw read, which contains the test mandate above) — the .github/ finding supersedes the root-404 conclusion. Maintainer activity current: GitHub API on 2026-07-16 — pushed_at 2026-07-16T16:00:05Z (same day), latest release killbill-0.24.19 published 2026-07-09, five most recent commits all within 2026-07-14..16, 5,626 stars, 258 open issues (this API count includes open PRs), created 2012-10-21, not archived; the org's other repos (killbill-platform, killbill-admin-ui, plugin repos) were also all pushed within days. Axis 5 stays ◇ on a deliberate close call: the nearest find is a University of Zurich master's thesis (N. Gordillo, "Deploying a Mobile Application for Digital Onboarding", 2020, hosted on ifi.uzh.ch; PDF read first-hand) with a dedicated subsection on Kill Bill's catalog/billing-period/payment-retry behavior — substantive independent academic engagement, but a master's thesis is none of this catalog's three qualifying citation types (textbook, course, or peer-reviewed paper), so it is recorded as a near-miss rather than counted; no peer-reviewed paper or published technical book covering Kill Bill was found (searches are heavily noised by the Tarantino film of the same name). |
| jcam1/python-sdk | Stablecoin SDK | MIT ★ | 2 of 6 (axis 0 ★; axis 2 ☆ CI-existence only; axes 1/3/5 ◇; axis 4 below the 90-day criterion) | Provisional low-score entry. LICENSE read first-hand (raw file): verbatim "MIT License" / "Copyright (c) 2025 JPYC株式会社"; GitHub API's license field agrees. The development org is github.com/jcam1 (jpyc.co.jp stated on its profile); github.com/jpycoin ("JPYC Official") hosts only a single informational .github repo. Axis 1 stays ◇ on a deliberate distinction: adoption announcements exist for the JPYC token/payment method itself (e.g., Asteria's own press release announcing JPYC payment support in its "Click" no-code tool; CAICA Technologies' payment solution), but no adopter's own published statement of running this python-sdk repository in production was found — token adoption and SDK adoption are distinct claims, and only the former is evidenced. Axis 2 ☆ limited: three CI workflow files confirmed to exist via GitHub API (check.yml, ~1KB; create-release-pr.yml; publish.yml) — existence only, green status and coverage criteria unchecked. Axis 3 below threshold: CONTRIBUTING.md covers git workflow only (1 of 6 core areas; no build/test commands, test policy, code structure, style rules, or explicit boundaries incl. AI). Axis 4 below threshold: last push 2025-11-06, about 8 months before the 2026-07-16 check — outside the 90-day maintainer-activity criterion; repo created 2024-12-12; 2 open issues (a low count, noted alongside the low activity). Sibling repos are older still: JPYCv2 (contracts, MIT) last push 2024-10-21; sdk-examples 2024-08-29. Axis 5 ◇: no independent third-party citation (textbook, course, or peer-reviewed paper) found; community blog write-ups exist but are trial reports, not exemplar citations. A JPYC Node SDK monorepo mentioned in search results (reportedly linked to JPYCv2 via git submodules) could not be located among jcam1's public repositories — unconfirmed, not asserted nonexistent. |

### Evidence notes — juspay/hyperswitch, axis 1 (Production proof): Flowbird case study

**Source and version.** The figures below were read first-hand from a **Wayback Machine (web.archive.org) archive** of the original hyperswitch.io case-studies page, "Flowbird leverages Hyperswitch as strategic partner to solve for global parking payments," accessed directly in a browser session on 2026-07-14. The current live URL (`hyperswitch.io/case-studies/flowbird-leverages-hyperswitch-as-strategic-partner-to-solve-for-global-parking-payments`) returns an **S3 AccessDenied** error and could not be reached directly — the archive was the only route to first-hand content.

**Verbatim quotes (Wayback archive of the original hyperswitch.io page):**
- Payment volume: "350 million plus payment transactions every year"
- UX: "the average number of clicks required to complete a payment was reduced significantly, from 10 to just 3"
- Reliability: "reliable, scalable, agile, and high-performing, ensuring 99.999% uptime"
- Scale: "a cache-based shock absorber to manage peak traffic, scaling seamlessly up to 20,000 TPS"

Also stated on the same archived page (paraphrased, not verbatim): 7 million users; 6,000 cities across 80 countries; multi-region active-active deployment; PCI DSS compliance; Flowbird's own card-present system ("Archipel") self-integrated as a connector into Hyperswitch. The same archived page also names other adopters via case-study links/logos — Recurly, Zurich, ShopLC, Narvar, and others — but only the Flowbird case study's body text has been read first-hand; see the scope caveat below.

**Newer, separate first-party source.** A different, current page — `juspay.io/customer-stories/flowbird` — covers the same Flowbird relationship but with more conservative framing: monthly transaction volume of 650,000/month scaling to 1,000,000/month. **The 20,000 TPS figure, the 99.999% uptime figure, and the 10-to-3-clicks figure are not repeated on this newer page.** Readers should treat those three specific numbers as unconfirmed by the current first-party source.

**Required caveats (read before treating this as ★ evidence):**
1. **Source-version caveat:** verification was performed via the Wayback Machine archive of the original hyperswitch.io page; the live page currently returns S3 AccessDenied and was not reachable directly during this check.
2. **Vendor-published caveat:** every figure above is vendor-published (by Hyperswitch/Juspay itself), not an independently audited number. It carries the same limitation as every other case study in this catalog — it is not third-party verification (that remains axis 5, marked ◇ for this entry).
3. **Figure-nature caveat:** "350 million transactions/year" is Flowbird's total payment volume, not necessarily volume processed through Hyperswitch specifically. "20,000 TPS" is a stated scaling capability/ceiling, not a claim of sustained/persistent throughput. "99.999% uptime" is presented as a design/reliability target, not an independently measured/audited uptime statistic. In addition, the newer juspay.io/customer-stories/flowbird page revises the volume figure (650k/month → 1M/month) and omits the 10→3 clicks, 20,000 TPS, and 99.999% uptime figures entirely — treat those three numbers as unconfirmed by the current first-party source.
4. **Scope caveat:** this ★ upgrade applies only to the Flowbird case study confirmed above. The same hyperswitch.io case-studies page also names other adopters — Recurly, Zurich, ShopLC, Narvar, and others — via case-study links/logos; those individual case studies have not been read first-hand and remain unverified. Do not read this entry as confirming production proof for any adopter other than Flowbird; other named adopters stay at the ☆ (secondary-confirmed) level until their case studies are read directly.

## Considered and declined (recorded, not hidden)

redis, elasticsearch (Type A; both later re-added an AGPL-3.0 option — still
copyleft, conclusion unchanged) · terraform, sentry, consul, nomad (Type A′) ·
neo4j (current public repo is GPL-3.0 — strong copyleft; enterprise
AGPL+Commons Clause code withdrawn from GitHub since 3.5) · n8n (Type F) ·
mongodb (SSPL originator) — each with the specific disqualifying clause on
record.

*The full registry, per-entry axis scoring, and provisional entries pending
verification will follow in subsequent releases as their evidence is upgraded.*
