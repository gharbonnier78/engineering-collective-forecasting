#!/usr/bin/env bash
set -euo pipefail

export TZ=UTC
export SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-$(git show -s --format=%ct HEAD)}"
export FORCE_SOURCE_DATE=1

cd "$(git rev-parse --show-toplevel)/paper"
latexmk -pdf -interaction=nonstopmode -halt-on-error engineering_collective_forecasting.tex
