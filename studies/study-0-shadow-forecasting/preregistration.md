# Study 0 preregistration template

Status: **protocol candidate - must be frozen before Study 0 outcome inspection**

This document specifies the default design. A real deployment must fill all bracketed fields, record an immutable commit/hash, and obtain the required organizational authorization before collection.

## 1. Research questions

**RQ0 - Feasibility.** Can prospectively specified Forecast Contracts be elicited and resolved with low participant burden and without material interference in the observed engineering process?

**RQ1 - Forecast validity.** What probabilistic accuracy and calibration do independent forecasts, simple aggregates and a market aggregate exhibit on the resolved contract set?

**RQ2 - Incremental aggregation.** What is the paired difference in Brier score between the market close probability and the simple mean of independent pre-market forecasts?

**RQ3 - Conditions of usefulness (exploratory).** Is market gain associated with initial belief dispersion, role diversity, or the presence of locally held information?

## 2. Primary estimand

For admissible resolved binary contracts indexed by j:

\[
\Delta_j = BS(p^{M}_j,y_j)-BS(p^{mean}_j,y_j),
\qquad BS(p,y)=(p-y)^2.
\]

Primary estimand:

\[
\Delta = \frac{1}{J}\sum_{j=1}^{J}\Delta_j.
\]

Negative values favor the market aggregate on the observed contract set. The estimand is descriptive of the sampled contracts; external generalization requires additional studies.

If multiple contracts belong to the same operational episode, release, campaign, or tightly coupled event cluster, uncertainty resampling must occur at that cluster level rather than pretending each contract is independent.

## 3. Baselines

Required:

- `individual_mean`: arithmetic mean of independent pre-market probabilities;
- `individual_median`: median of independent pre-market probabilities;
- `market_close`: last valid market probability before the frozen close time.

Optional only when naturally available and prospectively defined:

- `designated_expert` or `owner_forecast`;
- `existing_data_model` produced for operational reasons independently of this study.

No baseline may be invented after seeing outcomes solely because it makes one method look better or worse.

## 4. Study window and stopping

Deployment must choose **one prospective stopping rule** before outcome visibility:

- fixed calendar window `[START, END]`; or
- fixed number `[J_TARGET]` of resolved admissible contracts with a maximum calendar end.

Recommended feasibility target: approximately 20-40 resolved contracts across multiple event families. This is an estimation target, not a universal power claim.

If fewer than 20 admissible contracts resolve by the frozen end, report feasibility/descriptive results and do not promote C2 as established.

No outcome-dependent early stopping is allowed.

## 5. Participants

Eligibility:

- legitimate professional knowledge relevant to at least one contract;
- voluntary consent under the applicable organizational process;
- no requirement to forecast every contract.

Per-contract fields:

- probability 0-100%;
- role category;
- information visibility: `common | local_to_role | mixed`;
- ability to influence outcome: `none | indirect | direct`;
- `outcome_already_known`: yes/no;
- category of additional evidence that would most change the estimate;
- optional short rationale only if approved for the private deployment.

`outcome_already_known=yes` is an abstention, not a forecast.

## 6. Independence and exposure

Independent forecasts must be collected **before** the participant can see the market state for that contract. The interface must not prepopulate a reference probability.

After the independent forecast is frozen, the participant may enter the market phase and see the market according to the chosen platform configuration.

## 7. Market configuration

Freeze and export:

- platform/product/version;
- market-maker algorithm and parameters;
- initial probability;
- virtual bankroll/reward rule;
- opening/closing times;
- participant visibility rules;
- whether rationales or social signals are visible;
- any AI/news/retrieval assistance.

Default Study 0 preference: disable external AI/news synthesis and automated web retrieval so the measured signal remains attributable to participating humans plus the market mechanism. Any deviation must be explicit.

## 8. Resolution and evidence

Each contract must pass the JSON schema and identify a pre-existing authoritative evidence source. Resolution is performed by a resolver who did not set the market price and follows the frozen rule mechanically where possible.

Resolution statuses:

- `RESOLVED_TRUE`
- `RESOLVED_FALSE`
- `VOID_AMBIGUOUS`
- `VOID_MISSING_EVIDENCE`
- `VOID_INTERFERENCE`

Voids remain in the audit ledger and are excluded from the primary scoring estimand for the declared reason; they are not deleted.

## 9. Interference classification

`I=0`: no observed change attributable to the forecasting exercise.

`I=1`: discussion/attention was triggered, but no material operational action or decision was changed.

`I=2`: forecast/market exposure materially altered the operational action, decision, timing, resource allocation, or evidence-generation path.

Primary Study 0 scoring excludes `I=2` contracts because the study is no longer observing the unperturbed path. Report them separately as protocol interference evidence.

## 10. Primary metrics

- Brier score by method;
- paired event/cluster-level Brier difference, market minus mean;
- contract resolution/void rate;
- participation rate and abstention rate;
- participant burden (median and distribution of completion time if collectable without surveillance);
- interference distribution.

Secondary/descriptive:

- calibration/reliability plot with uncertainty shown;
- log score with probabilities clipped prospectively at `epsilon=0.01` for numerical safety;
- forecast sharpness/dispersion, interpreted only alongside calibration;
- market movement from independent mean to close;
- belief dispersion using clipped logit probabilities;
- role diversity and local-information fraction;
- trajectories over time without treating timestamps as independent observations.

## 11. Randomness and uncertainty

Reference bootstrap seed: `20260925` unless deployment-specific preregistration freezes another integer before outcomes.

Default uncertainty summary for the primary paired difference: 10,000 nonparametric bootstrap resamples of the independent event **cluster** units, percentile 95% interval, plus the raw event-level paired differences. If fewer than 8 independent clusters exist, the interval is reported as exploratory and no asymptotic precision claim is made.

A sensitivity analysis reports the event-level paired mean and a cluster-robust or cluster-aggregated alternative when multiple contracts share a cluster.

## 12. Confirmatory vs exploratory boundary

Confirmatory for Study 0:

- RQ0 feasibility measures;
- RQ2 paired market-vs-mean estimand under the frozen admissibility rule.

Descriptive:

- calibration diagnostics given small sample sizes;
- mean/median/expert/model comparisons beyond the primary pair.

Exploratory:

- association of aggregation gain with diversity, local information, role, forecast movement, or actor/observer status;
- human-machine fusion.

## 13. Publication rule

Report null, adverse and ambiguous outcomes. Do not label the market "better" from a negative point estimate alone. State the sampled population, event families, calendar period, exclusion counts, uncertainty interval, and platform configuration.
