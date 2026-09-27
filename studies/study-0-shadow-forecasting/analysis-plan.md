# Study 0 analysis plan

## 1. Analysis unit and target population

The primary unit is the **resolved Forecast Contract**, not a participant response, timestamp, or trade.

The target population must be frozen prospectively as all admissible contracts encountered during the declared calendar window and event families. Each contract receives equal weight in the primary estimand unless the deployment-specific preregistration declares otherwise.

Contracts from the same release, campaign, environment episode or tightly coupled operational episode share a prospective cluster_id. Uncertainty is resampled by cluster.

## 2. Binary scoring convention

For probability p in [0,1] and outcome y in {0,1}:

    BS(p,y) = (p-y)^2

This repository uses the normalized one-component binary quadratic/Brier loss. For a two-category probability vector, the original Brier formulation sums both category errors and is twice this quantity. All code, tables and claims in this repository use the normalized convention above.

Lower loss is better.

## 3. Institutional references

Every primary-analysis contract must contain, at the same freeze time:

- p_owner: accountable owner's private probability;
- official_status: the status already used by the organization.

When a defensible historical reference class exists, also freeze:

- p_base: historical base-rate probability;
- base_rate_status = available.

When it does not, set `base_rate_status = unavailable` with a reason. Base-rate unavailability does **not** remove an otherwise-admissible contract from the primary crowd-vs-owner contrast.

Official status is not silently mapped to a probability unless such mapping was frozen before outcomes.

## 4. Private collective forecasts

An eligible forecaster must have prospectively established role-relevant knowledge of the event, the system/process producing it, or its authoritative evidence path. Uninformed observers cannot be recruited merely to satisfy composition quotas.

For each eligible forecaster i:

- p_i: own probability;
- m_i: expected average probability from peers.

The accountable owner is captured separately as the institutional comparator. If the owner also qualifies as a crowd forecaster, the primary crowd aggregate excludes that owner; an including-owner aggregate is descriptive.

All values are private until outcome resolution.

Required simple aggregators:

- arithmetic mean of p_i;
- median of p_i.

Primary protocol candidate:

    L_i = logit(clip(p_i))
    M_i = logit(clip(m_i))
    L_bar = mean(L_i)
    M_bar = mean(M_i)
    p_meta = logistic(M_bar + a * (L_bar - M_bar))

with clip interval [0.01,0.99] and a = 2.0 fixed prospectively.

This implementation is inspired by meta-belief/shared-information aggregation literature. It is not asserted to be an exact implementation of any one published method.

## 5. Primary paired contrasts

For each otherwise-admissible resolved contract j:

    delta_owner_j = BS(p_meta_j,y_j) - BS(p_owner_j,y_j)

For contracts with `base_rate_status = available`:

    delta_base_j  = BS(p_meta_j,y_j) - BS(p_base_j,y_j)

Primary summary over the full owner-comparable target population:

    mean(delta_owner_j)

Required reference summary over the explicitly enumerated base-rate-available subset:

    mean(delta_base_j)

Negative values mean lower observed loss for the crowd aggregate on the sampled target population.

The study does not infer operational decision value from these score differences.

## 6. Cluster bootstrap

Bootstrap independent cluster identifiers, not individual contracts when contracts are clustered.

When a cluster is drawn, all contracts belonging to that cluster are included together. This preserves within-cluster dependence.

The reference implementation:

- rejects fewer than 2 clusters;
- uses a frozen seed;
- returns point estimate plus percentile interval;
- never treats repeated forecasts from the same contract as independent.

If there are fewer than 8 independent clusters, interval-based inference is labelled exploratory.

## 7. Actor / observer factor

ability_to_influence is mandatory:

- none = observer;
- indirect or direct = actor.

Report:

- the primary crowd aggregate excluding the accountable owner;
- the descriptive including-owner aggregate when the owner also forecast as an eligible participant;
- actors only;
- observers only.

The participant-composition rule is prospectively frozen. A contract that does not meet the rule remains in funnel/feasibility reporting but is outside the primary forecast comparison.

## 8. Belief dispersion

For at least two private forecasts:

    D_belief = SD(logit(clip(p_i)))

For fewer than two forecasts, dispersion is undefined and the implementation raises rather than returning zero.

## 9. Role diversity

For role proportions q_r over a prospectively defined eligible taxonomy of R categories:

    D_role = - sum_r q_r log(q_r) / log(R)

The implementation requires eligible_role_count explicitly. It must not silently use only the categories observed in one contract.

Role diversity is a descriptive proxy, not direct measurement of cognitive or information diversity.

## 10. Brier diversity identity

For the arithmetic mean p_bar:

    BS(p_bar,y)
      = mean_i BS(p_i,y)
        - mean_i (p_i-p_bar)^2

This exact identity explains one benefit of averaging: disagreement can cancel individual squared error. It does **not** imply that a simple mean fully pools independent evidence; probability averaging can remain conservative when forecasters each condition on only part of the available information.

## 11. Calibration and sharpness

Calibration diagnostics are descriptive at Study 0 scale. Reliability plots must show counts and uncertainty.

Sharpness is interpreted only alongside calibration. Greater extremity alone is not evidence of better forecasting.

## 12. Base-rate skill

A descriptive skill score may be reported:

    Skill_base = 1 - mean(BS_crowd) / mean(BS_base)

only when the base-rate construction was frozen and the denominator is non-zero.

The paired `delta_base` is a required reference only on contracts with a prospectively defensible base rate because it preserves event-level pairing without biasing the primary crowd-vs-owner target population toward routine event families.

## 13. Interference

Primary analysis is intention-to-observe: otherwise resolvable contracts remain included regardless of I=0/1/2.

Sensitivity analysis excludes detected I=2 contracts. Report detected interference descriptively by role category (accountable owner, actor, observer) because elicitation-induced reflection may differ by ability to influence the outcome.

The interference assessor and assessment timing must be frozen before outcomes. The assessor should not see forecast accuracy when feasible.

## 14. Missingness and voids

Retain every registered candidate and contract. Distinguish:

- failed funnel criterion;
- insufficient participant composition;
- owner forecast missing;
- base rate unavailable (retain for the primary owner contrast; omit only from base-rate-specific summaries);
- outcome already known to a participant;
- missing authoritative evidence;
- ambiguous resolution;
- technical collection failure.

VOID status is limited to resolution ambiguity or missing evidence. Interference is not used as a post-treatment void rule.

## 15. Market analyses

There is no market primary or secondary analysis in Study 0.

A later prediction-market study must compare a market with a qualified private aggregator at the same information time, use an intervention-aware design or observers-only arm, and separately qualify thin-market/liquidity settings.

## 16. Reference implementation

analysis/reference_analysis.py implements:

- normalized binary Brier loss;
- simple private aggregation;
- meta-belief recalibration;
- belief dispersion;
- role diversity with explicit eligible taxonomy size;
- paired event contrasts;
- cluster bootstrap with a minimum-cluster guard.

Tests include a mutation-sensitive case that fails if cluster-level resampling is replaced by event-level resampling.
