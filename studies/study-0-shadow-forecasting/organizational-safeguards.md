# Organizational and ethical safeguards

Study 0 is designed to learn about forecasting **without turning forecasting into governance**.

## Required safeguards

1. **Shadow mode.** Market outputs are withheld from operational decision owners until the contract resolves, unless exposure is itself explicitly studied under a later approved protocol.
2. **No HR use.** Individual forecasts, scores, trading behavior, abstentions or rationales must not be used for performance appraisal, disciplinary action, ranking, promotion or compensation decisions.
3. **Voluntary participation.** Declining to forecast must have no employment consequence.
4. **No real-money betting.** Use virtual points or another approved mechanism unless legal/compliance review explicitly authorizes otherwise.
5. **Pseudonymous analysis.** The research dataset uses participant IDs that are not meaningful outside the authorized mapping store.
6. **Data minimization.** Store only fields needed to answer the preregistered questions. Avoid free-text rationales by default; they create confidentiality and re-identification risk.
7. **Known-outcome abstention.** A participant who already knows the resolved outcome must abstain rather than trade on a non-forecast.
8. **Conflict/influence capture.** Record whether a participant can directly influence the outcome; analyze actor and observer forecasts separately when useful.
9. **Objective resolution.** The resolver follows the frozen rule and authoritative evidence; ambiguous questions are voided, not retrofitted.
10. **Non-retaliation for pessimism.** Management must not use pessimistic forecasts as evidence of disloyalty or poor attitude.
11. **Confidentiality boundary.** Do not expose internal forecasts externally, and do not put internal deployment data in this public repository.
12. **Stop condition.** Pause the pilot if participants report pressure, the output begins influencing real decisions, confidentiality is breached, or the platform cannot provide recoverable audit data.

## Data retention

A private deployment should specify retention separately for:

- identity mapping;
- raw forecasts/trades;
- optional rationales;
- resolved engineering evidence references;
- de-identified analysis extracts.

The public research repository should receive only synthetic examples, schemas, aggregate non-sensitive results approved for publication, and reproducibility metadata.

## Legal/compliance boundary

This repository is not legal advice. Internal use should pass the organization's normal privacy, security, labor/HR, compliance and works-council processes where applicable before employee data are collected.
