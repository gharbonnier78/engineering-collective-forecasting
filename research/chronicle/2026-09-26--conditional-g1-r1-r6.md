# Chronicle — 2026-09-26 — conditional G1 rereview closure work

Status: **append-only protocol amendment; no Study 0 outcomes exist**

## Independent rereview disposition

The independent rereview of PR #1 at head `a936054` returned:

**PARTIAL ACCEPT (conditional). The scientific core is accepted. G1 may be released after bounded corrections R1–R6 are verified on a new head; no third full review is required.**

The reviewer confirmed closure of the original blocking findings B1–B6 and most major/minor findings, then requested six operational/scientific clarifications.

## R1 — Study 0A decision rule

Accepted.

The preregistration now freezes, before the intake window:

- protocol-candidate minimum admissible yield `Y_min = 0.30`;
- minimum clean-resolution rate `R_clean_min = 0.80`;
- `J_min = 30` and `K_min = 8`;
- maximum projected time to reach both: `T_projected_max = 26 weeks`.

The funnel template now records:

- identification, drafting-start, freeze and resolution timestamps;
- drafting effort;
- potential eligible actors and observers;
- controlled rejection reason.

Base-rate availability is recorded but is not itself an admission criterion.

## R2 — forecaster eligibility and accountable owner

Accepted.

Eligible forecasters must have legitimate role-relevant knowledge of the event, the generating system/process, or the authoritative evidence path. Observer quotas cannot be filled with uninformed participants.

The accountable owner remains the R1 institutional comparator. If independently eligible, the owner may also submit an R2 forecast, but the **primary crowd aggregate excludes the owner**. An including-owner aggregate is descriptive.

## R3 — no-base-rate contracts

Accepted.

A missing defensible historical base rate no longer removes an otherwise-admissible contract from the primary crowd-vs-owner target population.

- `Delta_owner`: all otherwise-admissible resolved contracts.
- `Delta_base`: only the prospectively enumerated `base_rate_status=available` subset.

The Forecast Contract schema now represents `base_rate_status = available | unavailable` and requires an unavailability reason when needed.

## R4 — continuation margin and operating-characteristic boundary

Accepted.

The protocol-candidate gate freezes `delta_NI = 0.02` with `J_min=30`, `K_min=8` unless a deployment chooses different values before Study 0A and records the rationale.

The rereview's toy operating-characteristic analysis is treated as **design-review evidence only**, not Study 0 evidence. It showed that at about 32 contracts, `delta_NI=0.02` can reject a crowd that is clearly worse than the owner but has limited ability to distinguish near equality from modest advantage.

The preregistration therefore states explicitly:

- Study 0B is a screening/non-inferiority continuation gate, not a superiority test;
- it cannot establish that the crowd is better at this scale;
- a deployment needing reliable discrimination near equality must plan a larger `J` prospectively, not widen the margin after outcomes.

## R5 — exact-head PDF build and citation

Accepted in implementation.

The paper workflow now checks out the exact PR head SHA on pull requests, records both workflow-trigger SHA and checked-out head SHA, asserts the checked-out SHA, and records the PDF's own SHA-256 in `paper-sha256.txt`.

The artifact archive digest is not used as the paper hash.

## R6 — Figure 1 arrows

Accepted.

Institutional references, private crowd forecasts and the authoritative outcome now all point to the evaluation node. Forecasts no longer visually point into the outcome.

## Non-blocking recommendations adopted

- The "institutionally positive/green but private crowd < 0.50" output is pre-specified as descriptive, with the exact positive/green status set frozen before collection.
- Detected interference is reported by accountable owner, actor and observer role.
- Study 3 depends on Study 1, not on Study 2; prediction-market research is not on the critical path to operational-value research.
- All five public templates are now covered by structural/semantic validation.
- TeX quote, bibliography proper-noun and layout nits were cleaned where applicable.

## Gate consequence

G1 remains **PENDING_REREVIEW** until an independent verifier checks R1–R6 on the new exact head. If those bounded items pass, the rereview explicitly permits G1 release without another full scientific review.
