# Hypermind / Prescience as an instrument candidate

Status: **instrument note, not endorsement and not a scientific dependency**

A mature prediction-market platform can reduce experimental confounding compared with building a new market engine solely for Study 0. Hypermind/Prescience is one candidate because its public product material describes enterprise forecasting, private cohorts and deployment/integration options.

## Why vendor-neutrality matters

The scientific object is the comparison among independent forecasts, simple aggregation and a market mechanism. The protocol should survive a change of vendor. Therefore all platform-specific behavior must be mapped into frozen configuration fields and exported raw data.

## Due diligence before internal use

Confirm in writing and record:

- exact deployment model (cloud, private cloud, local/on-prem) and outbound dependencies;
- SSO/OIDC/SAML and RBAC behavior;
- data residency, encryption, backups, retention and deletion;
- administrator/support access and audit logs;
- whether forecasts/rationales are used for model training or analytics outside the tenant;
- raw export/API availability for forecasts, trades, timestamps, market states and resolution;
- market-maker/scoring algorithm and parameter versioning;
- whether AI summarization, web/news retrieval, recommendations or social features can be disabled;
- pseudonymous participation options;
- incident response and contractual security/privacy commitments.

## Study 0 preferred configuration

- virtual currency/points;
- independent private forecast captured before market exposure;
- market aggregate hidden from operational decision owners until resolution;
- AI/news/retrieval assistance disabled unless separately studied;
- minimal/no free-text rationale;
- immutable export at close;
- reproducible algorithm/version/parameter record.

A platform's own accuracy claims are vendor claims until independently verified for the intended use. Study 0 must score the local data regardless of product marketing.
