# Chronicle — 2026-09-26 — independent review and minimum-sufficient redesign

Status: **append-only protocol amendment; no Study 0 outcomes exist**

## Review disposition preserved

Independent review of PR #1 at bootstrap head c8a3516 returned:

**PARTIAL ACCEPT — scaffold accepted; scientific core not accepted; G1 not released.**

The review found the harness/provenance scaffold, Forecast Contract discipline, private-first intent, contract/cluster unit, non-claims and HR safeguards valuable, while identifying six blocking scientific issues and eleven major implementation/provenance issues.

This Chronicle entry does not overwrite the 2026-09-25 bootstrap record. It records why the design changed before any prospective outcome existed.

## Blocking findings accepted

### B1 — comparator was not decision-relevant

The old primary estimand compared market close with the simple mean of private forecasts. It did not require comparison with what the organization already knew.

**Change:** Study 0B now requires, at the same freeze time:

- R0 historical base rate;
- R1 accountable owner's private probability plus official status;
- R2 private collective forecast.

The primary paired contrast is crowd vs owner; base-rate skill is a required reference.

### B2 — market exposure perturbs actors

A market necessarily reveals an aggregate to its participants. Participants may also influence the engineering outcome.

**Change:** the prediction market is removed from Study 0. Study 0B exposes no collective aggregate before resolution. A market is deferred to a later intervention-aware or observers-only study.

### B3 — market-vs-mean mixed mechanisms and timing

The old comparison conflated later information, probability averaging conservatism, crowd composition and market mechanics.

**Change:** all Study 0 references are frozen at the same information time. Mean/median remain baselines; a fixed private meta-belief recalibration is evaluated without tuning on Study 0.

### B4 — Study 0 scale cannot support a strong market null/superiority claim

**Change:** Study 0 becomes feasibility plus estimation of private collective skill. Prediction-market residual value is not tested at this scale.

### B5 — decision-owner separation must include the study team

**Change:** an independent data custodian controls pre-resolution aggregate access. Any principal investigator or analyst with decision authority over a contract is denied pre-resolution aggregate access for that contract.

### B6 — actor/observer is a design factor

**Change:** ability_to_influence is mandatory; participant-composition rules are frozen; actor-only and observer-only aggregates are reported.

## Major findings accepted

- minimum participant/composition admissibility is now explicit;
- interference is assessed by a declared role and is a sensitivity factor rather than a post-treatment void;
- schema requires status, cluster, institutional references, timing and freeze semantics;
- templates are validated against the schema in CI;
- tests include a mutation-sensitive cluster-resampling check and reject fewer than two clusters;
- target population, equal-contract weighting and cluster thresholds are explicit;
- G8 now points to Study 3 decision-value work;
- SDR-002 removal test is applied by removing the market from Study 0;
- AI-assistant consultation is recorded as shared-information metadata;
- bibliography is made canonical through references.bib and new source notes;
- assurance adds static compile and high-signal secret-pattern review;
- PDF build is redesigned around normalized source dates, same-head hash comparison and recorded TeX versions.

## Minimum-sufficient sequence after redesign

1. **Study 0A — dry contract funnel:** 4–6 weeks, no participants, no platform.
2. **Study 0B — private collective forecasting:** base rate + owner + official status + private forecasts/meta-predictions, same freeze time, no aggregate exposure.
3. **Study 1 — replication/private aggregation.**
4. **Study 2 — residual prediction-market value.**
5. **Study 3 — intervention/decision value.**

## New pedagogical obligations

The redesign adds or strengthens:

- Brier-score convention;
- Brier diversity identity for an arithmetic mean;
- meta-prediction;
- shared-information/meta-belief recalibration;
- actor/observer forecast bias as a threat/design factor;
- clarity/resolvability lineage for Forecast Contracts.

These are handed to Diderot under its own review and epistemic-status rules.

## Non-claims preserved

- No empirical Study 0 result exists.
- No claim that prediction markets are superior for engineering.
- No claim that a private crowd is superior to the owner or base rate.
- No claim that the project's meta-recalibration exactly implements a published algorithm.
- No claim of zero interference; only detected interference can be measured.
- No forecast is authorized as a release/governance decision input.

## Gate consequence

G1 remains **PENDING_REREVIEW**. The next admissible action after the implementation and exact-head CI replay is a new independent review. No merge and no pilot authorization are implied by this redesign.
