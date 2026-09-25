#!/usr/bin/env python3
"""Fail-closed structural checks for the research bootstrap."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "AGENTS.md",
    "harness-adoption.yaml",
    "research/claims.yaml",
    "research/gates.yaml",
    "studies/study-0-shadow-forecasting/preregistration.md",
    "studies/study-0-shadow-forecasting/analysis-plan.md",
    "studies/study-0-shadow-forecasting/organizational-safeguards.md",
    "schemas/forecast-contract.schema.json",
    "paper/engineering_collective_forecasting.tex",
    "paper/references.bib",
    "reviews/AI_REVIEWER_PROMPT.md",
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    if missing:
        fail(f"missing required artifacts: {missing}")

    schema = json.loads((ROOT / "schemas/forecast-contract.schema.json").read_text(encoding="utf-8"))
    required = set(schema.get("required", []))
    expected = {"id", "version", "question", "outcome", "timing", "resolution", "context", "safeguards"}
    if not expected.issubset(required):
        fail("forecast schema no longer requires the complete core contract")

    safeguards = schema["properties"]["safeguards"]["properties"]
    if safeguards["shadow_mode"].get("const") is not True:
        fail("Study 0 schema must require shadow_mode=true")
    if safeguards["visible_to_decision_owner_before_resolution"].get("const") is not False:
        fail("Study 0 schema must hide outputs from decision owners before resolution")
    if safeguards["individual_hr_use"].get("const") is not False:
        fail("Study 0 schema must prohibit individual HR use")

    claims = (ROOT / "research/claims.yaml").read_text(encoding="utf-8")
    if "PROPOSED_NOT_TESTED" not in claims or "FUTURE_NOT_STUDY0_PRIMARY" not in claims:
        fail("claim status boundaries are missing")

    chronicle = (ROOT / "research/chronicle/2026-09-25--bootstrap.md").read_text(encoding="utf-8")
    if "No claim that prediction markets are superior" not in chronicle:
        fail("bootstrap non-claim was lost")

    print("PASS: repository structural assurance checks")


if __name__ == "__main__":
    main()
