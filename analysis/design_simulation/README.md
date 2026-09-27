# Design simulations

These files preserve the independent design-review simulations that motivated two protocol choices before Study 0 outcomes existed:

1. a fixed meta-prediction recalibration as a cautious private aggregator candidate;
2. the interpretation of the Study 0B continuation rule as a screening/non-inferiority gate rather than a superiority test.

They are **design evidence**, not empirical Study 0 evidence.

## Provenance

The Python files are preserved verbatim from the independent review appendices.

- `sim_pivot.py`
  - frozen seed: `20260926`
  - independent-review SHA-256: `66d49f55365845484fbec94a2a0b3e82b392729c9f86f9ae543566c28fa39591`
- `sim_continuation.py`
  - frozen seed: `20260927`
  - independent-review SHA-256: `e0808ffc177e62ee7e051bb11575204dc1f2f56c67a9c9ccfb08078ed215ce30`

The reference outputs in this directory were independently reproduced during the publication-preparation pass using Python 3.13.5 and NumPy 2.3.5.

## Replay

```bash
python -m venv .venv-design
. .venv-design/bin/activate
python -m pip install -r analysis/design_simulation/requirements.txt

cd analysis/design_simulation
python sim_pivot.py
python sim_continuation.py
```

Compare with the two `reference-output-*.txt` files.

## Inferential boundary

The simulation assumes a stylized Bernoulli outcome process, a specific public/private signal model, six private forecasters, and independent contracts across clusters. That last assumption is optimistic. The outputs characterize the protocol rule under these assumptions only. They do not estimate the effect of collective forecasting in an engineering organization and do not provide a universal sample-size requirement.
