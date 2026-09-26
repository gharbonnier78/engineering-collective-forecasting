# Paper build

engineering_collective_forecasting.tex is the primary scholarly artifact.

From the repository root:

    make paper

The build wrapper sets:

- TZ=UTC
- SOURCE_DATE_EPOCH to the current Git commit time unless explicitly supplied
- FORCE_SOURCE_DATE=1

For a same-environment reproducibility check:

    make paper-repro

CI builds twice from the exact head, compares the resulting PDFs byte-for-byte, records the SHA-256 digest, and stores pdflatex/latexmk version information with the artifact.

The runner is pinned to ubuntu-24.04, but GitHub-hosted runner images and apt repositories evolve. Therefore the repository claims deterministic rebuilding **within the recorded build environment**, not eternal bit identity across future TeX distributions.

The PDF is a generated artifact; LaTeX source and the immutable Git commit are the scientific source of truth.
