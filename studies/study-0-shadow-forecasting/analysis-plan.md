# Study 0 analysis plan

## Analysis unit

The unit of primary comparison is the **resolved Forecast Contract**. A market containing 100 trades still contributes one terminal probability to the primary paired comparison. If contracts are tightly coupled within an operational episode, define a `cluster_id` prospectively and resample/aggregate at the cluster level.

## Binary scoring

For forecast probability p and outcome y in {0,1}:

```text
Brier(p,y) = (p-y)^2
```

Lower is better. The primary per-contract contrast is:

```text
delta_j = brier(market_close_j, y_j) - brier(independent_mean_j, y_j)
```

A negative `delta_j` means the market was closer to the realized binary outcome on that contract. The primary summary is the mean delta over admissible contracts, with uncertainty resampled by independent cluster.

## Why the Brier score

The Brier score is a proper scoring rule for binary probabilistic forecasts and preserves information about confidence that accuracy-at-50%-threshold would discard. Proper scoring rules are used because the scientific object is a probability forecast, not a hard classifier.

## Calibration

Calibration asks whether events forecast near p occur at approximately frequency p across a sufficiently large comparable set. Study 0 is expected to be small, so reliability diagrams are descriptive and must display counts/uncertainty. Do not treat an empty or tiny bin as evidence of miscalibration.

## Sharpness

Sharpness is the concentration or decisiveness of forecasts independent of outcomes. It is valuable only conditional on adequate calibration. Report the distribution of probabilities and distance from the empirical base rate; do not reward extremity by itself.

## Belief dispersion

Independent probabilities are clipped to `[0.01,0.99]` before logit transformation:

```text
D_belief,j = SD(logit(p_ij))
```

This captures disagreement on a scale where 0.9 vs 0.99 is not treated as the same absolute change as 0.5 vs 0.59. It is exploratory.

## Role diversity

Let q_r be the fraction of participating forecasters in role category r. A normalized Shannon index may be reported:

```text
D_role = -sum_r q_r log(q_r) / log(R)
```

where R is the number of role categories represented in the eligible role taxonomy. This is a descriptive proxy, not direct measurement of cognitive diversity.

## Information locality

Report the fraction of valid independent forecasts marked `local_to_role` or `mixed`. Do not ask participants to disclose confidential information in order to prove locality.

## Market trajectory

Trajectory data are useful for describing belief updates and sudden movements. They are nested within a contract. Do not inflate sample size by treating every timestamp as an independent forecast event.

## Missingness and voids

Retain every registered contract. Distinguish:

- no participant forecast;
- incomplete market phase;
- missing authoritative evidence;
- ambiguous resolution;
- interference;
- technical platform failure.

Voids remain part of feasibility results even when excluded from predictive scoring.

## Reference implementation

`analysis/reference_analysis.py` implements Brier scores, paired contrasts, logit belief dispersion, a simple normalized role-diversity index, and a cluster bootstrap using only the Python standard library.
