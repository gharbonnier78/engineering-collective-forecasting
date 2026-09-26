# Pedagogical map

This project applies the pinned harness Pedagogical Concept Contract. Scientific protocol and pedagogy are separate: a clear explanation is not evidence that a claim is true.

## Prediction market

**Intuition.** A market aggregates beliefs by letting participants move a shared price or probability.

**Engineering boundary.** In this project a market is a later mechanism, not the Study 0 instrument. When participants can influence the forecast outcome, showing them the market state can itself be an intervention.

**Misconception.** market probability = truth.  
**Correction.** It is a mechanism-dependent aggregate conditioned on participants, information and incentives.

**Understanding gate.** Explain why a market can aggregate information without neural-network training, and why visible prices can contaminate a shadow study.

## Proper scoring rule

**Intuition.** A probability score should make honest probability reporting optimal in expectation under its assumptions.

**Mathematical descent.** If a forecaster's true belief is q=0.7 and the reported probability is p, normalized binary Brier loss has expected value

    E[BS] = 0.7(1-p)^2 + 0.3 p^2.

This is minimized at p=0.7. At p=0.7 the expected loss is 0.21; at p=1 it is 0.30.

**Misconception.** proper = calibrated.  
**Correction.** Propriety is a property of the scoring rule; calibration is an empirical property of forecasts over cases.

**Understanding gate.** Differentiate truthful-report incentives from empirical calibration.

## Brier convention

This repository uses the normalized binary loss

    BS(p,y) = (p-y)^2.

For a binary two-category probability vector, Brier's original summed index is twice this value. The convention must be stated whenever results are compared with external work.

## Brier diversity identity

For the arithmetic mean p_bar,

    BS(p_bar,y)
      = mean_i BS(p_i,y)
        - mean_i (p_i-p_bar)^2.

**Intuition.** Averaging can reduce squared error because individual deviations partially cancel.

**Boundary.** This identity does not mean a simple average fully combines independent evidence. Multiple forecasters can each move modestly from a common prior while their pooled evidence would justify a more extreme posterior.

**Understanding gate.** Explain what the subtraction term represents and why the identity does not prove that averaging is an optimal probabilistic aggregator.

## Meta-prediction

**Intuition.** Alongside "what probability do you assign?", ask "what average probability do you expect the other forecasters to assign?"

Call the own forecast p_i and the peer-average meta-prediction m_i.

**Why it matters.** Meta-predictions can carry information about what the forecaster believes is shared versus privately known. Published work uses related elicitation to correct aggregation when information is shared or to identify latent expertise.

**Project implementation.** Study 0 evaluates, prospectively and without tuning, a simplified logit recalibration:

    L_bar = mean(logit(p_i))
    M_bar = mean(logit(m_i))
    p_meta = logistic(M_bar + a(L_bar-M_bar))

with a fixed a=2 candidate.

**Boundary.** This formula is a project implementation inspired by the literature, not a claim to reproduce Palley--Soll, Martinie--Wilkening--Howe or Peker--Wilkening exactly.

**Misconception.** m_i is the true shared prior.  
**Correction.** It is another noisy human judgment and may include projection/faux-consensus effects.

**Understanding gate.** Explain why own forecasts alone cannot always reveal which information is common to everyone.

## Forecast Contract

**Intuition.** A forecast cannot be audited unless the event and its resolution are fixed before the answer is known.

**Canonical project tuple.**

    F_j = (Q_j, Omega_j, T_j, R_j, E_j, A_j, B_j, C_j, X_j, S_j)

where the fields represent question, outcome space, timing, resolution rule, authoritative evidence, resolver, institutional references, context, exclusions and safeguards.

**Concrete example.** Replace "Will performance be good?" with a binary criterion tied to a fixed test, deadline, evidence source, base-rate family and resolver.

**Misconception.** precise wording guarantees a meaningful scientific target.  
**Correction.** A resolvable event can still be irrelevant, gameable or affected by the act of forecasting.

**Understanding gate.** Turn one vague engineering question into a resolvable contract and name one condition that should make it inadmissible.

## Calibration and sharpness

Calibration asks whether stated probabilities agree with observed frequencies across enough comparable cases. Sharpness asks how concentrated the forecasts are.

**Misconception.** more extreme = better.  
**Correction.** Extremity is useful only when supported by calibration and evidence.

## Diderot boundary

Canonical reusable versions belong in gharbonnier78/mmals-ml-wiki with external source notes, epistemic status, misconceptions and understanding gates. The project-local Forecast Contract must remain labelled as local terminology.
