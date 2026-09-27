# Chronicle — 2026-09-27 — publication-prep review candidate

Status: **append-only handoff; accepted Study 0 design preserved; no Study 0 outcomes exist**

## Work completed

The publication-preparation workstream now includes:

- an external-facing abstract and explicit protocol contributions;
- a dedicated related-work section;
- new source notes for Bayesian Truth Serum, Surprisingly Popular, logit aggregation/extremization, question-behavior effects, software expert estimation and hidden-expert/meta-prediction work;
- bounded operating-characteristic results for the Study 0B continuation rule;
- verbatim preservation of the independent-review simulation scripts with source SHA-256 guards and reference outputs;
- Independent Researcher affiliation/contact and a manuscript AI-assistance declaration;
- a publication authorization boundary consistent with G2;
- an immutable-release / Zenodo / OSF / Registered Report publication plan;
- improved Study 0 figure layout.

## Accepted scientific baseline

The scientific baseline remains the independently accepted and merged commit:

`b38feb509f9b3ed94e37f590b441e0e906601341`.

No publication edit changes the Study 0A/0B estimands, eligibility logic, same-time owner comparator, optional-base-rate subset, fixed meta-recalibration, actor/observer design factor, data-custody rule, cluster bootstrap or decision firewall.

## New design evidence

The publication paper reports toy operating characteristics only to explain the continuation gate.

Preserved source hashes:

- `sim_pivot.py`: `66d49f55365845484fbec94a2a0b3e82b392729c9f86f9ae543566c28fa39591`
- `sim_continuation.py`: `e0808ffc177e62ee7e051bb11575204dc1f2f56c67a9c9ccfb08078ed215ce30`

These simulations are not empirical Study 0 evidence and are not a universal power analysis.

## Visual verification

A 12-page exact-head CI PDF was rendered page-by-page during preparation. The remaining word break in the first figure was removed by shortening the top node to “planned events”. Final review must use the post-fix exact-head PDF.

## Pedagogical follow-up

The publication pass strengthens the concepts of meta-prediction and introduces measurement reactivity/question-behavior effect as a reusable validity concept. After the publication-preparation PR is accepted and merged, Diderot should be updated in a separate bounded PR so its source pin targets the immutable merged publication commit rather than this moving branch.

## Next admissible action

Replay exact-head assurance and deterministic PDF build, visually inspect the post-fix PDF, then request independent publication-readiness review using `reviews/PUBLICATION_REVIEWER_PROMPT.md`. Do not merge before that review.
