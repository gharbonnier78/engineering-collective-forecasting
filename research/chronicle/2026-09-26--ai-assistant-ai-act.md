# Chronicle — 2026-09-26 — AI-assistant use and AI Act boundary

Status: **append-only protocol clarification; no Study 0 outcomes exist**

## Trigger

The paper already recorded whether a forecaster consulted an AI assistant because shared AI assistance can correlate private forecasts. The protocol did not yet make the organizational and EU AI Act boundary explicit.

## Clarification added

AI assistants are permitted in Study 0B only as declared ancillary information sources and only through organization-approved usage paths.

The protocol now states:

- `ai_assistant_consulted` remains part of the study information structure;
- optional coarse provider/tool/model-family metadata may be frozen when organizationally permissible;
- prompts, transcripts, secrets, personal data and confidential engineering evidence are excluded from the public research dataset;
- assistant output is non-authoritative and does not replace the participant's probability judgment or the Forecast Contract's authoritative evidence;
- deployment authorization includes proportionate AI-literacy/use guidance;
- individual forecasts, AI-use flags, scores and track records remain prohibited for HR use.

## AI Act boundary

The source basis is Regulation (EU) 2024/1689 and the European Commission's July 2026 Article 50 transparency guidance.

The protocol does **not** classify ordinary assistant consultation as high-risk by default. If the system or study records were later used to monitor/evaluate workers, allocate tasks based on individual behaviour/traits, or influence employment decisions, a separate legal classification would be required and Annex III employment use cases may become relevant.

## Scientific consequence

AI-assistant consultation is a possible shared-information channel and therefore a dependence/confounding descriptor. It is descriptive in Study 0 unless a later protocol separately preregisters an AI-assisted forecasting comparison.

## Gate consequence

No gate status changes. G1 remains PENDING_REREVIEW; this clarification must be included in the next exact-head review.
