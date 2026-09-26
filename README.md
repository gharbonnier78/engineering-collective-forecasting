# Engineering Collective Forecasting

**Research question:** can distributed engineering knowledge become calibrated, auditable and incrementally useful probabilistic evidence beyond what the organization already knows, without perturbing the engineering process being observed?

This repository studies **private collective forecasting first**, then progressively more complex aggregation mechanisms. Prediction markets remain an important later hypothesis, but they are no longer the mechanism under test in Study 0.

> **Prediction is evidence, not authority.** Forecasts estimate uncertainty. Accountable engineering governance retains the decision.

## Status

- Repository phase: **protocol redesign after independent review**
- Independent review of bootstrap PR: **PARTIAL ACCEPT; G1 not released**
- Study 0A: **dry Forecast Contract funnel, not launched**
- Study 0B: **private shadow forecasting, not launched**
- Scientific claims: **none about operational benefit or prediction-market superiority**
- Primary artifact: paper/engineering_collective_forecasting.tex
- Method dependency: gharbonnier78/scientific-research-harness@e8e043c2b66a74ccacd023d67a32f989885449eb

## Minimum-sufficient research sequence

    Study 0A — dry contract funnel
        candidate engineering events
                  |
                  v
     important / uncertain / resolvable /
     non-interfering / confidentiality-safe
                  |
                  v
     prospectively frozen Forecast Contracts
                  |
                  v
     clean resolution from authoritative evidence

    Study 0B — private forecasting only
                  |
          same freeze time T_f
                  |
       +----------+-----------+
       |          |           |
    base rate   owner       private crowd
      R0          R1       p_i + meta m_i
       |          |           |
       |          |      frozen aggregator
       +----------+-----------+
                  |
                  v
          authoritative outcome
                  |
                  v
     paired Brier / skill / calibration

No collective aggregate is shown to participants, decision owners, or members of the study team who hold decision authority over that contract before resolution.

## Study 0 baselines

At the same frozen time T_f, Study 0B records:

- **R0 — base rate:** historical probability for the preregistered event family;
- **R1 — institutional signal:** accountable owner's private probability plus the official status already used by the organization;
- **R2 — private collective signal:** independent probabilities plus a meta-prediction of the average probability expected from peers.

The primary scientific question is **R2 vs R1**, with skill against **R0** as a required reference. Mean and median are retained; a prospectively fixed meta-belief recalibration is evaluated without tuning on Study 0 outcomes.

## Prediction markets

Prediction markets are moved to a later study. A market exposes an aggregate to its participants; when those participants can influence the engineering outcome, that exposure is itself an intervention. A later market study must therefore use an explicitly intervention-aware design or an observers-only arm and compare the market at the **same information time** with a qualified private-poll aggregator.

## Core object: Forecast Contract

A Forecast Contract prospectively freezes the event, cluster, private-forecast window, outcome space, authoritative evidence, resolver, institutional references, exclusions, data custodian and safeguards. It exists to prevent semantic drift after the outcome is known.

## Public/private boundary

The public repository contains only generic schemas, code, methods and approved aggregate results. Customer/program identifiers, employee identities, internal statuses, unreleased architectures, vulnerabilities, raw rationales and live vendor evaluations belong only in an approved private overlay that pins this repository by immutable commit.

## Validation

    python -m pip install -r requirements.txt
    python scripts/validate_repo.py
    python scripts/check_secrets.py
    python -m compileall analysis scripts tests
    python -m unittest discover -s tests -v
    make paper

The PDF workflow normalizes source dates, verifies two same-head builds have identical hashes in the recorded CI environment, and records the TeX toolchain versions with the artifact. This is a bounded reproducibility claim, not a promise that an unpinned future TeX distribution will emit the same bytes.

## Research boundary

Corporate prediction-market evidence, polling research, aggregation theory and meta-prediction literature motivate mechanisms and threats. They do not establish effectiveness in this engineering context. Study 0 first asks whether usable, resolvable events exist and whether private distributed forecasts add signal beyond institutional knowledge.

## License

Code: MIT. Original documentation: CC BY 4.0; see LICENSE-CONTENT.md.
