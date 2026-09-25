# Pedagogical map

This project uses the pinned harness Pedagogical Concept Contract. The public paper is not enough by itself: difficult concepts should remain teachable, executable and connected to authoritative sources.

## Concepts introduced or materially re-encountered

### Prediction market

**Intuition.** A market is used as an information-aggregation mechanism: participants move a price when their own probability differs from the current collective probability.

**Concrete example.** If a binary contract pays one unit when a qualification criterion is met and the current market probability is 0.55, a participant who believes 0.75 has an incentive, under an appropriate mechanism, to move the market upward.

**Mathematical anchor.** A market scoring rule can update a state-dependent score/cost as reports change. LMSR is one mechanism; the research question does not depend on LMSR being uniquely correct.

**Misconception.** `market probability = truth`. Correction: it is an aggregated forecast conditional on mechanism, participation, incentives and information.

**Understanding gate.** Explain why a market can aggregate information without training neural-network weights, and name at least two reasons the market probability can be biased.

### Proper scoring rule

**Intuition.** A scoring rule evaluates a probability in a way designed not to reward strategic misreporting of belief in expectation.

**Concrete example.** For a binary event, Brier loss `(p-y)^2` penalizes a confident wrong probability more than a cautious wrong probability.

**Mathematical anchor.** Strict propriety means the expected score is uniquely optimized by reporting the forecaster's true predictive distribution under the scoring model.

**Misconception.** `proper = calibrated`. Correction: propriety is an incentive/evaluation property of the score; calibration is an empirical property of a set of forecasts.

**Understanding gate.** Given two probabilities and an outcome, compute both Brier losses and explain why lower loss does not by itself establish calibration.

### Forecast Contract

**Intuition.** A forecast cannot be audited unless everyone can later agree what was predicted and how reality will be resolved.

**Concrete example.** Replace "Will performance be good?" with a binary criterion tied to a fixed test, threshold, deadline and authoritative report.

**Mathematical anchor.** `F_j=(Q_j,Y_j,T_j,R_j,E_j,A_j,...)` is a local tuple collecting semantics, time, resolution rule, evidence and authority. It is a project formalism, not established external terminology.

**Misconception.** `precise wording guarantees a meaningful target`. Correction: a perfectly resolvable event may still be irrelevant, gameable, or causally entangled with the forecasting process.

**Understanding gate.** Transform one vague engineering question into a resolvable contract and identify a void condition.

### Calibration and sharpness

**Intuition.** Calibration asks whether probabilities match long-run frequencies; sharpness asks how concentrated/decisive forecasts are. Sharpness is desirable only if calibration is adequate.

**Misconception.** `more extreme probabilities are better`. Correction: unjustified extremity worsens proper scores and can destroy calibration.

**Understanding gate.** Explain how two forecasters can have similar Brier scores but different calibration/sharpness profiles.

## Diderot boundary

Canonical reusable versions of these notions should be maintained in `gharbonnier78/mmals-ml-wiki` with source notes, prerequisite links, misconceptions and understanding gates. This file remains the project-local pedagogical map tied to Study 0.
