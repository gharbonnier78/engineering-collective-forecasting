#!/usr/bin/env python3
"""Fail-closed structural and schema checks for the research protocol."""
from __future__ import annotations

import copy
import csv
import json
from datetime import datetime
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

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
    "templates/forecast-contract.yaml",
    "templates/contract-funnel-register.csv",
    "templates/participant-forecast.csv",
    "paper/engineering_collective_forecasting.tex",
    "paper/references.bib",
    "reviews/AI_REVIEWER_PROMPT.md",
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def parse_iso(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def validate_probability(value: str, label: str) -> None:
    p = float(value)
    if not 0 <= p <= 1:
        fail(f"{label} must lie in [0,1], got {value}")


def main() -> None:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    if missing:
        fail(f"missing required artifacts: {missing}")

    schema = json.loads((ROOT / "schemas/forecast-contract.schema.json").read_text(encoding="utf-8"))
    contract = yaml.safe_load((ROOT / "templates/forecast-contract.yaml").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(contract), key=lambda e: list(e.path))
    if errors:
        fail("forecast template does not validate: " + "; ".join(e.message for e in errors))

    # Mutation guard: a contract cannot claim frozen/closed/resolved/void status
    # while retaining a null freeze record.
    mutated = copy.deepcopy(contract)
    mutated["status"] = "frozen"
    if not list(validator.iter_errors(mutated)):
        fail("schema mutation guard failed: frozen contract accepted with freeze=null")

    required = set(schema.get("required", []))
    expected = {
        "id", "version", "status", "question", "cluster_id", "outcome", "timing",
        "resolution", "institutional_reference", "context", "safeguards", "freeze",
    }
    if not expected.issubset(required):
        fail("forecast schema no longer requires the complete Study 0 contract")

    safeguards = schema["properties"]["safeguards"]["properties"]
    false_controls = [
        "aggregate_visible_to_participants_before_resolution",
        "aggregate_visible_to_decision_owner_before_resolution",
        "aggregate_visible_to_study_decision_scope_before_resolution",
        "individual_hr_use",
        "individual_track_record_hr_use",
        "real_money",
    ]
    if safeguards["shadow_mode"].get("const") is not True:
        fail("Study 0 schema must require shadow_mode=true")
    for control in false_controls:
        if safeguards[control].get("const") is not False:
            fail(f"Study 0 schema must require {control}=false")

    timing = contract["timing"]
    if not (
        parse_iso(timing["elicitation_opens_at"])
        < parse_iso(timing["private_forecasts_close_at"])
        < parse_iso(timing["resolves_no_later_than"])
    ):
        fail("forecast template timing must satisfy open < private close < resolution deadline")

    with (ROOT / "templates/participant-forecast.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        fail("participant forecast template must contain one synthetic example")
    for row in rows:
        validate_probability(row["probability"], "participant probability")
        validate_probability(row["meta_predicted_peer_mean"], "meta-predicted peer mean")
        if row["outcome_already_known"] not in {"yes", "no"}:
            fail("outcome_already_known must be yes/no")
        if row["ai_assistant_consulted"] not in {"yes", "no"}:
            fail("ai_assistant_consulted must be yes/no")

    claims = (ROOT / "research/claims.yaml").read_text(encoding="utf-8")
    for marker in ("ECF-C0A", "ECF-C1", "FUTURE_NOT_STUDY0_PRIMARY"):
        if marker not in claims:
            fail(f"claim boundary marker missing: {marker}")

    chronicle_files = sorted((ROOT / "research/chronicle").glob("*.md"))
    chronicle = "\n".join(p.read_text(encoding="utf-8") for p in chronicle_files)
    if "prediction markets are superior" not in chronicle.lower():
        fail("prediction-market non-claim was lost from Chronicle")
    if "PARTIAL ACCEPT" not in chronicle:
        fail("independent review disposition is not preserved in Chronicle")

    print("PASS: structural, schema, template and claim-boundary checks")


if __name__ == "__main__":
    main()
