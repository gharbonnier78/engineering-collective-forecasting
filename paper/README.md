# Paper build

`engineering_collective_forecasting.tex` is the primary scholarly artifact for the protocol phase.

Build:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error engineering_collective_forecasting.tex
```

Expected packages: standard TeX Live LaTeX base/extra packages including `geometry`, `microtype`, `amsmath`, `booktabs`, `hyperref`, `natbib`, `tikz` and `xcolor`.

The repository does not treat a manually committed PDF as the source of truth. CI builds the PDF from the exact PR/head source and uploads it as a workflow artifact, preventing source/PDF drift.
