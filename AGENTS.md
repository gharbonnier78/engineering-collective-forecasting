# Agent instructions - Engineering Collective Forecasting

This repository adopts `gharbonnier78/scientific-research-harness` as its versioned scientific and pedagogical method contract.

## Mandatory startup

Before substantive work:

1. Read `harness-adoption.yaml`.
2. Load the exact immutable harness ref declared there, beginning with `HARNESS.md`.
3. Load relevant companion contracts, especially:
   - `pedagogy/PEDAGOGICAL_CONCEPT_CONTRACT.md`;
   - `pedagogy/MATHEMATICAL_NOTATION_CAPITALIZATION.md` when new notation is introduced;
   - `templates/independent-pr-review-request.md` for delegated review.
4. Emit a startup record into the append-only Chronicle before outcome-bearing work.
5. Keep **source / claim / evidence / decision / pedagogy** distinct.
6. Do not infer harness compliance from memory or from a moving branch.

Pinned harness entrypoint:
`https://github.com/gharbonnier78/scientific-research-harness/blob/e8e043c2b66a74ccacd023d67a32f989885449eb/HARNESS.md`

## Scientific boundary

Study 0 is a **protocol** until prospective data are collected. Do not write results in the past tense, fabricate forecasts, simulate outcomes and present them as evidence, or promote hypotheses because the mechanism is intuitively attractive.

The primary scientific unit is the **resolved Forecast Contract**, not a trade, participant, or timestamp. Repeated market updates are nested observations. Related contracts may also share an operational cluster and must not be treated as independent when analysis requires clustering.

## Frozen-before-outcome rule

Before any study outcome is inspected, freeze at minimum:

- Forecast Contract and version/hash;
- participant eligibility and abstention rules;
- market configuration and algorithm/version;
- baseline definitions;
- primary estimand and scoring rule;
- exclusion/interference rule;
- stopping rule;
- random seed and resampling plan when used.

Any amendment after outcome visibility must be recorded as post hoc and cannot silently replace the preregistered analysis.

## Organizational non-interference rule

Study 0 is shadow-mode. Forecast outputs must not be used to alter the observed engineering decision, release gate, staffing decision, supplier evaluation, or individual performance management before outcome resolution. If the study changes the operational path materially, record interference and apply the preregistered exclusion/sensitivity rule.

## Confidentiality rule

This is a public repository. Never commit customer/project identifiers, employee identities, credentials, unreleased system details, raw proprietary evidence, vulnerability details, or confidential free-text rationales. Use synthetic/generic examples in public artifacts. Deployment-specific data belong in an approved private store.

## Pedagogical obligation and Diderot

When the work introduces or materially re-encounters difficult concepts, apply the pinned Pedagogical Concept Contract: intuition -> concrete example -> mathematical descent -> plain-language interpretation -> executable check -> misconception -> understanding gate.

Canonical reusable teaching concepts should be proposed to `gharbonnier78/mmals-ml-wiki` (Diderot), not duplicated indefinitely here. Current concepts expected from this bootstrap include prediction markets, proper scoring rules, Brier score, forecast calibration, and Forecast Contracts. Diderot explanations remain pedagogical and do not become scientific authority.

## Mutation and review

- Work on a review branch; do not silently mutate `main`.
- Keep the PR draft until independent review and exact-head checks are available.
- An AI reviewer must inspect the real PR diff, this file, the local adoption manifest, the pinned harness, preregistration, claims, source notes, Chronicle, tests/CI, and paper source.
- Reviewers must not merge or edit the branch as part of an independent review.
- Negative findings, ambiguity, null results, and invalidated assumptions must be preserved rather than rewritten away.
