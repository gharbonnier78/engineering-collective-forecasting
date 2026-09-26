# Organizational and ethical safeguards

Study 0 is designed to learn about forecasting **without turning forecasting into governance**.

## Required safeguards

1. **Private shadow mode.** Before outcome resolution, no collective aggregate is shown to participants, decision owners, operational governance, or any study-team member who holds decision authority in the contract's scope.
2. **Independent data custodian.** Pre-resolution forecast data and aggregates are held by a role distinct from the accountable owner for that contract. If the principal investigator is also a decision owner, they do not receive the aggregate before resolution.
3. **No HR use.** Individual forecasts, meta-predictions, scores, abstentions, AI-use flags, rationales and longitudinal track records must not be used for appraisal, ranking, compensation, discipline, promotion or supplier/team performance management.
4. **Voluntary participation.** Declining to participate or abstaining on a question has no employment consequence.
5. **No real-money betting.** Study 0 contains no market and no real-money mechanism.
6. **Pseudonymous analysis.** The analysis dataset uses participant identifiers meaningless outside the authorized mapping store.
7. **Data minimization.** No free-text rationale is collected by default. Only preregistered fields needed for the study are retained.
8. **Known-outcome abstention.** A person who already knows the resolved outcome does not submit a forecast.
9. **Actor/observer design factor.** ability_to_influence is mandatory and actor/observer composition is prospectively controlled and reported.
10. **Non-retaliation for pessimism.** Pessimistic forecasts are not evidence of disloyalty, lack of engagement or poor performance.
11. **Objective resolution.** Ambiguous questions are voided rather than retrofitted after outcomes.
12. **Confidentiality boundary.** Internal forecasts and deployment data remain in an approved private store; the public repository receives only generic artifacts and approved aggregate results.
13. **AI-use transparency.** Record whether an AI assistant was consulted, but do not collect confidential prompts/transcripts into the research dataset.
14. **Stop condition.** Pause if participants report pressure, pre-resolution aggregate access occurs, confidentiality is breached, or the protocol begins influencing live decisions beyond ordinary private reflection.

## Interference

Private elicitation can still change how an actor thinks about their work. Therefore the protocol records **detected interference** rather than claiming zero interference.

Interference is assessed by a designated independent assessor after the forecast window using a frozen rubric. It is not used to void a contract in the primary analysis; excluding detected material interference is a sensitivity analysis.

## Participant track records

If longitudinal accuracy records are retained for research:

- they stay pseudonymous in the analysis layer;
- they are compared only on appropriately comparable contract sets;
- they are covered explicitly by the no-HR-use rule;
- publication requires additional aggregation/de-identification review.

## Data retention

A private deployment specifies separate retention for:

- identity mapping;
- raw individual forecasts and meta-predictions;
- AI-use metadata;
- institutional reference forecasts/status;
- evidence references and resolution;
- de-identified analysis extracts.

## AI assistant use and EU AI Act boundary

AI-assistant use is permitted only as a **declared ancillary information source**, through an organization-approved usage path.

Required controls:

- record `ai_assistant_consulted` and, where allowed, a coarse assistance category;
- do not place confidential engineering evidence, personal data, secrets, or restricted project material into an assistant unless the specific approved deployment path authorizes that processing;
- do not copy prompts or assistant transcripts into the public research repository;
- treat assistant outputs as non-authoritative; the human participant owns the forecast and authoritative resolution evidence remains external to the assistant;
- provide role-appropriate AI literacy and usage guidance to participants;
- preserve the no-HR-use rule for forecasts, AI-use flags, scores and longitudinal records.

For professional use under an organization's authority, current European Commission guidance treats the legal person as the deployer rather than each employee acting under its instructions. Article 4 of Regulation (EU) 2024/1689 requires providers and deployers to take measures, to their best extent, to ensure sufficient AI literacy of staff using AI systems. Article 50 transparency obligations apply from 2 August 2026 to certain interactive/generative systems and outputs. This protocol does not assume that ordinary AI-assistant consultation is automatically a high-risk use; however, repurposing AI outputs or forecasting records to monitor/evaluate workers, allocate tasks based on individual characteristics, or influence employment decisions would require a separate AI Act classification and may bring Annex III employment use cases into scope.

This section is a protocol compliance boundary, not legal advice.

## Legal/compliance boundary

This repository is not legal advice. Any internal employee-data collection must pass normal privacy, security, HR/labor, compliance and works-council processes where applicable.
