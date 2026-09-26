#!/usr/bin/env python3
"""Fail-closed structural and template checks for the research protocol."""
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
    "templates/study-event-register.csv",
    "templates/resolution-record.yaml",
    "paper/engineering_collective_forecasting.tex",
    "paper/references.bib",
    "reviews/AI_REVIEWER_PROMPT.md",
]

YES_NO = {"yes", "no"}
RESOLUTION_STATUSES = {
    "RESOLVED_TRUE",
    "RESOLVED_FALSE",
    "VOID_AMBIGUOUS",
    "VOID_MISSING_EVIDENCE",
}
REJECTION_CODES = {
    "NONE",
    "NOT_IMPORTANT",
    "NOT_UNCERTAIN",
    "NOT_RESOLVABLE",
    "NO_AUTHORITATIVE_EVIDENCE",
    "CONFIDENTIALITY_UNSAFE",
    "INTERFERENCE_RISK",
    "OUT_OF_SCOPE_EVENT_FAMILY",
    "OTHER_PREDECLARED",
}


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def parse_iso(value: str) -> datetime:
    if not value:
        fail("required ISO timestamp is empty")
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def validate_probability(value: str, label: str, *, allow_empty: bool = False) -> None:
    if value == "" and allow_empty:
        return
    p = float(value)
    if not 0 <= p <= 1:
        fail(f"{label} must lie in [0,1], got {value}")


def read_csv(path: str) -> tuple[list[str], list[dict[str, str]]]:
    with (ROOT / path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        return list(reader.fieldnames or []), rows


def require_columns(path: str, columns: set[str]) -> tuple[list[str], list[dict[str, str]]]:
    fields, rows = read_csv(path)
    missing = columns.difference(fields)
    if missing:
        fail(f"{path}: missing columns {sorted(missing)}")
    if not rows:
        fail(f"{path}: must contain one synthetic example")
    return fields, rows


def main() -> None:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    if missing:
        fail(f"missing required artifacts: {missing}")

    # Forecast Contract YAML <-> JSON schema.
    schema = json.loads((ROOT / "schemas/forecast-contract.schema.json").read_text(encoding="utf-8"))
    contract = yaml.safe_load((ROOT / "templates/forecast-contract.yaml").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(contract), key=lambda e: list(e.path))
    if errors:
        fail("forecast template does not validate: " + "; ".join(e.message for e in errors))

    mutated = copy.deepcopy(contract)
    mutated["status"] = "frozen"
    if not list(validator.iter_errors(mutated)):
        fail("schema mutation guard failed: frozen contract accepted with freeze=null")

    unavailable = copy.deepcopy(contract)
    unavailable["institutional_reference"].pop("base_rate_reference_class", None)
    unavailable["institutional_reference"].pop("base_rate_source", None)
    unavailable["institutional_reference"]["base_rate_status"] = "unavailable"
    unavailable["institutional_reference"]["base_rate_unavailable_reason"] = "no defensible historical reference class"
    if list(validator.iter_errors(unavailable)):
        fail("schema must permit an otherwise-valid no-base-rate contract for the owner primary contrast")

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

    # Study 0A funnel template.
    _, funnel_rows = require_columns(
        "templates/contract-funnel-register.csv",
        {
            "candidate_id", "event_family", "identified_at", "drafting_started_at",
            "contract_frozen_at", "resolved_at", "drafting_effort_minutes",
            "important", "uncertain", "resolvable", "authoritative_evidence_available",
            "confidentiality_safe", "non_interfering", "base_rate_reference_available",
            "potential_eligible_actors", "potential_eligible_observers",
            "admitted_contract_id", "rejection_reason_code", "resolution_status",
        },
    )
    for row in funnel_rows:
        for name in (
            "important", "uncertain", "resolvable", "authoritative_evidence_available",
            "confidentiality_safe", "non_interfering", "base_rate_reference_available",
        ):
            if row[name] not in YES_NO:
                fail(f"contract funnel {name} must be yes/no")
        if row["rejection_reason_code"] not in REJECTION_CODES:
            fail(f"unknown rejection_reason_code: {row['rejection_reason_code']}")
        if row["resolution_status"] not in RESOLUTION_STATUSES:
            fail(f"unknown funnel resolution_status: {row['resolution_status']}")
        if int(row["drafting_effort_minutes"]) < 0:
            fail("drafting_effort_minutes must be non-negative")
        if int(row["potential_eligible_actors"]) < 0 or int(row["potential_eligible_observers"]) < 0:
            fail("potential forecaster pool counts must be non-negative")
        if row["admitted_contract_id"] and row["rejection_reason_code"] != "NONE":
            fail("admitted funnel candidate must use rejection_reason_code=NONE")
        times = [parse_iso(row[k]) for k in ("identified_at", "drafting_started_at", "contract_frozen_at", "resolved_at")]
        if times != sorted(times):
            fail("funnel timestamps must satisfy identified <= drafting <= frozen <= resolved")

    # Participant template.
    _, participant_rows = require_columns(
        "templates/participant-forecast.csv",
        {
            "contract_id", "participant_pseudonym", "forecasted_at", "probability",
            "meta_predicted_peer_mean", "role_category", "eligibility_basis",
            "is_accountable_owner", "information_visibility", "ability_to_influence",
            "outcome_already_known", "ai_assistant_consulted", "ai_assistance_category",
        },
    )
    for row in participant_rows:
        validate_probability(row["probability"], "participant probability")
        validate_probability(row["meta_predicted_peer_mean"], "meta-predicted peer mean")
        if not row["eligibility_basis"].strip():
            fail("participant eligibility_basis must be non-empty")
        if row["is_accountable_owner"] not in YES_NO:
            fail("is_accountable_owner must be yes/no")
        if row["information_visibility"] not in {"common", "local_to_role", "mixed"}:
            fail("invalid information_visibility")
        if row["ability_to_influence"] not in {"none", "indirect", "direct"}:
            fail("invalid ability_to_influence")
        if row["outcome_already_known"] not in YES_NO:
            fail("outcome_already_known must be yes/no")
        if row["ai_assistant_consulted"] not in YES_NO:
            fail("ai_assistant_consulted must be yes/no")

    # Event-register template.
    _, event_rows = require_columns(
        "templates/study-event-register.csv",
        {
            "contract_id", "cluster_id", "freeze_time", "resolution_status", "outcome",
            "interference_level", "participants_total", "participants_actor",
            "participants_observer", "owner_also_forecaster", "base_rate_status",
            "base_rate_probability", "base_rate_unavailable_reason", "owner_probability",
            "official_status", "official_status_is_positive", "crowd_primary_probability",
            "crowd_including_owner_probability", "independent_mean_probability",
            "independent_median_probability",
        },
    )
    for row in event_rows:
        parse_iso(row["freeze_time"])
        if row["resolution_status"] not in RESOLUTION_STATUSES:
            fail(f"unknown event resolution_status: {row['resolution_status']}")
        if row["outcome"] not in {"0", "1"}:
            fail("event outcome must be 0 or 1")
        if row["interference_level"] not in {"0", "1", "2"}:
            fail("interference_level must be 0, 1, or 2")
        if row["owner_also_forecaster"] not in YES_NO or row["official_status_is_positive"] not in YES_NO:
            fail("owner_also_forecaster and official_status_is_positive must be yes/no")
        for name in ("participants_total", "participants_actor", "participants_observer"):
            if int(row[name]) < 0:
                fail(f"{name} must be non-negative")
        validate_probability(row["owner_probability"], "owner probability")
        validate_probability(row["crowd_primary_probability"], "primary crowd probability")
        validate_probability(row["crowd_including_owner_probability"], "including-owner crowd probability", allow_empty=True)
        validate_probability(row["independent_mean_probability"], "mean probability")
        validate_probability(row["independent_median_probability"], "median probability")
        if row["base_rate_status"] == "available":
            validate_probability(row["base_rate_probability"], "base-rate probability")
            if row["base_rate_unavailable_reason"]:
                fail("available base rate must not carry an unavailable reason")
        elif row["base_rate_status"] == "unavailable":
            if row["base_rate_probability"]:
                fail("unavailable base rate must have empty probability")
            if not row["base_rate_unavailable_reason"].strip():
                fail("unavailable base rate requires a reason")
        else:
            fail("base_rate_status must be available or unavailable")

    # Resolution-record template.
    resolution = yaml.safe_load((ROOT / "templates/resolution-record.yaml").read_text(encoding="utf-8"))
    for key in (
        "contract_id", "contract_version", "resolution_status", "resolved_at", "resolver_role",
        "authoritative_evidence_ref", "outcome", "interference_level", "interference_assessor_role",
    ):
        if key not in resolution:
            fail(f"resolution record missing {key}")
    if resolution["resolution_status"] not in RESOLUTION_STATUSES:
        fail("invalid resolution_status in resolution record")
    parse_iso(resolution["resolved_at"])
    if resolution["outcome"] not in (0, 1):
        fail("resolution outcome must be 0 or 1")
    if resolution["interference_level"] not in (0, 1, 2):
        fail("resolution interference_level must be 0, 1, or 2")

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

    print("PASS: structural, schema, all-template and claim-boundary checks")


if __name__ == "__main__":
    main()
