# Engineering Collective Forecasting

**Research question:** can distributed engineering knowledge be transformed into calibrated, auditable and incrementally useful probabilistic evidence without interfering with the engineering process being observed?

This repository studies **individual forecasting, simple aggregation, prediction markets, and later human-machine ensembles** as evidence sensors for engineering uncertainty. The first study is deliberately conservative: a **shadow-mode** protocol that forecasts outcomes of engineering activities that were already planned, without exposing forecasts to operational decision owners before resolution.

> **Prediction is evidence, not authority.** Forecasts estimate uncertainty. Accountable engineering governance retains the decision.

## Status

- Repository phase: **bootstrap / protocol design**
- Study 0: **not launched**
- Scientific claims: **none about operational benefit yet**
- Primary artifact: `paper/engineering_collective_forecasting.tex`
- PDF: built reproducibly by CI and uploaded as the `engineering-collective-forecasting-paper` workflow artifact
- Method dependency: `gharbonnier78/scientific-research-harness@e8e043c2b66a74ccacd023d67a32f989885449eb`

## Core objects

The study revolves around a versioned **Forecast Contract**. A contract fixes the forecast question, outcome space, opening/closing/resolution times, objective resolution rule, authoritative evidence, resolver role, shared context, exclusions, and safeguards before forecasts are analyzed.

Study 0 compares, at minimum:

1. independent private forecasts;
2. simple mean/median aggregation;
3. a prediction-market aggregate;
4. a designated-expert forecast when naturally available.

A data/model forecast may be added only when it already exists for operational reasons; Study 0 does not create a large ML model merely to stage a human-vs-AI contest.

## Repository map

```text
AGENTS.md                         agent startup and mutation rules
harness-adoption.yaml             immutable harness dependency and local adoption
paper/                            arXiv-like preprint source + bibliography
studies/study-0-shadow-forecasting/
                                  protocol, preregistration, analysis, threats, safeguards
schemas/forecast-contract.schema.json
                                  machine-readable Forecast Contract contract
templates/                        forecast, resolution and event-register templates
analysis/                         reference analysis code
research/sources/                 reviewed source notes
research/chronicle/               append-only research decisions and handoff
reviews/                          independent AI reviewer prompt and review form
docs/                             data governance, Hypermind instrumentation note, roadmap
.github/workflows/                assurance and PDF build
```

## Study 0 in one diagram

```text
existing engineering activity
          |
          v
  frozen Forecast Contract
          |
   +------+------+
   |             |
private       market phase
forecasts        |
   |             |
mean/median      |
   +------+------+
          |
   frozen predictions
          |
          v
existing authoritative evidence ----> resolved outcome
          |                                  |
          +---------------+------------------+
                          v
             calibration / Brier score /
          incremental value / interference
```

## Public-repository boundary

This repository is intentionally **generic and non-sensitive**. Internal project names, customer identifiers, unreleased architecture, vulnerability details, proprietary metrics, employee identities, and raw internal rationales must not be committed here. A deployment-specific overlay belongs in an approved private system of record and should reference this public protocol by immutable commit.

## Quick validation

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

Build the paper locally with a LaTeX distribution:

```bash
make paper
```

## Evidence status

The literature supports the feasibility of prediction markets as information-aggregation mechanisms in several corporate and forecasting settings, but those findings do **not** establish effectiveness in this engineering context. Study 0 exists to test the local question with explicit baselines, resolution evidence, interference controls, and bounded claims.

## Related research boundaries

Natural future links exist to probabilistic engineering models, executable/evidence contracts, human-machine forecasting, and sequential evidence acquisition. These are recorded as **extensions**, not as assumptions required to justify Study 0. In particular, GO-ED-POMDP is not part of the Study 0 causal or statistical claim.

## License

Code is released under the MIT License. Original documentation is intended for reuse under CC BY 4.0; see `LICENSE-CONTENT.md`.
