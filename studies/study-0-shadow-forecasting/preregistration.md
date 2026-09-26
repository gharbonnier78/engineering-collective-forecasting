# Study 0 preregistration template

Status: **protocol candidate — must be frozen before any Study 0 outcome is inspected**

Study 0 is split into two stages. Study 0A tests whether usable Forecast Contracts exist in the real engineering pipeline. Study 0B then tests whether private distributed forecasts add information beyond institutional knowledge. Prediction markets are outside Study 0.

## 1. Study 0A — dry Forecast Contract funnel

Duration: choose and freeze a 4–6 week intake window before starting.

No participants and no forecasting platform are used.

Every candidate event encountered in the predefined event families is entered into the funnel register and assessed prospectively against:

- engineering importance;
- genuine uncertainty at the intended freeze time;
- objective resolvability;
- pre-existing authoritative evidence;
- confidentiality/publication safety;
- non-interference suitability;
- event-family classification, including whether a defensible historical base-rate reference can be constructed.

For candidates that pass, create and freeze a Forecast Contract before the event resolves. After the event, record whether it resolved cleanly, became ambiguous, lacked evidence, or violated the intended scope.

### Study 0A estimands

Report:

- candidate-to-admissible fraction;
- admissible-to-cleanly-resolved fraction;
- reasons for rejection or void;
- event-family distribution;
- time required to draft and resolve contracts.

Study 0A is the primary feasibility test. It makes no forecasting-skill claim.

### Study 0A decision rule

Before the intake window opens, freeze the feasibility gate and the values used to project Study 0B throughput. The protocol-candidate defaults are:

- minimum candidate-to-admissible yield: `Y_min = 0.30`;
- minimum admissible-to-cleanly-resolved rate: `R_clean_min = 0.80`;
- Study 0B structural targets: `J_min = 30` admissible resolved contracts and `K_min = 8` independent clusters;
- maximum projected calendar time to reach both `J_min` and `K_min`: `T_projected_max = 26 weeks`.

A deployment may choose stricter or different values only **before Study 0A begins**, with the rationale recorded in the deployment-specific preregistration.

At the end of Study 0A, compute the observed admissible yield, clean-resolution rate, and projected time to `J_min/K_min` from the prospective intake rate and cluster mix. Study 0B is eligible to proceed only if all frozen feasibility thresholds are met, the potential forecaster pool is compatible with the frozen actor/observer composition rule, and G1/G2/G3 permit it. Otherwise stop/redesign rather than relaxing thresholds after seeing outcomes.

The funnel register must capture identification, drafting/freeze and resolution timestamps, drafting effort, candidate actor/observer pool counts, and a controlled rejection-reason code so these quantities can be computed without participant forecasting.

Allowed `rejection_reason_code` values are:

- `NONE`;
- `NOT_IMPORTANT`;
- `NOT_UNCERTAIN`;
- `NOT_RESOLVABLE`;
- `NO_AUTHORITATIVE_EVIDENCE`;
- `CONFIDENTIALITY_UNSAFE`;
- `INTERFERENCE_RISK`;
- `OUT_OF_SCOPE_EVENT_FAMILY`;
- `OTHER_PREDECLARED`.

Base-rate unavailability is **not** a Study 0A rejection reason by itself.

## 2. Study 0B — research questions

Study 0B starts only if the frozen Study 0A decision rule passes and G1/G2/G3 permit it.

**RQ1 — incremental private collective signal.** At a common frozen information time, does a prospectively specified private collective forecast add predictive information beyond the accountable owner's private probability?

**RQ2 — base-rate skill.** Does that collective forecast improve on the historical base rate for the same prospectively defined event family?

**RQ3 — aggregation method (secondary/exploratory).** How do the raw mean, median and a fixed meta-belief recalibration compare without tuning on Study 0 outcomes?

**RQ4 — information structure (exploratory).** How do actor/observer status, information locality and initial disagreement relate to forecast errors?

## 3. Target population and weighting

Before Study 0B collection, define the target population as all admissible Forecast Contracts encountered during a fixed calendar window from named event families.

Every admissible resolved contract receives equal weight in the primary estimand. Contracts sharing a release, campaign, environment episode or other dependent operational episode share a prospectively assigned cluster_id. Uncertainty is resampled by cluster.

Event-family-stratified summaries are sensitivity/descriptive analyses and do not replace the all-contract primary estimand unless prospectively declared otherwise.

## 4. Same-time institutional and collective references

At freeze time T_f, capture privately and without cross-exposure:

### R0 — historical base rate

A probability p_base derived from a prospectively specified historical reference class. The deployment-specific preregistration must define:

- event-family definition;
- lookback window;
- inclusion/exclusion rule;
- treatment of sparse history;
- rule for freezing the computed base rate.

If a defensible base rate cannot be constructed, record `base_rate_status = unavailable` and the reason. The contract **remains eligible for the primary crowd-vs-owner contrast** if all other admissibility criteria are met. The crowd-vs-base-rate contrast is computed only on the prospectively identified subset with a defensible base rate.

### R1 — institutional signal

Capture:

- p_owner in [0,1], privately elicited from the accountable owner;
- official status already in force at T_f, such as the existing RAG/readiness status;
- source of that official status.

The official status remains descriptive unless a numeric mapping was prospectively defined before outcomes. For the pre-specified descriptive "institutionally positive but privately doubtful" table, freeze before Study 0B collection the exact set of status values counted as positive/green; no post-outcome relabelling is allowed.

### R2 — private collective signal

An eligible forecaster must have legitimate, role-relevant knowledge of the event, the system/process producing it, or the authoritative evidence path. Eligibility must be established prospectively from role and scope; observer quotas cannot be filled with uninformed participants merely to satisfy composition counts.

The accountable owner is always captured separately as R1. The owner may also submit an R2 private forecast only if independently eligible, but the **primary crowd aggregate excludes the owner** to keep the comparator distinct. A descriptive all-eligible-person aggregate including the owner is reported when the owner participates.

Each participant supplies, privately:

- own probability p_i in [0,1];
- expected mean probability m_i that other eligible forecasters will report, in [0,1];
- role category;
- information visibility: common | local_to_role | mixed;
- ability_to_influence: none | indirect | direct;
- outcome_already_known: yes | no;
- ai_assistant_consulted: yes | no;
- category of additional evidence most likely to change the estimate.

No participant sees any other forecast, meta-prediction or aggregate before resolution.

## 5. Primary collective aggregator

The deployment must freeze one primary crowd aggregator before outcomes.

Default protocol candidate:

1. clip each p_i and m_i to [0.01,0.99] for logit arithmetic only;
2. compute L_bar = mean(logit(p_i));
3. compute M_bar = mean(logit(m_i));
4. use a fixed a = 2.0;
5. compute p_crowd = logistic(M_bar + a * (L_bar - M_bar)).

This is a project implementation inspired by shared-information/meta-belief aggregation literature. It is not claimed to reproduce any published algorithm exactly.

The value a = 2.0 is fixed prospectively and must not be retuned on Study 0 outcomes. Raw mean and median remain required comparators.

## 6. Primary estimands

For binary outcome y_j in {0,1}, this project uses the normalized binary quadratic/Brier loss:

BS(p,y) = (p-y)^2.

The original two-category Brier index can be written as twice this value for a binary event; this repository uses the normalized one-component convention consistently.

Primary paired contrast:

Delta_owner,j = BS(p_crowd,j,y_j) - BS(p_owner,j,y_j).

Required reference contrast, on the subset with `base_rate_status = available`:

Delta_base,j = BS(p_crowd,j,y_j) - BS(p_base,j,y_j).

Report mean `Delta_owner` over all otherwise-admissible resolved contracts. Report mean `Delta_base` on the explicitly enumerated base-rate-available subset, with the subset size and event-family composition. Use cluster-bootstrap uncertainty for each applicable contrast.

Negative values indicate lower observed loss for the crowd on the sampled target population. They do not by themselves establish general superiority or decision value.

## 7. Continuation decision rule

Study 0 is an estimation study, not a powered market-comparison trial.

Before Study 0B outcomes, the deployment-specific preregistration must freeze:

- minimum number of admissible resolved contracts J_min;
- minimum number of independent clusters K_min;
- a practically tolerable non-inferiority margin delta_NI on the Brier-loss scale for crowd vs owner;
- the rule for deciding whether Study 1 is justified.

The protocol-candidate structural defaults are `J_min = 30` and `K_min = 8`. The protocol-candidate non-inferiority margin is `delta_NI = 0.02` on the normalized Brier-loss scale, unless a deployment freezes a different value **before Study 0A begins** and documents its operating-characteristic rationale.

At roughly 30 contracts this is a **screening/non-inferiority continuation gate, not a superiority test**. The independent design review's toy operating-characteristic study showed that a `delta_NI = 0.02` rule can reject a crowd that is clearly worse than the owner, but has only limited ability to distinguish near-equality from modest advantage at this scale. If a deployment needs reliable continuation under near-equality or evidence that the crowd is better, it must plan a larger `J` prospectively rather than widen `delta_NI` after outcomes.

A generic continuation rule is:

- feasibility thresholds met;
- upper bound of the preregistered interval for mean Delta_owner does not exceed delta_NI;
- on the base-rate-available subset, mean Delta_base is not materially worse than zero under the separately frozen base-rate criterion;
- no unresolved organizational or confidentiality issue.

Failing this rule means stop/redesign, not "negative proof" that distributed knowledge has no value.

## 8. Participant composition and admissibility

Predeclare actor/observer participation requirements. Recommended default for a primary contract:

- at least 4 valid private forecasts total;
- at least 2 observers with ability_to_influence = none;
- at least 2 actors with ability_to_influence = indirect or direct.

If the deployment cannot sustain those quotas, specify a different fixed rule before outcomes. Contracts that fail the frozen composition rule remain in feasibility accounting but are outside the primary forecast comparison.

Report:

- primary crowd aggregate excluding the accountable owner;
- descriptive all-eligible-person aggregate including the owner when the owner also submitted an R2 forecast;
- actor-only aggregate;
- observer-only aggregate.

No one who already knows the outcome contributes a forecast.

## 9. Independence and data custody

The elicitation interface must not display:

- any reference probability;
- another participant's forecast;
- owner probability;
- base rate;
- aggregate;
- market price.

An independent data custodian stores forecasts until resolution. A principal investigator, data steward or analyst who has decision authority within a contract's operational scope must not access pre-resolution aggregates for that contract.

Longitudinal individual track records, if retained for research, are covered by the no-HR-use rule.

## 10. AI-assistance metadata and compliance boundary

Private does not necessarily mean independent. Forecasters may consult the same AI assistant or shared source, so AI use is part of the information structure and must be observable without turning the assistant into an authority.

Record `ai_assistant_consulted` as yes/no and, if organizationally permissible, an approved coarse assistance category. A deployment may additionally freeze provider/tool/model-family metadata when this can be collected without creating confidentiality or re-identification risk. Do not collect prompts, assistant transcripts, secrets, personal data, or confidential engineering evidence in the public research dataset.

Participants may use only organization-approved AI-assistant paths. Assistant output is advisory: the participant owns the submitted probability, and authoritative resolution evidence remains the source named in the Forecast Contract.

The deployment-specific authorization must include an AI-literacy/use briefing proportionate to the tools and context, consistent with the EU AI Act's Article 4 duty for providers/deployers to take measures for sufficient AI literacy. Article 50 transparency duties for certain interactive and generative systems apply from 2 August 2026. Ordinary assistant consultation is not classified by this protocol as high-risk by default; any later use of AI or forecast records for employee monitoring, performance evaluation, task allocation based on individual characteristics, promotion, termination or similar employment decisions requires a separate legal classification and is outside Study 0.

AI use is descriptive in Study 0 unless separately preregistered.

## 11. Resolution and evidence

Each contract must pass the schema and identify pre-existing authoritative evidence.

Resolution statuses:

- RESOLVED_TRUE
- RESOLVED_FALSE
- VOID_AMBIGUOUS
- VOID_MISSING_EVIDENCE

Interference is recorded separately and is not itself a resolution status.

A resolver follows the frozen rule and, where feasible, is distinct from the accountable owner and data custodian.

## 12. Interference assessment

Private elicitation can itself prompt reflection even when no aggregate is shown.

An independent custodian or designated assessor assigns I in {0,1,2} after the forecast window using a frozen rubric and without seeing forecast accuracy when feasible:

- I=0: no detected study-caused operational change;
- I=1: discussion/attention but no material change;
- I=2: material change in action, timing, resources or evidence generation plausibly caused by study participation.

Primary analysis is intention-to-observe: otherwise resolvable I=2 contracts remain in the primary dataset. A preregistered sensitivity analysis excludes I=2. Therefore C0B can claim only absence/presence of **detected** interference.

## 13. Metrics

Confirmatory/pre-specified:

- Study 0A funnel and clean-resolution rates;
- mean Delta_owner;
- mean Delta_base;
- participation and composition admissibility;
- burden and detected interference, including detected interference counts/rates by owner, actor and observer role.

Descriptive:

- Brier loss by owner, base rate, primary crowd, mean and median;
- official-status/outcome cross-tabulation;
- a pre-specified "institutionally positive but privately doubtful" table: freeze the set of official status values counted as positive/green before collection, then report cases where `official_status` is in that set while the primary private-crowd probability is < 0.50, together with eventual outcomes;
- calibration/reliability plots with counts and uncertainty;
- sharpness;
- actor-only and observer-only scores.

Exploratory:

- meta-recalibration vs raw mean/median;
- association with information locality, AI-assistance flag and belief dispersion;
- alternative thresholds or status mappings beyond the frozen descriptive green/<0.50 table.

## 14. Randomness and uncertainty

Reference bootstrap seed: 20260926 unless a deployment freezes another integer before outcomes.

Use 10,000 nonparametric bootstrap resamples of independent cluster units. The analysis implementation must reject fewer than 2 clusters. If K < 8, interval-based inference is labelled exploratory even when the point estimate is reported.

A sensitivity analysis reports:

- equal-contract weighting;
- cluster-aggregated weighting;
- actor-only and observer-only contrasts.

## 15. Stopping

Freeze one rule before collection:

- fixed calendar window; or
- fixed number of admissible resolved contracts plus a maximum calendar end.

No outcome-dependent stopping is allowed.

## 16. Publication rule

Report every registered contract, including rejected, void, under-participated and missing-evidence cases. Report null and adverse results. State the exact target population, event families, calendar period, base-rate construction, exclusions, cluster count, participant composition and aggregation constants.

Study 0 must not be described as a prediction-market evaluation.
